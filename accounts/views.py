from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserLoginForm, UserChangePasswordForm
from django.contrib.auth.decorators import login_required


#___  viewregister برای عضویت در سایت
def ViewRegister(request):
    if request.method=='POST':
        form_register=UserRegisterForm(request.POST)
        if form_register.is_valid():
            data=form_register.cleaned_data
            User.objects.create_user(username=data['user_name'],
                                     email=data['email'],
                                     first_name=data['first_name'],
                                     last_name=data['last_name'],
                                     password=data['password_2'],
                                     )

            return redirect('viewShoe')
    else:
        form_register=UserRegisterForm()
    return render(request,'aaccounts/register_page.html',{'form_register':form_register})


def ViewLogin(request):
    if request.method=='POST':
        form_login=UserLoginForm(request.POST)
        if form_login.is_valid():
            data=form_login.cleaned_data
            user=authenticate(request,username=data['user_name'],password=data['password'])
            if user:
                login(request,user)
                # return HttpResponse('وارد شدی')
                return redirect('viewShoe')
    else:
        form_login=UserLoginForm()
    return render(request,'aaccounts/login_page.html',{'form_login':form_login})

def ViewLogout(request):
    logout(request)
    return HttpResponse('خارج شدی')

#___view change password برای تغییر پسورد

@login_required
def ViewChangePassword(request):
    if request.method == 'POST':
        user=request.user
        form_change = UserChangePasswordForm(request.POST)
        if form_change.is_valid():
            data=form_change.cleaned_data
            old_password=data['old_password']
            new_password1=data['new_password1']
            new_password2 = data['new_password2']
            if old_password!=user.password:
                return HttpResponse('این پسورد قبلا ثبت شده:((')
            elif new_password1!=new_password2:
                return HttpResponse('پسوردها با هم مچ نیست:(')
            elif len(new_password2)<8:
                return HttpResponse('پسوردت خیلی کوتاهه:(')
            else:
                user.set_password(new_password1)
                login(request, user)
                user.save()
                return HttpResponse('با موفقیت تغییر کرد')
    else:
        form_change=UserChangePasswordForm()
    return render(request,'aaccounts/change_password.html',{'form_change':form_change})
