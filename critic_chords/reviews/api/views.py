from rest_framework import generics, views, status
from rest_framework.response import Response

from . import serializers, mixins
from .stat import Stat
from critic_chords.reviews import models as reviews_models


class ReviewCreateListView(
    mixins.NestedAlbumViewMixin,
    generics.ListCreateAPIView
):
    def get_queryset(self):
        return reviews_models.Review.objects.filter(album=self.album)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return serializers.ReviewListSerializer
        return serializers.ReviewCreateSerializer

    def perform_create(self, serializer):
        serializer.save()
        serializer.instance.album.update_overall_rating()


class UserStatsView(views.APIView):
    def get(self, request, user_email, *args, **kwargs):
        stats = {
            "reviews_written": (
                reviews_models.Review.objects.get_commented_by(
                    user=user_email).count()
            ),
            "reviews_liked": (
                reviews_models.Like.objects.get_by_user(
                    user=user_email).count()
            ),
            "albums_rated": (
                reviews_models.Review.objects.get_by_user(
                    user=user_email).count()
            )
        }
        stats_serializer = serializers.UserStatsResponseSerializer(
            Stat(**stats))
        return Response(data=stats_serializer.data, status=status.HTTP_200_OK)


class MostRecentReviewsView(generics.ListAPIView):
    queryset = reviews_models.Review.objects.latest()
    serializer_class = serializers.ReviewListSerializer


class LikeCreateView(mixins.NestedReviewViewMixin, generics.CreateAPIView):
    queryset = reviews_models.Review.objects.all()
    serializer_class = serializers.LikeCreateSerializer

    def perform_create(self, serializer):
        serializer.instance.review = self.review
        serializer.save()
