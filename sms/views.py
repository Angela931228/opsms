
from django.shortcuts import render,get_object_or_404,redirect
from .models import Product,Staff,Promo_event,DiscoutingTable
from django.http import HttpResponse
import pandas as pd
from .apriori import processApriori
import numpy as np
import csv
from multiprocessing import Pool
import json
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
	pool = Pool(processes=1) 
	args = ['0','0.001', '0.8','9835','whole milk', 'whole milk']
	#processApriori(args)
	pool.apply_async(processApriori, args, ) 
	rule_list  = readData('ruledf.csv')
    	rule_list1 = readData('ruledf1.csv')
	rule_list2 = readData('ruledf2.csv')
	context = {
		'rule_list':rule_list,
		'rule_list1':rule_list1,
		'rule_list2':rule_list2
    	}
	return render(request, 'sms/mb_analysis.html', context)

def promo_analysis(request):
	event_list= Promo_event.objects.all()
	context = {'event_list': event_list}
	return render(request, 'sms/promo_analysis.html', context)
def cal_pur(request):
	product_list= Product.objects.all()
	context = {'product_list': product_list}
	return render(request, 'sms/cal_pur.html', context)

def expiry_food_discount(request):
	product_list= Product.objects.all()
	context = {'product_list': product_list}

	if request.method == 'POST':
		print request.body
		data = json.loads(request.body)
		p = Promo_event(name=data['event_name'], event_type='discounting', start_date=data["start_date"], end_date=data["end_date"])
		p.save()
		for  item in  data['data']:

				x = get_object_or_404(Product, pk=item['value'])
				x.discount_rate = data['discount_rate']
				x.save(update_fields=["discount_rate"]) 
				print item['value']
				dt = DiscoutingTable(product_id= Product.objects.get(id=item['value']), promo_event_id= p, discount_rate =data['discount_rate'],start_date=data["start_date"], end_date=data["end_date"] )
				dt.save()
		response = {'status': 1, 'message': "Ok"}
		return HttpResponse(json.dumps(response), content_type='application/json')

	return render(request, 'sms/expiry_fd_dis.html', context)
def proact_management(request):
	event_list= Promo_event.objects.all()
	context = {'event_list': event_list}
	return render(request, 'sms/promo_activitys.html', context)

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
