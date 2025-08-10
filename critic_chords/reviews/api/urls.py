from django.urls import path

from . import views


app_name = "reviews"

urlpatterns = [
    path("albums/<int:album_id>/reviews/",
         views.ReviewCreateListView.as_view(), name="create"),
    path("reviews/<str:user_email>/stats/",
         views.UserStatsView.as_view(), name="user_stats"),
    path("reviews/latest/",
         views.MostRecentReviewsView.as_view(), name="latest")
]
