from django.urls import path

from . import views

urlpatterns=[
    path('',views.cart,name='cart'),
    path('add/',views.cart_add,name='cart_add'),
    path('delete/',views.cart_delete,name='cart_delete'),
    path('update/',views.update_cart_view,name='update_cart'),
    # path('get_cart_total/', views.get_cart_total, name='get_cart_total'),

]