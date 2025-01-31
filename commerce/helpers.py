from .models import Product


def get_recently_viewed_products(request):
    recently_viewed = request.session.get('recently_viewed', [])
    products = Product.objects.filter(pk__in=recently_viewed)
    return products

def update_recently_viewed(request, product_id):
    recently_viewed = request.session.get('recently_viewed', [])
    if product_id in recently_viewed:
        recently_viewed.remove(product_id)
    recently_viewed.insert(0, product_id)
    if len(recently_viewed) > 5:
        recently_viewed = recently_viewed[:3]
    request.session['recently_viewed'] = recently_viewed