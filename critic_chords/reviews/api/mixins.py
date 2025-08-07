from rest_framework.generics import get_object_or_404

from critic_chords.albums import models as albums_models


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
