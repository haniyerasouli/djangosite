from django.urls import path, re_path

from .import views

# تععین مسیر url هر یک از ویو های اپ shoes
urlpatterns=[

              path('shoe/',views.viewShoe,name='viewShoe'),

              # path('shoe/<slug:s>/<int:shoe_id>/',views.viewShoedetail,name='viewShoedetail'),
              path('shoe/<slug:s>/<int:pk>/', views.viewShoedetail,name='viewShoedetail'),
              path('check_inventory/', views.check_inventory, name='check_inventory'),




    ]