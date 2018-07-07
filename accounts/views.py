from django.shortcuts import render, redirect, get_object_or_404
import os.path
from django.contrib.auth.models import User
from accounts.models import Profile
from django.contrib import auth


def signup(request):
    parent_directory = os.path.split(os.path.dirname((__file__)))[0]
    f = open(parent_directory + '/static/countries.txt', 'r')
    countries = [line[:-1] for line in f]
    f.close()
    age = [age for age in range(18, 101)]

    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            if 8 <= len(request.POST['password1']) <= 20:
                # try:
                #     user = User.objects.get(username=request.POST['username'])
                #     return render(request, 'accounts/signup.html',
                #                   {'countries': countries, 'ages': age, 'title': 'Sign up',
                #                    'error': 'Username has already been taken'})
                #
                # except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'], email=request.POST['email'],
                                                password=request.POST['password1'], first_name=request.POST['firstname'],
                                                last_name=request.POST['lastname'])
                user.save()
                profile = Profile(user=user, age=request.POST['age'], address=request.POST['address'],
                                  address2=request.POST['address2'],city=request.POST['city'],
                                  country=request.POST['country'], postcode=request.POST['postcode'])
                profile.save()
                auth.login(request, user)
                return redirect('home')

            else:
                return render(request, 'accounts/signup.html', {'countries': countries, 'ages': age, 'title': 'Sign up',
                                                                'error': 'Password must be between 8 and 20 symbols'})

        else:
            return render(request, 'accounts/signup.html', {'countries': countries, 'ages': age, 'title': 'Sign up',
                                                            'error': 'Passwords are different'})

    else:
        return render(request, 'accounts/signup.html', {'countries': countries, 'ages': age, 'title': 'Sign up'})


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    else:
        return render(request, 'accounts/signup.html')


def login(request):
    if request.method == 'POST':
        try:
            user1 = User.objects.get(email__exact=request.POST['email'])
            user = auth.authenticate(username=user1.username, password=request.POST['password'])
            # if user is not None:
            auth.login(request, user)
            return redirect('home')
            # else:
            #     return render(request, 'accounts/login.html', {'error': 'You have entered invalid data. '
            #                                                             'Try to log in again. If you are not registered,'
            #                                                             ' please register'})
        except User.DoesNotExist:
            return render(request, 'accounts/login.html', {'error': 'You have entered invalid data. '
                                                                    'Try to log in again. If you are not registered,'
                                                                    ' please register'})
    else:
        return redirect('home')

