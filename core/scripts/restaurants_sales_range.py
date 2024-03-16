from core.models import Sale


def run():
    sales = Sale.objects.filter(income__range=(50, 60))
    for sale in sales:
        print(sale.restaurant.name)
