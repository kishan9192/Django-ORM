from core.models import Restaurants, Rating
from django.contrib.auth.models import User

def run():
    restaurant = Restaurants.objects.first()
    user = User.objects.first()
    Rating.objects.create(
        user=user,
        restaurant=restaurant,
        rating=3
    )