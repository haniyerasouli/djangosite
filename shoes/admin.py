from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import Shoe, Discription, Kind, Size, Color, ShoeColorInventory, ShoeSizeInventory, Category, Order, \
    ShoeImage


#برای پر شدن اسلاگ به صورت همزمان با نام ---
#نشان دادن نام به جای رکورد-----
class KindAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':['name']}
    list_display = ['name']

#برای پر شدن اسلاگبا ویژگی وبرند و رنگ و قیمت---
#نشان دادن ویژگی و برند و رنگ و قیمت و جنسیت  به جای رکورد-----
#فیلتر بر اساس قیمت------


class ShoeColorInventoryInline(admin.TabularInline):
    model = ShoeColorInventory
    extra = 1

class ShoeSizeInventoryInline(admin.TabularInline):
    model = ShoeSizeInventory
    extra = 1

class ShoeImageInline(admin.TabularInline):
    model= ShoeImage
    extra= 3


class ShoeAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'slug':['property','brand','price']}
    list_filter = ['price']
    list_display = ['property','brand','price','gender']
    inlines = [ShoeColorInventoryInline, ShoeSizeInventoryInline,ShoeImageInline]


#نشان دادن سایز به جای رکورد-----
class SizeAdmin(admin.ModelAdmin):
    list_display = ['range']

    def get_colors(self, obj):
        return ", ".join([color.name for color in obj.colors.all()])

    get_colors.short_description = 'Colors'


class ColorAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'slug':['name']}
    list_display = ['name']

# class PhotoAdmin(admin.ModelAdmin):
#     # prepopulated_fields = {'slug':['name']}
#     list_display = ['item']
class CategoryAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'slug':['name']}
    list_display = ['name']


class OrderAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'slug':['name']}
    list_display = ['shoe','quantity','addres','phone','status']








#
# admin.site.register(Discription,DiscriptinAdmin)
admin.site.register(Shoe,ShoeAdmin)
admin.site.register(Discription)
admin.site.register(Kind,KindAdmin)
admin.site.register(Size,SizeAdmin)
admin.site.register(Color,ColorAdmin)
# admin.site.register(Photo,PhotoAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(ShoeImage)