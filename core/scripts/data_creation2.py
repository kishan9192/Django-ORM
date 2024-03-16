from core.models import Restaurants
from django.utils import timezone

def run():
    Restaurants.objects.create(
        name = 'Hunger hacker',
        longitude = 50.2,
        latitude = 50.2,
        date_opened = timezone.now(),
        restaurant_type = Restaurants.TypeChoices.CHINESE
    )