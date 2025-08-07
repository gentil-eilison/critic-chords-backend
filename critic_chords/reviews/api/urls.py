from django.urls import path

from . import views


app_name = "reviews"

urlpatterns = [
    path("albums/<int:album_id>/reviews/",
         views.ReviewCreateListView.as_view(), name="create")
]
