from django.conf import settings

from shoes.models import Shoe


#سبد خرید و ارتباط با سیشن-----
class Cart:
    def __init__(self,request):
        self.session=request.session

        cart=self.session.get('cart')
        if not cart:
            cart=self.session['cart']={}
        self.cart=cart
        #----اضافه کردن کفش به سبد خرید

    # def add(self, shoe, quantity=1, update_quantity=False, color=None, size=None):
    #     shoe_id = str(shoe.id)
    #     if shoe_id not in self.cart:
    #         self.cart[shoe_id] = {'quantity': 0, 'price': str(shoe.price), 'color': color, 'size': size}
    #     if update_quantity:
    #         self.cart[shoe_id]['quantity'] = quantity
    #     else:
    #         self.cart[shoe_id]['quantity'] += quantity
    #     self.save()
    #
    # def save(self):
    #     self.session[settings.CART_SESSION_ID] = self.cart
    #     self.session.modified = True


    def add(self, shoe, color, size):
        shoe_id=str(shoe.id)
        shoe_color = str(color)
        shoe_size=str(size)

        # shoe_id = str(shoe.id)
        if shoe_id in self.cart:
            self.cart[shoe_id]['quantity'] += 1
        else:
        #     self.cart[shoe_id] = shoe_color
        # self.session.modified=True
            self.cart[shoe_id] = {'quantity': 1, 'color': shoe_color, 'size':shoe_size}
            self.session.modified = True
    # def add(self, shoe, color, size, quantity=1):
    #     shoe_id = str(shoe.id)
    #     # shoe_color = str(color)
    #     # shoe_size = str(size)
    #
    #     # shoe_id = str(shoe.id)
    #     if shoe_id in self.cart:
    #         self.cart[shoe_id]['quantity'] += {'quantity': 0, 'price': str(shoe.price), 'color': color, 'size': size}
    #         self.cart[shoe_id]['quantity'] += quantity
    #         self.save()
    #
    # def save(self):
    #     self.session.modified = True

    # def __len__(self):
    #     return sum(item['quantity'] for item in self.cart.values())
        # else:
        #     #     self.cart[shoe_id] = shoe_color
        #     # self.session.modified=True
        #     self.cart[shoe_id] = {'quantity': 1, 'color': shoe_color, 'size': shoe_size}
        #     self.session.modified = True
        # بازگردانی طول سبد خرید------
    # def __len__(self):
    #     return len(self.cart)
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    #دریافت کفش ها در سبد خرید-----
    def get_shoes(self):
        # shoe_ids=self.cart.keys()
        # shoes=Shoe.objects.filter(id__in=shoe_ids)
        # return shoes
        shoe_ids = self.cart.keys()
        shoes = Shoe.objects.filter(id__in=shoe_ids)
        return shoes

    def delete(self,shoe):
        shoe_id=str(shoe)
        if shoe_id in self.cart:
            del self.cart[shoe_id]
        self.session.modified = True


    # def get_cl(self):
    #     colors=self.cart
    #     return colors
    # def get_cl(self):
    #     colors = {}
    #     for shoe_id, item in self.cart.items():
    #         colors[shoe_id] = item['color']
    #     return colors

    def get_cl(self):
        colors = {}
        for shoe_id, item in self.cart.items():
            if isinstance(item, dict) and 'color' in item:
                colors[shoe_id] = item['color']
        return colors


    def get_si(self):
        sizes = {}
        for shoe_id, item in self.cart.items():
            if isinstance(item, dict) and 'size' in item:
               sizes[shoe_id] = item['size']
        return sizes

    # def get_total_price(self):
    #     total_price = 0
    #     for item in self.cartitem_set.all():
    #         if item.shoe.is_sale:
    #             total_price += item.shoe.sale_price * item.quantity
    #         else:
    #             total_price += item.shoe.price * item.quantity
    #     return total_price


    # def get_total_price(self):
    #     cart_items = Cart.objects.all()
    #     total_price = sum(
    #         item.shoe.sale_price * item.quantity if item.shoe.is_sale else item.shoe.price * item.quantity
    #         for item in cart_items
    #     )
    #
    #     return total_price


    #
    # def get_total(self):
    #     shoe_ids=self.cart.keys()
    #     shoes=Shoe.objects.filter(id__in=shoe_ids)
    #     total=0
    #     for key,value in self.cart.items():
    #         # key=int(key)
    #        shoe_id = int(key)
    #          quantity = value['quantity']
    #         for shoe in shoes:
    #             if shoe.id == shoe_id:
    #                 if shoe.is_sale:
    #                     total=total + (shoe.sale_price * quantity)
    #                 else:
    #                     total=total + (shoe.price *quantity)
    #
    #
    #         return total
    #
