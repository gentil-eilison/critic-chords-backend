from rest_framework import serializers

from critic_chords.albums import models as albums_models


class AlbumListSerializer(serializers.ModelSerializer):
    genre = serializers.CharField(source="genre.name")
    artist = serializers.CharField(source="artist.name")

    class Meta:
        model = albums_models.Album
        fields = (
            "id", "title", "release_year",
            "duration", "tracks", "label",
            "genre", "artist", "cover_art",
            "about"
        )


class AlbumDetailSerializer(AlbumListSerializer):
    class Meta:
        model = albums_models.Album
        fields = AlbumListSerializer.Meta.fields + ("reviews",)
        depth = 1


class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = albums_models.Genre
        fields = ("id", "name")
