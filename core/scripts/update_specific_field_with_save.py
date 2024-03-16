from core.models import Restaurants

# THis performs an optimised SQL query behind the scenes, because if we execute script1
# it will perform an UPDATE query and not just the name field, it will update all the fields
# along with the name field

# Whereas when we execute the optimisedQuery, it only updates the name field, since we have passed
# the argument update_fields which is a list of all the fields that we want to update while performing save.


def script1():
    restaurants = Restaurants.objects.first()
    restaurants.name = "My italian dhaba"
    restaurants.save()


def optimisedQuery():
    restaurants = Restaurants.objects.first()
    restaurants.name = "My italian dhaba"
    restaurants.save(update_fields=["name"])


def run():
    # script1()
    optimisedQuery()
