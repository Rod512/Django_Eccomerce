from django.shortcuts import render,redirect
from .forms import RegistrationForm
from .models import Account
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required



def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            phone_number = form.cleaned_data['phone_number']
            username = email.split('@')[0]
            user = Account.objects.create_user(first_name=first_name,last_name=last_name,email=email,username = username, password=password)
            user.phone_number = phone_number
            user.save()
            messages.success(request, 'registration successfull')
            return redirect('register')

    else:
        form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'account/register.html',context)

def user_login(request):
    if request.method == "POST":
        email =  request.POST["email"]
        password =  request.POST["password"]

        user = authenticate(email = email, password = password)

        if user is not None:
            login(request, user)
            #messages.info(request, "You are successfully loged in")
            return redirect("home")
        else:
            messages.warning(request, "Invalid login credentials")
            return redirect("login")
    else:
        return render(request, 'account/login.html')

@login_required(login_url='login')
def user_logout(request):
    logout(request)
    messages.success(request, "You are successfully loged out")
    return redirect("login")
