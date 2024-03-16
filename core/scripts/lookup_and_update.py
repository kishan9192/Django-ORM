from core.models import Restaurants
from django.utils import timezone


# THis performs lookup on the the table to find out all the restaurants that start with the letter M
# Post that it performs the update on the queryset, updates all the records returned
# Updates their field "date_opened"
def run():
    restaurants = Restaurants.objects.filter(name__startswith="M")
    print("restaurants", restaurants)
    restaurants.update(date_opened=timezone.now())
