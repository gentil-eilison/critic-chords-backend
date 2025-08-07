from django.urls import path
from . import views

app_name = "albums"

urlpatterns = [
    path("albums/", views.AlbumListView.as_view(), name="list"),
    path("albums/<int:pk>/", views.AlbumDetailView.as_view(), name="detail"),
    path("genres/", views.GenreListView.as_view(), name="genre_list")
]
