
from django.shortcuts import render,get_object_or_404
from .models import Product
# Create your views here.


def index(request):
	product_list= Product.objects.all()
	context = {'product_list': product_list}
	return render(request, 'sms/index.html', context)

def detail(request,product_id):
	product = get_object_or_404(Product, pk=product_id)
	return render(request, 'sms/detail.html', {'product': product})