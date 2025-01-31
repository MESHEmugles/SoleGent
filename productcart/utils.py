from decouple import config
import yagmail


from .cart import Cart
from .models import Paidorder, Ship
from commerce.models import Product


email_address = config("EMAIL_HOST_USER")
email_password = config("EMAIL_HOST_PASSWORD")
receiver = config("RECEIVER_EMAIL")

yag = yagmail.SMTP(f'{email_address}', f'{email_password}')



def get_order_details(request):
    prod = Cart(request)
    order_details = ''
    for item in prod:
        order_details += f'{item["product"]['name']} - {item["qnt"]} - {item["total_price"]}\n'
    return order_details


def clear_cart(request):
    request.session['cartkey'] = {}
    request.session.modified = True
    return True

def save_order_details(order, ref_num, order_num, request):
    prod_bought = Cart(request)
    productname = ', '.join([item['product']['name'] for item in prod_bought])

    for item in prod_bought:
        proditem = Product.objects.get(name=item['product']['name'])

    shipping_method = ''

    paidorder = Paidorder()
    paidorder.product = proditem
    paidorder.total = order.total
    paidorder.cart_no = order_num
    paidorder.payment_code = ref_num
    paidorder.payment_method = order.payment_method
    if order.payment_method == 'card':
        paidorder.paid_item =True
        shipping_method = 'Already Paid'
    else:
        paidorder.paid_item = False
        shipping_method = 'Payment will be done on delivery'

    paidorder.firstname = order.firstname
    paidorder.save()


    ship =Ship()
    ship.product = proditem
    ship.things_bought = productname
    ship.total = order.total
    ship.ordr_no = order_num
    ship.payment_method = order.payment_method
    ship.address = order.address
    ship.state = order.state
    if order.payment_method == 'card':
        ship.itm_paid =True
        shipping_method = 'Already Paid'
    else:
        ship.itm_paid = False
        shipping_method = 'Payment will be done on delivery'
    ship.firstname = order.firstname
    ship.save()


    # send email to customer
    to = [f'{receiver}', f'{order.email}']
    subject = 'New Transaction alert !'
    body = f'Admin, a client {order.firstname} {order.lastname}, with the phone number {order.phone_number} has just completed a transaction. \n kindly follow up on his transaction. {shipping_method}',
            
    yag.send(to = to, subject = subject, contents = body)



