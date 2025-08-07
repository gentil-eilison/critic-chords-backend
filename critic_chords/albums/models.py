from django.db import models

from critic_chords.core import models as core_models
from . import querysets


class Genre(core_models.CreatedAtModel):
    name = models.CharField(
        max_length=128,
        verbose_name="Name",
        unique=True
    )

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"

    def __str__(self) -> str:
        return self.name


class Artist(core_models.CreatedAtModel):
    name = models.CharField(
        max_length=255
    )

    class Meta:
        verbose_name = "Artist"
        verbose_name_plural = "Aritsts"

    def __str__(self) -> str:
        return self.name


class Album(core_models.CreatedAtModel):
    title = models.CharField(
        max_length=255,
        verbose_name="Title",
    )
    release_year = models.PositiveSmallIntegerField(
        verbose_name="Release Year"
    )
    duration = models.PositiveIntegerField(
        verbose_name="Duration"
    )
    tracks = models.PositiveSmallIntegerField(
        verbose_name="Tracks"
    )
    label = models.CharField(
        max_length=128,
        verbose_name="Label"
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.PROTECT,
        related_name="albums"
    )
    artist = models.ForeignKey(
        Artist,
        on_delete=models.CASCADE,
        related_name="albums"
    )
    cover_art = models.ImageField(
        verbose_name="Cover Art",
        blank=True,
        null=True
    )
    about = models.TextField(
        verbose_name="About"
    )
    objects = querysets.AlbumQuerySet.as_manager()

    class Meta:
        verbose_name = "Album"
        verbose_name_plural = "Albums"

    def __str__(self) -> str:
        return self.title
