import random
from django.shortcuts import render, redirect
from .models import Account, Employee, Company
from company.models import CompanyProfile
from employee.models import ProfileEdit
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from .models import UserOTP



# Create your views here.


def admin_create(request):
    
    
    if request.method == "POST":
        username = request.POST.get("username")
        fname = request.POST.get("firstname")
        email = request.POST.get("email")
        role = request.POST.get("role")
        pasw1 = request.POST.get("password1")
        pasw2 = request.POST.get("password2")

        user = Account.objects.filter(username=username)
        if not user:
            if pasw1 == pasw2:
                Account.objects.create_user(
                    username=username,
                    first_name=fname,
                    role=role,
                    email=email,
                    password=pasw1,
                )
                messages.success(request, "Account create Successfuly")
                return redirect("user_login")
            else:
                messages.error(request, "Password does not match")
        else:
            messages.error(request, "Username already exits ")

    return render(request, "accounts/create_user.html")


def employee_create(request):
    if request.method == "POST":
        username = request.POST.get("username")
        fname = request.POST.get("firstname")
        lname = request.POST.get("lastname")
        email = request.POST.get("email")
        pasw1 = request.POST.get("password1")
        pasw2 = request.POST.get("password2")

        user = Employee.objects.filter(username=username)
        if not user:
            if pasw1 == pasw2:
                Employee.objects.create_user(
                    username=username,
                    first_name=fname,
                    last_name=lname,
                    email=email,
                    password=pasw1,
                    is_active =True
                )
                messages.success(request, "Account create Successfuly")
                return redirect("user_login")
            else:
                messages.error(request, "Password does not match")
        else:
            messages.error(request, "Username already exits ")

    return render(request, "accounts/create_user.html")


def company_create(request):
    if request.method == "POST":
        username = request.POST.get("username")
        fname = request.POST.get("firstname")
        email = request.POST.get("email")
        role = request.POST.get("role")
        pasw1 = request.POST.get("password1")
        pasw2 = request.POST.get("password2")

        user = Company.objects.filter(username=username).first()
        if not user:
            if pasw1 == pasw2:
                Company.objects.create_user(
                    username=username,
                    first_name=fname,
                    role=role,
                    email=email,
                    password=pasw1,
                )
                messages.success(request, "Account create Successfuly")
                return redirect("user_login")
            else:
                messages.error(request, "Password does not match")
        else:
            messages.error(request, "Username already exits ")

    return render(request, "accounts/create_user.html")


def user_login(request):
    
    user =request.user
    
   
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        

        user = authenticate(username=username, password=password)
        
            
        if user:
            login(request, user)
            messages.success(request, "Login")
            
            if request.user.role == "USER":
                employee = ProfileEdit.objects.filter(rel_profile = user)
                if employee:
                    return redirect("employee_home")
                else:
                    return redirect("employee_profile_edit")
                
            elif request.user.role == "COMPANY":
                company = CompanyProfile.objects.filter(rel_comp = user)
                if user.is_active == True:
                    if company:                
                        return redirect("company_home")
                    else:
                        return redirect("company_profile_edit")
                else:
                    
                    messages.error(request, "Pleace")
                
            elif request.user.role == "ADMIN":
                return redirect("admin_homepage")
            
        elif request.user.is_active == "False":
            messages.error(request, "Pleace Waiting for Permission")
        else:

            if user :
                print('hellloooooo')
                messages.error(request, "Pleace")
            else:
                messages.error(request, "invalid username or password")

    return render(request, "accounts/index.html")


def user_logout(request):
    logout(request)
    return redirect(
        "user_login",
    )


def employee_forgot_password(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        
        users = Account.objects.filter(username = username).first()
        
        if users:
            otp = random.randint(1000,9999)
            sub = 'Password reset'
            message = f'Here is your One time password(OTP)-{otp}'
            from_email = 'benisondevis.py@gmail.com'
            to_email = [users.email]
            
            user_otps = UserOTP.objects.filter(user = users)
            if user_otps :
                user_otp = user_otps.first()
                user_otp.otp = otp
                user_otp.save()
            else :
                UserOTP.objects.create(
                    otp = otp,
                    user = users
                )
            
            send_mail(
                subject = sub,
                message = message,
                from_email = from_email,
                recipient_list = to_email,
                fail_silently = False
            )
            messages.success(request,'Successfuly OTP send to your registered Email Address')
            return redirect('verify_otp',users.id)
        else:
            messages.error(request,"username does't exit")        
    return render(request,'accounts/empl_forgot.html')


def verify_otp(request,id):
    user = Account.objects.get(id = id)
    if request.method =='POST':
        submitted_otp = request.POST.get('otp')
        user_otp = UserOTP.objects.filter(user = user).first()
        
        if submitted_otp == user_otp.otp:
            messages.success(request,'OTP verified')
            return redirect('password_reset',user.id)
        messages.error(request,'Invalid otp')
    return render(request,'accounts/verify_otp.html')


def password_reset(request,id):
    user = Account.objects.get(id = id)
    if request.method == 'POST':
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 == password2:
            user.set_password(password2)
            user.save()
            messages.success(request,'password changed successfuly')
            return redirect('user_login')
        messages.error(request,'password does not match')
    return render(request,'accounts/reset.html')
