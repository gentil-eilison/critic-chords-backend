from django.db import models


class AlbumQuerySet(models.QuerySet):
    def get_by_name_and_type(self, name: str, name_type: str):
        lookups = (
            {"artist__name__icontains": name}, 
            {"title__icontains": name}
        )
        if name_type == "1":
            return self.filter(**lookups[0])
        if name_type == "2":
            return self.filter(**lookups[1])
        return self.filter(
            models.Q(**lookups[0]) |
            models.Q(**lookups[1])
        )
