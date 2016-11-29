
from django.shortcuts import render,get_object_or_404,redirect
from .models import Product,Staff,Promo_event,DiscoutingTable
from django.http import HttpResponse
from .apriori import processApriori
import csv
from multiprocessing import Pool
import json
from itertools import chain
import datetime
# Create your views here.


def index(request):
	product_list= Product.objects.all()
	context = {'product_list': product_list}
	return render(request, 'sms/index.html', context)


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
	if request.method == 'POST':
		print request.body
		data = json.loads(request.body)
		p = Promo_event(name=data['event_name'], event_type='Buddle selling', priority=data["priority"],start_date=data["start_date"], end_date=data["end_date"])
		p.save()
		for  item in  data['data']:
				x = Product.objects.get(product_name=item['name'])
				x.discount_rate = data['discount_rate']
				x.save(update_fields=["discount_rate"]) 
				dt = DiscoutingTable(product_id= Product.objects.get(product_name=item['name']), promo_event_id= p, discount_rate =data['discount_rate'],start_date=data["start_date"], end_date=data["end_date"] )
				dt.save()
		response = {'status': 1, 'message': "Ok"}
		return HttpResponse(json.dumps(response), content_type='application/json')
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
	event_list= Promo_event.objects.all().order_by('id').reverse()
	context = {'event_list': event_list}
	return render(request, 'sms/promo_analysis.html', context)

def cal_pur(request):
	product_list= Product.objects.all()
	dt_list = DiscoutingTable.objects.all()
	for product in product_list:
		if not DiscoutingTable.objects.filter(product_id = product).exists():
			product.discount_rate = 1.0
			product.save()
	context = {'product_list': product_list}
	return render(request, 'sms/cal_pur.html', context)


def directmarketing(request):
	product_list= Product.objects.all()
	context = {'product_list': product_list}
	return render(request, 'sms/directmarketing.html', context)

def expiry_food_discount(request):
	product_list= Product.objects.all()
	dt_list = DiscoutingTable.objects.all()
	for product in product_list:
		if not DiscoutingTable.objects.filter(product_id = product).exists():
			product.discount_rate = 1.0
			product.save()
	context = {'product_list': product_list}
	

	if request.method == 'POST':
		print request.body
		data = json.loads(request.body)
		p = Promo_event(name=data['event_name'], event_type='discounting', start_date=data["start_date"], end_date=data["end_date"], priority=data["priority"])
		p.save()
		for  item in  data['data']:
				x = get_object_or_404(Product, pk=item['value'])
				x.discount_rate = data['discount_rate']
				x.save(update_fields=["discount_rate"]) 
				dt = DiscoutingTable(product_id= Product.objects.get(id=item['value']), promo_event_id= p, discount_rate =data['discount_rate'],start_date=data["start_date"], end_date=data["end_date"] )
				dt.save()
		response = {'status': 1, 'message': "Ok"}
		return HttpResponse(json.dumps(response), content_type='application/json')

	return render(request, 'sms/expiry_fd_dis.html', context)

def proact_management(request):
	event_list= Promo_event.objects.all().order_by('id').reverse()
	context = {'event_list': event_list}
	return render(request, 'sms/promo_activitys.html', context)

def proact_delete(request):
	if request.method == 'POST':
		data = json.loads(request.body)
		Promo_event.objects.filter(id=data['data']).delete()
		response = {'status': 1, 'message': "Ok"}
		return HttpResponse(json.dumps(response), content_type='application/json')
def proact_pause(request):
	if request.method == 'POST':
		data = json.loads(request.body)
		p = Promo_event.objects.get(id=data['data'])
		p.status = 'pause'
		p.save()
		response = {'status': 1, 'message': "Ok"}
		return HttpResponse(json.dumps(response), content_type='application/json')
def proact_reopen(request):
	if request.method == 'POST':
		data = json.loads(request.body)
		p = Promo_event.objects.get(id=data['data'])
		p.status = 'active'
		p.save()
		response = {'status': 1, 'message': "Ok"}
		return HttpResponse(json.dumps(response), content_type='application/json')

def proact_search(request):
	if request.method == 'POST':
		data = json.loads(request.body)


		p = Product.objects.get(product_name =data['data'])
		dt = DiscoutingTable.objects.get(product_id=p)
		return HttpResponse(json.dumps(response), content_type='application/json')

def proact_edit(request,event_id):

	event = Promo_event.objects.get(id=event_id)
	dtList = DiscoutingTable.objects.filter(promo_event_id=event_id)
	dt = dtList.first()
	discount_rate = dt.discount_rate
	context = {
			'event' :event,
			'dtList' :dtList,
			'discount_rate':discount_rate
	}

	return render(request, 'sms/pro_form.html', context)


def proact_view(request,event_id):
	dtList = DiscoutingTable.objects.filter(promo_event_id=event_id)
	return render(request, 'sms/event.html', {'dtList': dtList})

def markdowns(request):
	if request.method == 'POST':
		print request.body
		data = json.loads(request.body)
		p = Promo_event(name=data['event_name'], event_type='Buddle selling', priority=data["priority"],start_date=data["start_date"], end_date=data["end_date"])
		p.save()
		for  item in  data['data']:
				x = Product.objects.get(product_name=item['name'])
				x.discount_rate = data['discount_rate']
				x.save(update_fields=["discount_rate"]) 
				dt = DiscoutingTable(product_id= Product.objects.get(product_name=item['name']), promo_event_id= p, discount_rate =data['discount_rate'],start_date=data["start_date"], end_date=data["end_date"] )
				dt.save()
		response = {'status': 1, 'message': "Ok"}
		return HttpResponse(json.dumps(response), content_type='application/json')
	product_list= Product.objects.all()
	dt_list = DiscoutingTable.objects.all()
	for product in product_list:
		if not DiscoutingTable.objects.filter(product_id = product).exists():
			product.discount_rate = 1.0
			product.save()
	context = {'product_list': product_list}
	return render(request, 'sms/markdowns.html', context)

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
