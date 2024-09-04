from django.urls import path
from .import views

urlpatterns=[
    path('account/',views.ViewRegister,name='ViewRegister'),
    path('login/',views.ViewLogin,name='ViewLogin'),
    path('logout/',views.ViewLogout,name='ViewLogout'),
    path('change/',views.ViewChangePassword,name='ViewChangePassword'),
]