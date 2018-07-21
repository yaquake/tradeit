from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Product, Images, Cart, Category
from django.utils import timezone
from accounts.models import Profile
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def home(request):
    product = Product.objects.all().order_by('-pub_date')[:6]
    return render(request, 'products/home.html', {'title': 'Trade It', 'product': product})


def details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    image = get_object_or_404(Images, item=product)
    category = get_object_or_404(Category, id=product.category_id)
    if request.user.is_authenticated:
        if Cart.objects.filter(item__exact=product_id, master=request.user):
            return render(request, 'products/details.html', {'product': product, 'images': image, 'title': product.title,
                                                         'disabled': 'disabled', 'category': category})
        else:
            return render(request, 'products/details.html', {'product': product, 'images': image, 'title': product.title,
                                                         'category': category})
    else:
        return render(request, 'products/details.html', {'product': product, 'images': image, 'title': product.title,
                                                         'disabled': 'disabled', 'category': category})


@login_required(login_url='/accounts/login')
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['desc'] and request.FILES['image1'] and request.POST['subcategory'] \
                and request.POST['price']:
            product = Product()
            product.title = request.POST['title']
            product.body = request.POST['desc']
            product.uploader = request.user
            product.pub_date = timezone.now()
            product.category = Category.objects.get(name=request.POST['subcategory'])
            product.price = request.POST['price']
            product.save()

            images = Images(item=product)
            images.image1 = request.FILES['image1']
            images.image2 = request.FILES.get('image2', None)
            images.image3 = request.FILES.get('image3', None)
            images.image4 = request.FILES.get('image4', None)
            images.image5 = request.FILES.get('image5', None)
            images.save()
            return redirect('/products/' + str(product.id))
    else:
        cats = Category.objects.filter(parent_id__isnull=True)
        subcats = Category.objects.filter(parent_id__isnull=False)
        return render(request, 'products/create.html', {'title': 'Sell a new product', 'cats': cats, 'subcats': subcats})


def cart(request):
    payment_price = 0
    korz = Cart.objects.filter(master=request.user)
    for kor in korz:
        payment_price += kor.item.price
    title = str(request.user) + '\'s cart'
    return render(request, 'products/cart.html', {'result': korz, 'title': title, 'payment_price': payment_price})


def addtocart(request, product_id):
    if Cart.objects.filter(item=product_id, master=request.user):
        return redirect('/products/' + str(product_id))
    else:

        korz = Cart()
        korz.item = Product(pk=product_id)
        korz.master = request.user
        korz.save()
        user = request.user
        profile = get_object_or_404(Profile, user=user)
        profile.items = Cart.objects.filter(master=request.user).count()
        profile.save()
        return redirect('cart')


def changedetails(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        if request.POST['title']:
            product.title = request.POST['title']
        if request.POST['body']:
            product.body = request.POST['body']
        if request.POST['price']:
            product.price = request.POST['price']
        product.save()
        return redirect('/products/' + str(product_id))

    else:
        return redirect('/products/' + str(product_id))


def delete(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    profile = get_object_or_404(Profile, user=product.uploader)
    items = Cart.objects.filter(master=request.user).count()
    profile.items = items
    profile.save()
    product.delete()
    return redirect('odmen')


def productlist(request):
    if request.method == 'GET':
        category1 = request.GET.get('cat')
        if request.GET.get('subcat') == 'all categories':
            subcat = Category.objects.filter(parent__name__contains=category1)
            product = Product.objects.filter(category__parent__name=category1).order_by('-pub_date')
            paginator2 = Paginator(product, 10)
            page = request.GET.get('page')
            result = paginator2.get_page(page)
            return render(request, "products/list.html", {'subcat': subcat, 'category': category1, 'title': category1,
                                                          'result': result, 'subcategory': 'all categories'})

        else:
            category2 = request.GET.get('subcat')
            product = Product.objects.filter(category__name=category2).order_by('-pub_date')
            paginator2 = Paginator(product, 10)
            page = request.GET.get('page')
            result = paginator2.get_page(page)
            subcat = Category.objects.filter(parent__name__contains=category1)
            return render(request, "products/list.html", {'subcat': subcat, 'category': category1, 'title': category1,
                                                          'subcategory': category2, 'result': result})

    else:
        return render(request, "products/list.html")


def deletefromcart(request, product_id):
    profile = get_object_or_404(Profile, user=request.user)
    item = Cart.objects.get(item_id__exact=product_id, master=request.user)
    item.delete()
    profile.items -= 1
    profile.save()
    return redirect('cart')


def search(request):
    cats = Category.objects.filter(parent_id__isnull=True)
    subcats = Category.objects.filter(parent_id__isnull=False)
    search_query = request.GET.get('search')
    search_list = search_query.split()
    result = Product.objects.filter(title__icontains=search_list[0])
    for s in search_list[1:]:
        result = result | Product.objects.filter(title__icontains=s)
    if request.GET.get('subcategory'):
        result = result.filter(category__name__exact=request.GET.get('subcategory'))
    result_number = result.count()
    paginator = Paginator(result, 10)
    page = request.GET.get('page')
    result = paginator.get_page(page)
    print(result)
    return render(request, 'products/search.html', {'title': "Search results", 'result': result, 'cats': cats,
                                                    'subcats': subcats, 'query': search_query, 'number': result_number})


def buy(request):
    number = request.user.profile.items
    return render(request, 'products/buy.html')