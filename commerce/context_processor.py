from productcart.cart import Cart
from base.views import G


def cartpros(request):
    return {'cart': Cart(request)}



def catnav(request):
    catlist = G.cat

    return {'catlist': catlist}

def banner(request):
    carousel = G.image

    banner_data = [
        {
            "carousel": item,
            "banner": item.carouselnewlisting.all(),
            "otherbanner": item.carouselotherimages.all()
        }
        for item in carousel
    ]

    return {'banner': banner_data}
