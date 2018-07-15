from products.models import Category


def get_categories(request):
    category = Category.objects.filter(parent__isnull=True)
    return {'maincategory': category}


