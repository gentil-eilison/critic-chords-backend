from rest_framework import generics

from . import serializers, mixins
from critic_chords.reviews import models as reviews_models


class ReviewCreateListView(
    mixins.NestedAlbumViewMixin,
    generics.ListCreateAPIView
):
    queryset = reviews_models.Review.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return serializers.ReviewListSerializer
        return serializers.ReviewCreateSerializer
