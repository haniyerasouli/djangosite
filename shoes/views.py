from django.shortcuts import render

# Create your views here.
from pkgutil import get_data

import django.urls
# from PIL.DdsImagePlugin import item
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from shoes.models import Shoe, ShoeColorInventory, ShoeSizeInventory, ShoeImage


# Create your views here.
#viewshoe برای نمایش محصولات
def viewShoe(request):
    shoe_record=Shoe.objects.all()
    return render(request,'shoes/index.html',{'shoe_record':shoe_record})

#برای نمایش جزییات هر یک از محصولات
def viewShoedetail(request,s,pk):
    shoe=get_object_or_404(Shoe,slug=s,id=pk)
    image = ShoeImage.objects.filter(shoe=shoe)


    return render(request,'shoes/shoe_detail.html',{'shoe':shoe, 'images':image})

# @csrf_exempt
# def check_inventory(request):
#     if request.method == 'POST':
#         shoe_id = request.POST.get('shoe_id')
#         color_id = request.POST.get('color_id')
#         size_id = request.POST.get('size_id')
#         quantity = int(request.POST.get('quantity'))
#
#         try:
#             inventory = ShoeColorSizeInventory.objects.get(shoe_id=shoe_id, color_id=color_id, size_id=size_id)
#             if inventory.quantity >= quantity:
#                 return JsonResponse({'status': 'success', 'message': 'موجودی کافی است.'})
#             else:
#                 return JsonResponse({'status': 'error', 'message': 'موجودی کافی نیست.'})
#         except ShoeColorSizeInventory.DoesNotExist:
#             return JsonResponse({'status': 'error', 'message': 'موجودی یافت نشد.'})
#
#     return JsonResponse({'status': 'error', 'message': 'درخواست نامعتبر است.'})

@csrf_exempt
def check_inventory(request):
    if request.method == 'POST':
        shoe_id = request.POST.get('shoe_id')
        color_id = request.POST.get('color_id')
        size_id = request.POST.get('size_id')
        quantity = int(request.POST.get('quantity'))

        try:
            color_inventory = ShoeColorInventory.objects.get(shoe_id=shoe_id, color_id=color_id)
            size_inventory = ShoeSizeInventory.objects.get(shoe_id=shoe_id, size_id=size_id)

            if color_inventory.quantity >= quantity and size_inventory.quantity >= quantity:
                return JsonResponse({'status': 'success', 'message': 'با موفقیت وارد سبد خرید شد:)'})
            else:
                return JsonResponse({'status': 'error', 'message': 'موجودی کافی نیست.'})
        except ShoeColorInventory.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'از این رنگ نداریم ):'})
        except ShoeSizeInventory.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'از این سایز نداریم ):'})

    return JsonResponse({'status': 'error', 'message': 'درخواست نامعتبر است.'})