from rest_framework import serializers

from critic_chords.albums import models as albums_models


class AlbumSerializer(serializers.ModelSerializer):
    genre = serializers.CharField(source="genre.name")
    artist = serializers.CharField(source="artist.name")
    reviews_count = serializers.IntegerField(
        source="reviews.count"
    )

    class Meta:
        model = albums_models.Album
        fields = (
            "id", "title", "release_year",
            "duration", "tracks", "label",
            "genre", "artist", "cover_art",
            "about", "reviews_count", "overall_rating"
        )


class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = albums_models.Genre
        fields = ("id", "name")
