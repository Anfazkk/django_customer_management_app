from django.shortcuts import render, reverse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http.response import HttpResponseRedirect
from django.contrib.auth.models import User

from users.forms import UserForm, Customer


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                url = f'/{user.pk}'
                return HttpResponseRedirect(url)
            
        context = {
            'title' : 'Login',
            'error' : True,
            'message' : 'Invalid username or password',
        }
        return render(request, 'users/login.html', context=context)
    
    else:
        context = {
            'title' : 'Login',
        }
        return render(request, 'users/login.html', context=context)


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('web:index'))


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)

            user = User.objects.create_user(
                username = instance.full_name,
                password = instance.password
            )

            customer = Customer.objects.create(
                number = user.id,
                full_name = user.username,
                phone = instance.phone,
                email = instance.email,
                address = instance.address,
                date_of_birth = instance.date_of_birth,
                user = user
            )

            user = authenticate(request, username = instance.full_name, password = instance.password)
            auth_login(request, user)

            url = f'/{customer.number}'
            return HttpResponseRedirect(url)
        
        context = {
            'title' : 'Signup',
            'error' : True,
        }
        return render(request, 'users/signup.html', context=context)
    
    else:
        form = UserForm()
        context = {
            'title' : 'Signup',
            'form' : form,
            'error' : True,
            'message' : 'Username already exists'
        }
        return render(request, 'users/signup.html', context=context)


    