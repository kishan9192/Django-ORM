from core.models import Restaurants

def run():
    restaurant = Restaurants.objects.first()
    sale = restaurant.sale_set.all()[0]
    # even though sale stores the reference of restaurant, 
    # from the reference django can fetch all the data of 
    # that particular reference from its respective table, 
    # in this case rating object is fetched, 
    # and we can access all the fields of the ratings object.
    print(sale.income)