
from django.shortcuts import render,get_object_or_404
from .models import Product
import pandas as pd
from .apriori import processApriori
import numpy as np
import csv
# Create your views here.


def index(request):
	product_list= Product.objects.all()
	context = {'product_list': product_list}
	return render(request, 'sms/index.html', context)

def detail(request,product_id):
	product = get_object_or_404(Product, pk=product_id)
	return render(request, 'sms/detail.html', {'product': product})

def inventory_management(request):
	product_list= Product.objects.all()
	context = {'product_list': product_list}
	return render(request, 'sms/inventory_management.html', context)

def calendar(request):
	product_list= Product.objects.all()
	context = {'product_list': product_list}
	return render(request, 'sms/calendar.html', context)

def sales_analysis(request):
	product_list= Product.objects.all()
	context = {'product_list': product_list}
	return render(request, 'sms/sales_analysis.html', context)

def mb_analysis(request):
	args = ['0','0.001', '0.8','9835','whole milk', 'whole milk']
	processApriori(args)
	rule_list  = readData('ruledf.csv')
    	rule_list1 = readData('ruledf1.csv')
	rule_list2 = readData('ruledf2.csv')
	context = {
		'rule_list':rule_list,
		'rule_list1':rule_list1,
		'rule_list2':rule_list2
    	}
	return render(request, 'sms/mb_analysis.html', context)

def readData(fname):
	rule_list = []
	with open('./sms/static/sms/data/'+fname) as f:
                reader = csv.DictReader(f)
                for row in reader:
                        rule_list.append(row)
	return rule_list
def approval(request):
	product_list= Product.objects.all()
	context = {'product_list': product_list}
	return render(request, 'sms/approval.html', context)
