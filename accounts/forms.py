from django import forms
from django.contrib.auth.models import User
from django.http import HttpResponse



#فرم ثبت نام
class UserRegisterForm(forms.Form):

    user_name=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'لطفا نام کاربری رو وارد کنید'}))
    email = forms.CharField(max_length=20, widget=forms.EmailInput(attrs={'placeholder':'اینجوری: test@gmail.com'}))
    first_name=forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder':'اسم خودتون رو وارد کنید'}))
    last_name=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'فامیلی خودتون رو وارد کنید'}))
    password_1=forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={'placeholder':'پسورد خودتون رو وارد کنید.'}))
    password_2 = forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={'placeholder':'دوباره پسورد خودتون رو وارد کنید.'}))



# اعتبار سنجی نام کاربری وارد شده
    def clean_user_name(self):
        user=self.cleaned_data['user_name']
        if User.objects.filter(username=user).exists():
            raise forms.ValidationError('این نام کاربری قبلا ثبت شده :(')
        else:
            return user

    # اعتبار سنجی ایمیل وارد شده
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('این ایمیل قبلا ثبت شده :(')
        return email

    # اعتبار سنجی پسورد وارد شده
    def clean_password_2(self):
        password1=self.cleaned_data['password_1']
        password2=self.cleaned_data['password_2']
        if password1!=password2:
            raise forms.ValidationError('!پسوردهای وارد شده متفاوتند')
        elif len(password2)<8:
            raise forms.ValidationError(':( پسورد وارد شده خییلی کوتاهه ')
        elif not any( i.isupper() for i in password2):
            raise forms.ValidationError(':( پسورد باید حداقل شامل یک حرف بزرگ باشه ')
        return password2


#___فرم ورود کاربر
class UserLoginForm(forms.Form):
    user_name=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'لطفا نام کاربری رو وارد کنید'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'لطفا پسورد خودتون رو وارد کنید.'}))

#----فرم تغییر پسورد
class UserChangePasswordForm(forms.Form):
    old_password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':' پسورد قبلی را وارد کنید.'}))
    new_password1=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':' پسورد جدید خودتون رو وارد کنید.'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': ' .دوباره وارد کنید'}))