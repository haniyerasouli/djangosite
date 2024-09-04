from django.db import models

# Create your models here.
from datetime import datetime

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.template.defaultfilters import slugify
from django.db import connection

from unidecode import unidecode


# ----تابع get_slug  برای فارسی ایجاد اسلاگ برای زبان فارسی
def get_slug(text):
    return slugify(unidecode(text))


# Create your models here.

# ----discription model


class Category(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها '
class Discription(models.Model):
    name = models.CharField(max_length=100, verbose_name='توضیح')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'توضیح'
        verbose_name_plural = 'توضیحات'


# --------size model
class Size(models.Model):
    range = models.IntegerField(null=True, blank=True, verbose_name='اندازه')

    # slug=models.SlugField(default='',null=False,db_index=True)

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.range)
    #     super().save(*args, **kwargs)
    def __int__(self):
        return self.range

    def __str__(self):
        return str(self.range)

    class Meta:
        verbose_name = 'اندازه'
        verbose_name_plural = 'اندازه ها'


# --------kind model
class Kind(models.Model):
    name = models.CharField(max_length=50, verbose_name='جنس رویه')
    slug = models.CharField(max_length=25, default='', unique=True, null=False, db_index=True,verbose_name='اسلاگ در url')

    def save(self, *args, **kwargs):
        self.slug = get_slug(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'جنس رویه'
        verbose_name_plural = 'جنس های رویه'


class Color(models.Model):
    name = models.CharField(max_length=50, verbose_name='رنگ')
    # slug = models.CharField(max_length=25, default='', unique=True, null=False, db_index=True,verbose_name='اسلاگ در url')
    #
    # def save(self, *args, **kwargs):
    #     self.slug = get_slug(self.name)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'رنگ'
        verbose_name_plural = 'رنگ ها'


# class Photo(models.Model):
#     item=models.ImageField(upload_to='files/shoes', verbose_name='عکس')
#
#     def __str__(self):
#         return self.item
#
#     class Meta:
#         verbose_name = 'عکس'
#         verbose_name_plural = 'عکس ها'

class Shoe(models.Model):
    brand = models.CharField(max_length=30, verbose_name='برند')
    property = models.CharField(max_length=30, verbose_name='ویژگی')
    # color = models.ForeignKey(Color, on_delete=models.CASCADE, null=True, blank=True, verbose_name='رنگ')
    color=models.ManyToManyField(Color ,verbose_name='رنگ')
    kind = models.ForeignKey(Kind, on_delete=models.CASCADE, null=True, blank=True, verbose_name='جنس رویه')
    # price=models.DecimalField(max_digits=8,decimal_places=2,verbose_name='قیمت')
    price = models.IntegerField(null=True, blank=True, verbose_name='قیمت')
    discription = models.OneToOneField(Discription, on_delete=models.CASCADE, null=True, blank=True,
                                       verbose_name='توضیح')
    # size = models.ForeignKey(Size,on_delete=models.CASCADE,null=True, blank=True, verbose_name='اندازه')
    size=models.ManyToManyField(Size, verbose_name='اندازه')
    # speces=models.FileField(upload_to='files/shoes')
    photo=models.ImageField(upload_to='files/shoes',null=True,blank=True, verbose_name='عکس منتخب')
    gender = models.CharField(max_length=10, verbose_name='جنسیت')
    is_sale=models.BooleanField(default=False, verbose_name='تخفیف')
    sale_price=models.IntegerField(null=True, blank=True, verbose_name='قیمت تخفیف')

    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True, blank=True,default=1,verbose_name='دسته بندی')
    notexist=models.BooleanField(default=False, verbose_name='ناموجود')
    slug = models.CharField(max_length=50, default='', null=False, db_index=True, verbose_name='اسلاگ در url')
    id = models.AutoField(primary_key=True)

    def save(self, *args, **kwargs):
        self.slug = get_slug(self.property + '_' + self.brand + '-' + self.gender)
        super(Shoe, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.property}-----{self.kind}----{self.discription}----{self.slug}'

    class Meta:
        verbose_name = 'کفش'
        verbose_name_plural = 'کفش ها'

class ShoeColorInventory(models.Model):
        shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)
        color = models.ForeignKey(Color, on_delete=models.CASCADE)
        quantity = models.PositiveIntegerField()

        def __str__(self):
            return f"{self.shoe.brand} - {self.color.name} - {self.quantity}"


class ShoeSizeInventory(models.Model):
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.shoe.brand} - {self.quantity}"


# class ShoeColorSizeInventory(models.Model):
#     shoe = models.ManyToManyField(Shoe)
#     color = models.ManyToManyField(Color)
#     size = models.ManyToManyField(Size)
#     quantity = models.PositiveIntegerField()
#
#     def __str__(self):
#         return f"{self.shoe.brand} - {self.color.name} - {self.size.range} - {self.quantity}"
#
#     class Meta:
#         # unique_together = ('shoe', 'color', 'size')
#         verbose_name = 'موجودی کفش بر اساس رنگ و سایز'
#         verbose_name_plural = 'موجودی کفش ها بر اساس رنگ و سایز'



class Order(models.Model):
    shoe=models.ForeignKey(Shoe,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    addres=models.CharField(max_length=400, default='',blank=False)
    phone=models.CharField(max_length=20, blank=True)
    status=models.BooleanField(default=False)
    def __str__(self):
        return self.order.addres


    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارش ها'



class Cart(models.Model):
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.shoe.brand} - {self.quantity}"

    def get_total_price(self):
        total_price = 0
        for item in self.items.all():
            total_price += item.shoe.price * item.quantity
        return total_price

    # def get_shoes(self):
    #     return self.shoe

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبد خرید'



class ShoeImage(models.Model):
    shoe=models.ForeignKey(Shoe,related_name='images',on_delete=models.CASCADE,verbose_name='عکس کفش')
    image=models.ImageField(upload_to='files/shoes',null=True,blank=True,verbose_name='دیگر عکس ها')

    def __str__(self):
        return f"{self.image}"