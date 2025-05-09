from django.shortcuts import render, redirect
from django.contrib.auth import login,logout, authenticate
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
import re


User = get_user_model()

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful")
            if user.is_superuser:
                return redirect('dashboard')  
            else:
                return redirect('home') 
        else:
            messages.error(request, "Your email or password is incorrect")

    return render(request, 'login.html')



def logout_view(request):
      logout(request)  
      messages.success(request, "Logout successful")
      return redirect('login') 



def register_view(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if not all([full_name, email, phone, password, confirm_password]):
            messages.error(request, "All fields are required")
            return render(request, 'register.html')

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return render(request, 'register.html')
        
        if not re.match(r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', password):
            messages.error(request, "Password must be at least 8 characters long and include at least one uppercase letter, one number, and one special character.")
            return render(request, 'register.html')
        

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered")
            return render(request, 'register.html')
        
        if User.objects.filter(phone=phone).exists():
            messages.error(request, "Phone Number is already registered")
            return render(request, 'register.html')

        # Split full name
        name_parts = full_name.strip().split()
        first_name = name_parts[0]
        last_name = " ".join(name_parts[1:]) if len(name_parts) > 1 else ""

        User.objects.create(
            email=email,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            password=make_password(password),
        )

        messages.success(request, "Registration successful. Please log in.")
        return redirect('login')

    # Always return a response here for GET request
    return render(request, 'register.html')