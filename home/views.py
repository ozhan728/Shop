from django.shortcuts import render , get_object_or_404
from django.views import View
from .models import Product,Category
import time
from Shop.celery_conf import celery_app
# Create your views here.

# this is for celery test only
# @celery_app.task
# def my_task():
#     time.sleep(10)
#     with open('test.txt','w') as myFile:
#         print('*'*100)
#         print(myFile)

class HomeView(View):
    def get(self,request,category_slug=None):
        # this is for celery test only
        # my_task.delay()
        products = Product.objects.filter(available=True)
        categories = Category.objects.all()
        if category_slug:
            category = Category.objects.get(slug=category_slug)
            products = products.filter(category=category)
        return render(request,'home/home.html',{'products':products,'categories':categories})


class ProductDetailView(View):
    def get(self,request,slug):
        product = get_object_or_404(Product,slug=slug)
        return render(request,'home/detail.html',{'product':product})



