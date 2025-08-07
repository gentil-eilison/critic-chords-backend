from rest_framework import serializers

from critic_chords.reviews import models as reviews_models


class UserStatsSerializer(serializers.Serializer):
    reviews_liked = serializers.IntegerField()
    reviews_written = serializers.IntegerField()
    albums_rated = serializers.IntegerField()


class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = reviews_models.Review
        fields = ("id", "rating", "commentary", "user")


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = reviews_models.Review
        fields = ("rating", "commentary", "user")

    def create(self, validated_data):
        return reviews_models.Review.objects.create(
            album=self.context.get("album"),
            **validated_data
        )
