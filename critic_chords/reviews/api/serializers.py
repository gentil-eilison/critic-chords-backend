from datetime import date

from rest_framework import serializers

from critic_chords.reviews import models as reviews_models


class UserStatsResponseSerializer(serializers.Serializer):
    reviews_liked = serializers.IntegerField()
    reviews_written = serializers.IntegerField()
    albums_rated = serializers.IntegerField()


class ReviewListSerializer(serializers.ModelSerializer):
    days_since = serializers.SerializerMethodField()

    class Meta:
        model = reviews_models.Review
        fields = ("id", "rating", "commentary", "user", "days_since", "likes")
        depth = 1

    def get_days_since(self, review: reviews_models.Review):
        delta = date.today() - review.created_at.date()
        return delta.days


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = reviews_models.Review
        fields = ("rating", "commentary", "user")

    def create(self, validated_data):
        return reviews_models.Review.objects.create(
            album=self.context.get("album"),
            **validated_data
        )


class LikeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = reviews_models.Like
        fields = ("user",)

    def create(self, validated_data):
        return reviews_models.Like.objects.create(
            review=self.context.get("review"),
            **validated_data
        )
