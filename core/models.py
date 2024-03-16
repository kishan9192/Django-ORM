from django.db import models
from django.contrib.auth.models import User


class Restaurants(models.Model):
    class TypeChoices(models.TextChoices):
        INDIAN = "IN", "Indian"
        CHINESE = "CH", "Chinese"
        ITALIAN = "IT", "Italian"
        GREEK = "GR", "Greek"
        MEXICAN = "MX", "Mexican"
        FASTFOOD = "FF", "FastFood"
        OTHER = "OT", "Other"

    name = models.CharField(max_length=100)
    date_opened = models.DateField()
    website = models.URLField(default="")
    latitude = models.FloatField()
    longitude = models.FloatField()
    restaurant_type = models.CharField(max_length=2, choices=TypeChoices.choices)

    def __str__(self):
        return self.name

    # Override save method of django ORM to check if the field exist or the field is being added
    def save(self, *args, **kwargs):
        print(self._state.adding)
        super().save(*args, **kwargs)


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(
        Restaurants, on_delete=models.CASCADE, related_name="ratings"
    )
    rating = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"Rating: {self.rating}"


class Sale(models.Model):
    restaurant = models.ForeignKey(Restaurants, on_delete=models.SET_NULL, null=True)
    income = models.DecimalField(max_digits=8, decimal_places=2)
    datetime = models.DateTimeField()
