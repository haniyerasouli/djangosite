from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from carts.carts import Cart
from shoes.models import Shoe
# from shoes.models import Cart

# Create your views here.
#----view cart سبد خرید
def cart(request):
    cart=Cart(request)
    cart_shoes=cart.get_shoes()
    colors = cart.get_cl()
    sizes=cart.get_si()
    # total=cart.get_total()
    # cart_items = Cart.objects.all()
    # total_price = 0
    #
    # for item in cart_shoes:
    #     try:
    #         shoe_price = item.shoe.sale_price if item.shoe.is_sale else item.shoe.price
    #         total_price += shoe_price * item.quantity
    #     except Cart.shoe.RelatedObjectDoesNotExist:
    #         # اگر فیلد shoe وجود نداشت، این آیتم را نادیده بگیرید
    #         continue

    # cart_quantity = len(cart)
    return render(request,'carts/cart.html',{'cart_shoes':cart_shoes, 'colors':colors, 'sizes':sizes})
# def get_cart_total(request):
#     if request.user.is_authenticated:
#         try:
#             cart = get_object_or_404(Cart, user=request.user)
#             total_price = cart.get_total_price()
#             return JsonResponse({'total_price': total_price})
#         except Cart.DoesNotExist:
#             return JsonResponse({'total_price': 0})
#     return JsonResponse({'total_price': 0})

#----view cart_add اضافه کردن به سبد خرید
# def cart_add(request):
#     cart=Cart(request)
#     if request.method == 'POST':
#         shoe_id = request.POST.get('shoe_id')
#         color_id = request.POST.get('color_id')
#         quantity = int(request.POST.get('quantity'))
#
#         inventory = ShoeColorInventory.objects.filter(shoe_id=shoe_id, color_id=color_id).first()
#         if inventory and inventory.quantity >= quantity:
#             # return JsonResponse({'status': 'success', 'message': 'از خریدتون ممنونیم'})
#             shoe_color = request.POST.get('shoe_color')
#             shoe_size = request.POST.get('shoe_size')
#
#             if shoe_id:
#                 shoe_id = int(shoe_id)
#                 shoe = get_object_or_404(Shoe, id=shoe_id)
#                 cart.add(shoe=shoe, color=shoe_color, size=shoe_size)
#                 cart_quantity = cart.__len__()
#                 response = JsonResponse({'qty': cart_quantity})
#                 # response=JsonResponse({'shoe.brand':shoe.brand})
#                 return response
#             else:
#                 # ارسال پاسخ خطا به کاربر
#                 return JsonResponse({'error': 'shoe_id is required'}, status=400)
#         else:
#             return JsonResponse({'status': 'error', 'message': 'متاسفانه تعداد انتخاب شده بیشتر از تعداد موجود است.'})

    # if request.POST.get('action') == 'post':
    #     shoe_id=request.POST.get('shoe_id')
    #     shoe_color = request.POST.get('shoe_color')
    #     shoe_size = request.POST.get('shoe_size')
    #
    #     if shoe_id:
    #         shoe_id=int(shoe_id)
    #         shoe=get_object_or_404(Shoe,id=shoe_id)
    #         cart.add(shoe=shoe, color=shoe_color, size=shoe_size)
    #         cart_quantity=cart.__len__()
    #         response = JsonResponse({'qty': cart_quantity})
    #         # response=JsonResponse({'shoe.brand':shoe.brand})
    #         return response
    #     else:
    #         # ارسال پاسخ خطا به کاربر
    #         return JsonResponse({'error': 'shoe_id is required'}, status=400)


