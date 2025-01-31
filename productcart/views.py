import requests
import json
import uuid


from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages


from decouple import config
import yagmail

from base.views import G
from .helpers import generate_short_id
from .utils import *
from .models import *
from .cart import Cart
from .forms import CheckoutForm


email_address = config("EMAIL_HOST_USER")
email_password = config("EMAIL_HOST_PASSWORD")
receiver = config("RECEIVER_EMAIL")

yag = yagmail.SMTP(f'{email_address}', f'{email_password}')

# Create your views here.


def checkout(request):
    itemtotal = 0
    subtotal = 0
    prod = Cart(request)
    for item in prod:
        subtotal += item['price'] * item['qnt']


    itemtotal = subtotal  
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            checkedout = form.save(commit=False)
            checkedout.payment_method = form.cleaned_data['payment_method']
            checkedout.total = itemtotal
            checkedout.itm_paid = False
            checkedout.status = 'New'
            checkedout.total = itemtotal

            checkedout.save()


            request.session['current_order_id'] = checkedout.id
            request.session.modified = True


            # send email to customer
            to = [f'{receiver}', f'{checkedout.email}']
            subject = 'New Order Received'
            body = f'New order from {checkedout.firstname} {checkedout.lastname}\n' f'Products: {get_order_details(request)}\n',
                    
            yag.send(to = to, subject = subject, contents = body)

            
            if form.cleaned_data['save_info']:
                saved_data = {
                    f.name: form.cleaned_data[f.name] for f in form if f.name not in ['save_info', 'terms', 'payment_method']
                }
                request.session['checkout_info'] = saved_data
            return redirect('productcart:paidorder')
        else:
            # Form is invalid: fall through and re-render template
            messages.error(request, 'form not submitted')
    else:
        initial = request.session.get('checkout_info', {})
        form = CheckoutForm(initial=initial)
    

    return render(request, 'utils/checkout.html', {'prod':prod, 'itemtotal':itemtotal, 'form':form})



def paidorder(request):

    order_id = request.session.get('current_order_id')
    if not order_id:
        return redirect('productcart:checkout')
    
    try:
        order = Checkout.objects.get(pk=order_id)
    except Checkout.DoesNotExist:
        return redirect('productcart:checkout')
    
    ref_num = str(uuid.uuid4())
    order_num = generate_short_id()

    if order.payment_method == 'card':
        api_key= config('PAYSTACK_API_KEY')
        curl= config('PAYSTACK_CURL_URL')
        # cburl = 'http://3.89.180.169/thankyou'
        cburl = config('PAYSTACK_CBURL')

        totalprice = int(order.total)*100

        headers= {'Authorization': f'Bearer {api_key}'}
        data = {'reference':ref_num, 'order_number':order_num, 'amount': totalprice, 'callback_url': cburl, 'email':order.email, 'currency':'NGN'}


        try:
            r = requests.post(curl, headers=headers, json=data)
        except Exception:
            messages.error(request, 'Please refresh and try again, issue being resolved')
        else:
            transback = json.loads(r.text)
            rd_url = transback['data']['authorization_url']


            # take record of transaction made
            save_order_details(order, ref_num, order_num, request)

            return redirect(rd_url)
        return redirect('productcart:checkout')
    
    elif order.payment_method == 'payment_on_delivery':

        save_order_details(order, ref_num, order_num, request)

        return redirect('productcart:nocardthankyou')

    messages.error(request, 'Invalid payment method')
    return redirect('productcart:checkout')



def thankyou(request):
    cart = Cart(request)
    for item in cart:
        prod = int(item['product']['id'])
    items = ProductCart.objects.filter(product=prod, item_paid=False)

    for item in items:
        item.item_paid = True
        item.save()

    clear_cart(request)
    return render(request, 'payment/cardthankyou.html')

def nocardthankyou(request):
    clear_cart(request)
    return render(request, 'payment/ondeliverythankyou.html')


