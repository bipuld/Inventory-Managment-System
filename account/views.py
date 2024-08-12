from django.shortcuts import render,redirect
from django.contrib import messages
from account.models import UserInfo
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, logout,login as auth_login

# Create your views here.
def login(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        print(email,password)
                # Handle login form submission
        try:
            # Find the user profile based on the email
            print("Finding user profile")
            user_profile = UserInfo.objects.get(email=email)
            user = user_profile.user
            print(user, user_profile)

            # Check if the password is correct
            if user.check_password(password):
                auth_login(request, user)
                print("User logged in")
                return redirect('home')  
            else:
                print("Incorrect password")
                messages.error(request, "Incorrect password.")
        except UserInfo.DoesNotExist:
            print("User with this email does not exist")
            messages.error(request, "User with this email does not exist.")
    return render(request,'account/login.html')

def logout_user(request):
    logout(request)
    messages.success(request, f"Thank You For Using Us")
    return redirect('login')

