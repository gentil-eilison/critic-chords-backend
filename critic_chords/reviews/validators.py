from django.core.exceptions import ValidationError


def validate_rating(value: int):
    if value < 0 or value > 5:
        raise ValidationError(
            "%(value)s must be between 0 and 5",
            params={"value": value}
        )
