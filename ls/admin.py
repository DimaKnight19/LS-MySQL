from django.contrib import admin
from .models import Customer, Sale, Shop 


admin.site.register(Shop)


#обновленный код
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=('name', 'surname','email', 'phone', 'dt_of_reg',
                  'percent_of_discount', 'current_balance', 'money_spent_cus', 'shop')
    list_filter=('dt_of_reg', 'percent_of_discount', 'shop')


    def save_model(self, request, obj, form, change):
        # Проверяем, изменилось ли поле percent_of_discount
        if change and 'percent_of_discount' in form.changed_data:
            # Обновляем поле money_spent_cus в соответствии с новым процентом скидки
            if obj.percent_of_discount == 3:
                obj.money_spent_cus = 10001
            elif obj.percent_of_discount == 5:
                obj.money_spent_cus = 20001
            elif obj.percent_of_discount == 7:
                obj.money_spent_cus = 30001
            elif obj.percent_of_discount == 10:
                obj.money_spent_cus = 50001
            elif obj.percent_of_discount == 2:
                obj.money_spent_cus = 0       
        # Вызываем super().save_model для сохранения изменений
        super().save_model(request, obj, form, change)

#Старый рабочий код
# @admin.register(Customer)
# class Customer(admin.ModelAdmin):
#     list_display=('name', 'surname','email', 'phone', 'dt_of_reg',
#                   'percent_of_discount', 'current_balance', 'money_spent_cus', 'shop')
    
#     list_filter=('phone', 'dt_of_reg', 
#                   'percent_of_discount', 'shop')


@admin.register(Sale)
class Sale(admin.ModelAdmin):
    list_display=('purchase_amount', 'accumulated_bonuses','the_number_of_bonuses_to_be_debited', 'sum_of_purchase', 'shop', 
                  'customer', 'current_balance', 'dt_of_sale')
    list_filter=('dt_of_sale', 'shop', ) 