from django.shortcuts import render
import os.path
# Create your views here.


def about(request):
    return render(request, 'info/about.html', {'title': 'About'})


def contact(request):
    return render(request, 'info/contact.html', {'title': 'Contact us'})


def payment(request):
    parent_directory = os.path.split(os.path.dirname(__file__))[0]
    f = open(parent_directory + '/static/payment.txt', 'r')
    payfile = f.read()
    f.close()
    return render(request, 'info/payment.html', {'payfile': payfile, 'title': 'Payment'})

