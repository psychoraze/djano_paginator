from django.urls import path
from .views import *

urlpatterns = [
    path("", albums, name="albums"),
    path("albums_class/", AlbumList.as_view(), name="albums_class"),
    path("create_album/", CreateAlbum.as_view(), name="create_album"),
]
