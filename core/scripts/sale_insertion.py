from core.models import Restaurants, Sale
from django.utils import timezone

def run():
    restaurant = Restaurants.objects.first()
    Sale.objects.create(
        restaurant=restaurant,
        income = 13000,
        datetime = timezone.now()
    )
    