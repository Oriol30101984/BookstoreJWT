from django.urls import include, path
from rest_framework import routers
from . import views


AuthorRouter = routers.DefaultRouter()
BookRouter = routers.SimpleRouter()
AuthorRouter.register(r'autores', views.AuthorViewSet)
BookRouter.register(r'libros', views.BookViewSet)

urlpatterns = [
    path('', include(AuthorRouter.urls)),
    path('', include(BookRouter.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]