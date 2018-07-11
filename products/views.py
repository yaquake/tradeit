from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import ContactForm
from django.http import HttpResponseRedirect
from .models import Product, Images, Cart
from django.utils import timezone


def home(request):
    return render(request, 'products/home.html', {'title': 'Trade It'})


def details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    image = get_object_or_404(Images, item=product)
    return render(request, 'products/details.html', {'product': product, 'images': image, 'title': product.title})


@login_required(login_url='/accounts/login')
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['desc'] and request.POST['cat'] and request.POST['subcat'] and request.FILES['image1']:
            product = Product()
            product.title = request.POST['title']
            product.body = request.POST['desc']
            product.category = request.POST['cat'].capitalize()
            product.subcategory = request.POST['subcat'].capitalize()
            product.uploader = request.user
            product.pub_date = timezone.datetime.now()
            product.save()

            images = Images(item=product)
            images.image1 = request.FILES['image1']
            # if request.FILES['image2']:
            #     images.image2 = request.FILES['image2']
            # if request.FILES['image3']:
            #     images.image2 = request.FILES['image3']
            # if request.FILES['image4']:
            #     images.image2 = request.FILES['image4']
            # if request.FILES['image5']:
            #     images.image2 = request.FILES['image5']
            images.save()
            return redirect('/products/' + str(product.id))
    else:
        return render(request, 'products/create.html')


def cart(request):
    korz = Cart.objects.filter(master=request.user)
    product = Product()
    return render(request, 'products/cart.html', {'result': korz, 'product': product})


def addtocart(request, product_id):
    if Cart.objects.filter(item__exact=product_id):
        return redirect('/products/' + str(product_id))
    else:
        korz = Cart()
        korz.item = Product(pk=product_id)
        korz.master = request.user
        korz.save()
        return redirect('cart')
