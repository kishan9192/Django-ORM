from core.models import Restaurants
from django.utils import timezone

def run():
    restaturant = Restaurants()
    restaturant.name = 'My Italian restaurant'
    restaturant.date_opened = timezone.now()
    restaturant.latitude = 50.2
    restaturant.longitude = 50.2
    restaturant.website = 'www.google.com'
    restaturant.restaurant_type = restaturant.TypeChoices.ITALIAN

    restaturant.save()