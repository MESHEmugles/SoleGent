import json
from datetime import datetime, timedelta


from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse


from commerce.models import *
from .models import *
from productcart.models import *
from dataclasses import dataclass

@dataclass
class G:
    prod = Product.objects.all()
    cat = Category.objects.all()
    cart = ProductCart.objects.all()
    image = CarouselImage.objects.all()


def index(request,category_slug= None):
    product = G.prod
    cateogry = None
    today = datetime.now()
    day_before_yesterday = (today - timedelta(days=2)).strftime('%Y-%m-%d')

    if category_slug:
        category = get_object_or_404(Category, slug = category_slug)
        product = G.prod.filter(category=category)[:5]
    
    newlisting = product.filter(created__range = [day_before_yesterday, today.strftime('%Y-%m-%d')] )


    return render(request, 'pages/index.html', {"product":product, 'newlisted':newlisting})

def about(request):
    
    return render(request, 'pages/aboutus.html')

def contact(request):
    
    return render(request, 'pages/contact.html')


def save_email(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        if email:
            if NewsLetter.objects.filter(email=email).exists():
                return JsonResponse({'success': "We've got this email, thanks for subscribing"}, status=200)
            NewsLetter.objects.create(email=email)
            return JsonResponse({'message': 'You have subscribed to newsletter successfully'}, status=201)
        return JsonResponse({'error': 'Email is required'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)
