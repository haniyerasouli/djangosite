from django.shortcuts import render

from shoes.models import Shoe


#----view صفحه اصلی
def viewhome(request):
    shoe_record = Shoe.objects.all()  # یا هر فیلتری که مد نظر شماست
    context = {
        'shoe_record': shoe_record,
    }
    return render(request, 'home_page.html', context)

