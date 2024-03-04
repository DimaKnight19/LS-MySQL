from django.contrib import admin
from .models import Customer, Sale, Shop 


admin.site.register(Shop)


@admin.register(Customer)
class Customer(admin.ModelAdmin):
    list_display=('name', 'surname','email', 'phone', 'dt_of_reg',
                  'percent_of_discount', 'current_balance', 'money_spent_cus', 'shop')
    
    list_filter=('phone', 'dt_of_reg', 
                  'percent_of_discount', 'shop')


@admin.register(Sale)
class Sale(admin.ModelAdmin):
    list_display=('purchase_amount', 'accumulated_bonuses','the_number_of_bonuses_to_be_debited', 'sum_of_purchase', 'shop', 
                  'customer', 'current_balance', 'dt_of_sale', 'time_of_sale')
    list_filter=('customer', 'dt_of_sale', 'time_of_sale', 'shop')
    
