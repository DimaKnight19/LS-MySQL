from .views import customer_reg, index, customer_list, customer_detail 
from django.urls import path

app_name = "ls"

urlpatterns = [
    path('customer_reg/', customer_reg, name='customer_reg'),
    path('', index, name='index'),
    path('customer_list/', customer_list, name='customer_list'),
    path('<int:pk>/', customer_detail, name='customer_detail'),
]

