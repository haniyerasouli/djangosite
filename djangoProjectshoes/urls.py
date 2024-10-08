"""
URL configuration for djangoProjectshoes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path, include
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.viewhome,name='viewhome'),
    path('admin/', admin.site.urls),
    path('shoe/',include('shoes.urls')),
    path('account/',include('accounts.urls')),
    path('reset_password/',auth_views.PasswordResetView.as_view(),name='reset_password_form'),
    path('reset-password_sent/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset_compelete/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complate'),
    path('cart/',include('carts.urrls'))



]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)