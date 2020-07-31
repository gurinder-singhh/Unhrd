from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import UserRegistrationForm,UserLoginForm
from django.contrib.auth import logout ,login ,authenticate
from django.contrib import messages
import re
from django.core.mail import EmailMessage
from django.conf import settings


#User Login View
def login_view(request):

    if request.method == 'POST':
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect("home:userhomepage")
        else:
            messages.error(request,'Please check! username or password is  incorrect')


    else:
        form = UserLoginForm()
    return render(request,'userAuth/login.html',{'form': form})

#User Registration View
def register_view(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        data = request.POST.dict()
        if data.get('confirm_password') == data.get('password'):
            if re.match(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$', data.get('password')):
                if form.is_valid():
                    form.save()
                    username = data.get('username')
                    email = data.get('email')
                    messages.info(request,f"Hello {username} a mail has been set to {email} Please check your mailbox and verify your email address" )
                    return redirect("auth:verifyemail")

                else:
                    context = {'form':form}
                    return render (request,"userAuth/register.html",context)
            else:
                messages.error(request,"Your Password shoud contain one lower case letter, one uppercase letter, one special symbol and at least one number.")
                return render(request,"userAuth/register.html",{'form':form})
        else:
            messages.error(request,"Those passwords didn't match. Try again.")
            return render(request,"userAuth/register.html",{'form':form})


    form = UserRegistrationForm()
    context = {'form':form}
    return render(request,"userAuth/register.html",context)


#User Logout View
def logout_view(request):
    logout(request)
    print("Logged out")
    return redirect("auth:login")

#User Email Verification View
def verifyemail(request,**kwargs):

    return render(request,'userAuth/verifyemail.html')




