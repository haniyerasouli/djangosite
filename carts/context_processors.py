from .carts import Cart

#----اضافه کردن سیشن
def cart(request):
    return {'cart':Cart(request)}