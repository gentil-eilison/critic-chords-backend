from django.db import models


class ReviewQuerySet(models.QuerySet):
    def get_by_user(self, user: str):
        return self.filter(user=user)

    def get_commented_by(self, user: str):
        return self.get_by_user(user).exclude(commentary="")

    def latest(self):
        return self.all().order_by("-created_at")[:5]


class LikeQuerySet(models.QuerySet):
    def get_by_user(self, user: str):
        return self.filter(user=user)
