from django.db.models import Q

from django_filters import rest_framework as filters

from critic_chords.albums import models as albums_models


SEARCH_BY_CHOICES = (
    (0, 'All'),
    (1, 'Artist'),
    (2, 'Album'),
)


class AlbumFilter(filters.FilterSet):
    search_by = filters.ChoiceFilter(
        choices=SEARCH_BY_CHOICES,
        method="filter_by_search_by"
    )
    name = filters.CharFilter(method="filter_by_artist_or_album_name")

    class Meta:
        model = albums_models.Album
        fields = ("genre", "release_year")

    def filter_by_search_by(self, queryset, *args, **kwargs):
        return queryset
    
    def filter_by_artist_or_album_name(self, queryset, name, value):
        name_type = self.data.get("search_by")
        return queryset.get_by_name_and_type(value, name_type)
