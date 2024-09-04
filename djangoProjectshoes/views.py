from django.shortcuts import render


#----view صفحه اصلی
def viewhome(request):
    return render(request,'home_page.html')

