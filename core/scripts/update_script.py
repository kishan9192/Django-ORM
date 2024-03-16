from core.models import Restaurants

def run():
    restaurant = Restaurants.objects.first()
    print(restaurant.name) #prints old name
    restaurant.name = 'My dhaba'
    restaurant.save() # saves the new name as My dhaba


    #to run these scripts do -> python manage.py runscript script_name
    #eg: python manage.py runscript update_script