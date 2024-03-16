
# Ratings table has the restaurant id as reference, and we can get the restaurant details
# after getting an instance of rating class. 
# But what if we have the instance of restaurant class and we want all the ratings of that particular restaurant
# this is called backward relation, and django by-default maintains the backward relation
# In order to fetch the details of the ratings from restaurant object,
# the functions of the manager have to be called
# manager is jispe hum .count(), .all(), .first() methods apply karte h
# so the default name that django maintains of this manager is "maintablename_set"
# here maintable is the table which stores the foreign key, in our case it is rating table
# therefore manager name will be rating_set
# while defining the foreign key we can also change this name, the third argument in foreign key 
# is related_name and the name provided to that argument becomes the name of the manager that maintains the backward relations
# 'ratings' in this example. Take a look at the Ratings class in models where restaurant is added as foreign key for reference.

from core.models import Restaurants

def run():
    restaurant = Restaurants.objects.first()
   
    # below line is when the name of the manager was not provided. this is the default name. try by removing the related_name in foreign key in Rating model class
    # rating = restaurant.rating_set.all() 
    # print(rating)

    rating_with_custom_name_of_manager = restaurant.ratings.all()
    print(rating_with_custom_name_of_manager)