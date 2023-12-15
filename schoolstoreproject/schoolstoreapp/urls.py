from django.urls import path
from . import views
app_name = 'schoolstoreapp'

urlpatterns=[
    path('',views.home,name='home'),
    path('purchase/',views.purchase,name='purchase'),
    path('order/',views.order,name='order')

]