def cart_add(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        shoe_id = request.POST.get('shoe_id')
        shoe_color = request.POST.get('shoe_color')
        shoe_size = request.POST.get('shoe_size')

        if shoe_id:
            shoe_id = int(shoe_id)
            shoe = get_object_or_404(Shoe, id=shoe_id)
            cart.add(shoe=shoe, color=shoe_color, size=shoe_size)
            cart_quantity = cart.__len__()
            response = JsonResponse({'qty': cart_quantity})
            # response=JsonResponse({'shoe.brand':shoe.brand})
            return response
        else:
            # ارسال پاسخ خطا به کاربر
            return JsonResponse({'error': 'shoe_id is required'}, status=400)
# def cart_add(request):
#     cart = Cart(request)
#
#     if request.method == 'POST' and request.POST.get('action') == 'post':
#         quantity = int(request.POST.get('quantity', 1))
#         shoe_id = request.POST.get('shoe_id')
#         shoe_color = request.POST.get('shoe_color')
#         shoe_size = request.POST.get('shoe_size')
#
#         if shoe_id:
#             shoe_id = int(shoe_id)
#             shoe = get_object_or_404(Shoe, id=shoe_id)
#             cart.add(shoe=shoe, color=shoe_color, size=shoe_size, quantity=quantity)
#             cart_quantity = cart.__len__()
#             return JsonResponse({'qty': cart_quantity})
#         else:
#             return JsonResponse({'error': 'shoe_id is required'}, status=400)
#
#     return JsonResponse({'error': 'Invalid request'}, status=400)
    # cart = Cart(request)
    #
    # if request.method == 'POST':
    #     shoe_id = request.POST.get('shoe_id')
    #     shoe_color = request.POST.get('shoe_color')
    #     shoe_size = request.POST.get('shoe_size')
    #     quantity = int(request.POST.get('quantity', 1))  # اگر quantity وجود نداشت، فرض می‌کنیم 1 است
    #
    #     print(f"Received shoe_id: {shoe_id}, color: {shoe_color}, size: {shoe_size}, quantity: {quantity}")
    #
    #     if shoe_id:
    #         shoe_id = int(shoe_id)
    #         shoe = get_object_or_404(Shoe, id=shoe_id)
    #         cart.add(shoe=shoe, quantity=quantity, color=shoe_color, size=shoe_size)
    #         cart_quantity = cart.__len__()
    #         response = JsonResponse({'qty': cart_quantity})
    #         return response
    #     else:
    #         # ارسال پاسخ خطا به کاربر
    #         return JsonResponse({'error': 'shoe_id is required'}, status=400)
    # else:
    #     # ارسال پاسخ خطا به کاربر اگر درخواست POST نباشد
    #     return JsonResponse({'error': 'Invalid request method'}, status=405)
def cart_delete(request):
    cart = Cart(request)
    #
    # if request.POST.get('action') == 'post':
    #     shoe_id = request.POST.get('shoe_id')
    #     cart.delete(shoe=shoe_id)
    #     total = cart.get_total()
    #
    #     response = JsonResponse({'success': True, 'shoe_id': shoe_id, 'total':total})
    #     return response
    if request.POST.get('action') == 'post':
        shoe_id = request.POST.get('shoe_id')
        cart.delete(shoe=shoe_id)
        # total = cart.get_total()  # به روزرسانی مجموع پس از حذف محصول

        response = JsonResponse({'success': True, 'shoe_id': shoe_id})
        return response


def update_cart_view(request):
    if request.method == 'POST':
        cart_items = request.session.get('cart', {})
        total_price = 0
        for shoe_id, item in cart_items.items():
            shoe = Shoe.objects.get(id=shoe_id)
            quantity = item['quantity']
            if shoe.is_sale:
                total_price += shoe.sale_price * quantity
            else:
                total_price += shoe.price * quantity
        return JsonResponse({'total_price': total_price})

# def clean_cart_items():
#     invalid_items = Cart.objects.filter(shoe__isnull=True)
#     for item in invalid_items:
#         # اینجا می‌توانید اشیا نامعتبر را حذف یا اصلاح کنید
#         item.delete()
#
#     # اجرای اسکریپت
# clean_cart_items()