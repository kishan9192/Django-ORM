from core.models import Restaurants


def run():
    restaurants = Restaurants.objects.all()
    count = Restaurants.objects.count()
    firstRestaurant = Restaurants.objects.all()[0]
    lastRestaurant = Restaurants.objects.last()
    print(lastRestaurant)
    print(firstRestaurant)
    print(count)
    print(restaurants)