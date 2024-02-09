from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import render, redirect

from portal.models import Customer


def home_view(request):
    return render(request, 'home.html')


def logout(request):
    auth.logout(request)
    return redirect('home')


def login(request):
    print(request.method)
    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials!")

    return render(request, 'portal/login_form.html')


class CustomerCreateView(CreateView):
    model = Customer
    template_name = 'portal/customer_form.html'
    fields = ('first_name', 'last_name', 'dob', 'phone_no', 'email')


class CustomerUpdateView(UpdateView):
    model = Customer
    template_name = 'portal/customer_update_form.html'
    fields = ('first_name', 'last_name', 'dob', 'phone_no', 'email')