from django.db import models
from django.contrib.auth.models import User


class Shop(models.Model):
    name = models.CharField(max_length=25, default='Al Barsha',                            
                            verbose_name="Shop", unique=True)
    def __str__(self):
        return self.name
    

class Customer(models.Model):
    name = models.CharField(max_length=25, verbose_name="Name")
    surname = models.CharField(max_length=25, verbose_name="Surname")
    email = models.EmailField(max_length=255, verbose_name="E-mail")
    
    phone = models.CharField(max_length=25,verbose_name="Phone", unique=True)
    
    dt_of_reg = models.DateTimeField(null=True, blank=True, verbose_name="Date and time of reg")

    percent_of_discount = models.IntegerField(verbose_name="Discount", default=2)
    
    
    current_balance = models.IntegerField(verbose_name="Bonus Balance", default=0)
    money_spent_cus = models.FloatField(verbose_name="Money spent (AED)", default=0)
    
    
    next_level = models.IntegerField(verbose_name="Кол-во бонусов для дальнейшей скидки", default=10000)


    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, verbose_name="Shop", to_field='name')
    def save(self, *args, **kwargs):
        if self.money_spent_cus <= 10000:
            self.percent_of_discount = 2
        elif 20000 >= self.money_spent_cus > 10001:
            self.percent_of_discount = 3
        elif 30000 >= self.money_spent_cus > 20001:
            self.percent_of_discount = 5
        elif 50000 >= self.money_spent_cus > 30001:
            self.percent_of_discount = 7
        elif self.money_spent_cus >= 50001:
            self.percent_of_discount = 10

        super(Customer, self).save(*args, **kwargs) 
    
    def __str__(self):
        return f"{self.phone}"


class Sale(models.Model):
    purchase_amount = models.FloatField(verbose_name="Sum of purchase")
    
    accumulated_bonuses = models.IntegerField(verbose_name="Received bonuses")

    the_number_of_bonuses_to_be_debited = models.IntegerField(verbose_name="Written-off bonuses", null=True) 
    
    sum_of_purchase = models.FloatField(verbose_name="Sum of sale")
    
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE,verbose_name="Shop", to_field='name') 
    
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,verbose_name="Phone", to_field='phone')
    percent_of_discount = models.IntegerField(verbose_name="Discount")
    current_balance = models.IntegerField(verbose_name="Bonus Balance", default=0)

    dt_of_sale = models.DateField(null=True, blank=True, verbose_name="Date")
    time_of_sale = models.TimeField(null=True, blank=True, verbose_name="Time")
    
    def save(self, *args, **kwargs):
        # Вызываем save родительского класса для сохранения Sale (часто его нужно ставить в конец)
        super(Sale, self).save(*args, **kwargs) 

   
        customer = self.customer
        customer.current_balance = self.current_balance 


        customer.money_spent_cus += float(self.sum_of_purchase)

        customer.save()


    def __str__(self):
        return f"{self.dt_of_sale}, {self.customer}"
