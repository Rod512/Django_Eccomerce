from django.shortcuts import render,redirect
from .forms import RegistrationForm
from .models import Account
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator 
from django.core.mail import EmailMessage




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

            current_site = get_current_site(request)
            mail_subject = messages('please activate your account')
            message = render_to_string('account/account_verification_email.html',{
                'user' : user,
                'domain' : current_site,
                'uid' : urlsafe_base64_encode(force_bytes(user.pk)),
                'token' : default_token_generator.make_token.make_token(user)
            })
            to_mail = email
            send_mail = EmailMessage(mail_subject, message, to=[to_mail])
            send_mail.send()
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
