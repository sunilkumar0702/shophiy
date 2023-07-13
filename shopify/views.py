from rest_framework import viewsets
from .serializers import RegistrationSerializer
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from .models import *

from django.contrib.auth.hashers import make_password, check_password


def index(request):
    if request.method == 'POST':
        product_id = request.POST.get('cartid')
        remove = request.POST.get('remove')
        print(remove)
        print("product_id ============ ", product_id)

        cart = request.session.get('cart')
        print("cart ============ ", cart)
        if cart:
            quantity = cart.get(product_id)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product_id)
                    else:
                        cart[product_id] = quantity - 1
                else:
                    cart[product_id] = quantity + 1
            else:
                cart[product_id] = 1
        else:
            cart = {}
            cart[product_id] = 1
        request.session['cart'] = cart
        print("request.session['cart'] ============ ", request.session['cart'])

    category = Category.objects.all()
    products = request.GET.get('category_id')

    cate = request.GET.get('category_id')
    if cate:
        products = Product.objects.filter(category=cate)
    else:
        products = Product.objects.all()
    context = {
        'category': category,
        'product': products
    }

    return render(request, 'index.html', context=context)


def sign_up(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        mobile = request.POST.get('mobile')
        gender = request.POST.get('gender')

        reg_obj = Registrations(
            first_name=fname,
            last_name=lname,
            email=email,
            password=make_password(password),
            mobile=mobile,
            gender=gender
        )
        reg_obj.save()

        return HttpResponse("Registration successful")


def login(request):
    if request.method == 'POST':
        email = request.POST.get('emailid')
        password = request.POST.get('password')

        try:
            email_id = Registrations.objects.get(email=email)
            if email_id:
                if check_password(password, email_id.password):
                    request.session['name'] = email_id.first_name
                    request.session['customer_id'] = email_id.id
                    return redirect('home')
                else:
                    return HttpResponse("wrong password")
        except:
            return HttpResponse("wrong email")


def logout(request):
    request.session.clear()
    return redirect('home')


def cart_dtls(request):
    ids = list(request.session.get('cart').keys())
    cart_info = Product.objects.filter(id__in=ids)

    context = {
        'cart_dtls': cart_info
    }

    return render(request, 'cart.html', context=context)


def checkout(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        mobile = request.POST.get('mobile')
        customer_id = request.session.get('customer_id')
        cart = request.session.get('cart')
        product = Product.objects.filter(id__in=list(cart.keys()))
        if not customer_id:
            return HttpResponse("Please Login")
        for pro in product:
            ord_save = Order(
                address=address,
                mobile=mobile,
                quantity=cart.get(str(pro.id)),
                customer=Registrations(id=customer_id),
                price=pro.pro_price,
                product=pro
            )
            ord_save.save()
        return redirect('order')


def order_dtls(request):
    customer_id = request.session.get('customer_id')
    ord_dtls = Order.objects.filter(customer=customer_id)

    tp = 0
    for i in ord_dtls:
        tp = tp + (i.price * i.quantity)
    context = {
        'order': ord_dtls,
        'tp': tp
    }
    return render(request, 'order.html', context=context)


class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registrations.objects.all()
    serializer_class = RegistrationSerializer
