from rest_framework.generics import get_object_or_404

from critic_chords.albums import models as albums_models
from critic_chords.reviews import models as reviews_models


class NestedAlbumViewMixin:
    album = None

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)
        album_id = kwargs.get("album_id")
        if not album_id:
            raise Exception(
                "You must specify album_id path param when using NestedAlbumViewMixin")
        self.album = get_object_or_404(albums_models.Album, id=album_id)

    def get_serializer_context(self):
        context: dict = super().get_serializer_context()
        context.update({"album": self.album})
        return context


class NestedReviewViewMixin:
    review = None

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)
        review_id = kwargs.get("review_id")
        if not review_id:
            raise Exception(
                "You must specify review_id path param when using NestedReviewViewMixin")
        self.review = get_object_or_404(reviews_models.Review, id=review_id)

    def get_serializer_context(self):
        context: dict = super().get_serializer_context()
        context.update({"review": self.review})
