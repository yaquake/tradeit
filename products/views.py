from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import ContactForm
from django.http import HttpResponseRedirect
from .models import Product, Images, Cart
from django.utils import timezone
from accounts.models import Profile


def home(request):
    return render(request, 'products/home.html', {'title': 'Trade It'})


def admindetails(request, product_id):
    return render(request, 'accounts/admindetails')


def details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    image = get_object_or_404(Images, item=product)
    if Cart.objects.filter(item__exact=product_id, master=request.user):
        return render(request, 'products/details.html', {'product': product, 'images': image, 'title': product.title,
                                                         'disabled': 'disabled'})
    else:
        return render(request, 'products/details.html', {'product': product, 'images': image, 'title': product.title})


@login_required(login_url='/accounts/login')
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['desc'] and request.POST['cat'] and request.POST['subcat'] \
                and request.FILES['image1']:
            product = Product()
            product.title = request.POST['title']
            product.body = request.POST['desc']
            # product.category = request.POST['cat'].capitalize()
            # product.subcategory = request.POST['subcat'].capitalize()
            product.uploader = request.user
            product.pub_date = timezone.datetime.now()
            product.save()

            images = Images(item=product)
            images.image1 = request.FILES['image1']
            images.image2 = request.FILES['image2']
            images.image2 = request.FILES['image3']
            images.image2 = request.FILES['image4']
            images.image2 = request.FILES['image5']
            images.save()
            return redirect('/products/' + str(product.id))
    else:
        return render(request, 'products/create.html')


def cart(request):
    korz = Cart.objects.filter(master=request.user)
    # cart_no = korz.count()
    # user = request.user
    # profile = Profile(user=user)
    # profile.items = cart_no
    # profile.save()
    # product = Product()
    title = str(request.user) + '\'s cart'
    return render(request, 'products/cart.html', {'result': korz, 'title': title})


def addtocart(request, product_id):
    if Cart.objects.filter(item=product_id, master=request.user):
        return redirect('/products/' + str(product_id))
        # return render(request, 'products/details.html', {'error': 'Error'})
    else:

        korz = Cart()
        korz.item = Product(pk=product_id)
        korz.master = request.user
        korz.save()
        user = request.user
        profile = get_object_or_404(Profile, user=user)
        print(profile)
        profile.items += 1
        profile.save()
        return redirect('cart')


def changedetails(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        product.title = request.POST['title']
        product.body = request.POST['body']
        product.save()
        return redirect('/products/' + str(product_id))

    else:
        return redirect('/products/' + str(product_id))
