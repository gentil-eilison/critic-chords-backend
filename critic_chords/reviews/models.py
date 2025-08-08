from django.db import models

from critic_chords.core import models as core_models
from critic_chords.albums import models as albums_models
from . import validators, querysets


class Review(core_models.CreatedAtModel):
    rating = models.PositiveSmallIntegerField(
        verbose_name="Rating",
        default=0,
        validators=[validators.validate_rating]
    )
    commentary = models.TextField(verbose_name="Commentary", blank=True)
    user = models.EmailField()
    album = models.ForeignKey(
        albums_models.Album,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    objects: querysets.ReviewQuerySet = querysets.ReviewQuerySet.as_manager()

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
        constraints = [
            models.UniqueConstraint(
                "user",
                "album",
                name="unique_user_album"
            )
        ]


class Like(core_models.CreatedAtModel):
    user = models.EmailField()
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name="reviews"
    )
    objects: querysets.LikeQuerySet = querysets.LikeQuerySet.as_manager()

    class Meta:
        verbose_name = "Like"
        verbose_name_plural = "Likes"
        constraints = [
            models.UniqueConstraint(
                "user",
                "review",
                name="unique_user_review"
            )
        ]
