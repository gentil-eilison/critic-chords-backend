from rest_framework import generics

from critic_chords.albums import models as albums_models
from . import serializers
from . import filters


class AlbumListView(generics.ListAPIView):
    queryset = albums_models.Album.objects.all()
    serializer_class = serializers.AlbumSerializer
    filterset_class = filters.AlbumFilter


class AlbumDetailView(generics.RetrieveAPIView):
    queryset = albums_models.Album.objects.all()
    serializer_class = serializers.AlbumSerializer


class GenreListView(generics.ListAPIView):
    queryset = albums_models.Genre.objects.all()
    serializer_class = serializers.GenreListSerializer
