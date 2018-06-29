from django.shortcuts import render
import os.path


def signup(request):
    parent_directory = os.path.split(os.path.dirname((__file__)))[0]
    f = open(parent_directory + '/static/countries.txt', 'r')
    countries = [line[:-1] for line in f]
    f.close()
    age = [age for age in range(18, 101)]
    return render(request, 'accounts/signup.html', {'countries': countries, 'ages': age, 'title': 'Sign up'})
