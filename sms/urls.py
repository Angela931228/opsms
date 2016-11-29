from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^inventory_management/', views.inventory_management, name='inventory_management'),
    url(r'^sales_management/sales_analysis', views.sales_analysis, name='sales_analysis'),
    url(r'^sales_management/mb_analysis', views.mb_analysis, name='sales_analysis'),
    url(r'^approval', views.approval, name='approval'),
    url(r'^calendar/', views.calendar, name='calendar'),
    url(r'^sales_management/promo_analysis',views.promo_analysis, name= 'promo_analysis'),
    url(r'^sales_management/buddling_sales/',views.promo_analysis, name= 'promo_analysis'),
    url(r'^sales_management/expiry_food_discount/',views.expiry_food_discount, name= 'expiry_food_discount'),
    url(r'^sales_management/directmarketing/',views.directmarketing, name= 'expiry_food_discount'),
    url(r'^sales_management/cal_pur/',views.cal_pur, name= 'cal_pur'),
    url(r'^sales_management/proact_management/',views.proact_management,name ='proact_management'),
    url(r'^sales_management/proact_delete',views.proact_delete,name ='proact_delete'),
    url(r'^sales_management/proact_pause',views.proact_pause,name ='proact_pause'),
    url(r'^sales_management/proact_reopen',views.proact_reopen,name ='proact_reopen'),
    url(r'^sales_management/proact_search',views.proact_search,name ='proact_search'),
    url(r'^sales_management/proact_editview(?P<event_id>[0-9]+)/',views.proact_edit,name ='proact_edit'),
    url(r'^sales_management/markdowns',views.markdowns,name ='markdowns'),
    url(r'^sales_management/proact_view(?P<event_id>[0-9]+)/',views.proact_view,name ='proact_management')
]