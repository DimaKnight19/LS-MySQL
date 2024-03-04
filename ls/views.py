from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Customer, Sale, Shop
from .forms import CustomerModelForm, SaleModelForm, CustomerSearchForm, LoginForm #CustomerForm,

from django.contrib.auth import authenticate, login




def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print("Name:", username)  # Добавьте эту строку для вывода имени пользователя в консоль
            print("Password:", password)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/ls')  # Поменяйте 'index' на имя вашего представления главной страницы
            else:
                error_message = "Invalid name or password."
                print("Authentication failed!")
    else:
        form = LoginForm()
        error_message = None
        
    context = {
        'form': form,
        'error_message': error_message
    }
    return render(request, 'ls/login.html', context)





def index(request):
    # Получаем список всех магазинов
    shops = Shop.objects.all()

    # Создаем пустой словарь для хранения количества клиентов в каждом магазине
    customers_count = {}

    # Для каждого магазина подсчитываем количество клиентов
    for shop in shops:
        customers_count[shop] = Customer.objects.filter(shop=shop).count()
    
    # Вычисляем общее количество клиентов по всем магазинам
    total_customers = sum(customers_count.values())

    # Передаем данные в шаблон
    return render(request, "ls/index.html", {"customers_count": customers_count, "total_customers": total_customers})




def customer_list(request):
    form = CustomerSearchForm(request.GET)
    customers = Customer.objects.all()

    if form.is_valid():
        search_query = form.cleaned_data['search_query']
        if search_query:
            customers = customers.filter(phone__icontains=search_query)

    context = {
        "customers": customers,
        "form": form,
    }

    return render(request, "ls/customer_list.html", context)



def customer_reg(request):
    form = CustomerModelForm()
    if request.method == "POST":
        print("Receiving a post request")
        form = CustomerModelForm(request.POST)
        if form.is_valid():
            form.save() 
            print('The Customer has been created')
            return redirect("/ls") #перенаправляет нас на страничку с лидами
    context ={
        "form": form #вставка из forms.py для того, чтобы можно было в html обращаться по {}
    }
    return render(request, "ls/customer_reg.html", context)



def customer_detail(request, pk):
    customer = Customer.objects.get(id=pk)
    shops = Shop.objects.all()
    if request.method == "POST":
        purchase_amount=request.POST.get('purchase_amount')
        the_number_of_bonuses_to_be_debited=request.POST.get('the_number_of_bonuses_to_be_debited')
        sum_of_purchase=request.POST.get('sum_of_purchase')
        accumulated_bonuses=request.POST.get('accumulated_bonuses')    
        customer=request.POST.get('customer')
        customer = Customer.objects.get(id=pk)
        percent_of_discount=customer.percent_of_discount
        current_balance=request.POST.get('new_bonuses')
        dt_of_sale=request.POST.get('dt_of_sale')
        time_of_sale=request.POST.get('time_of_sale')
        shop_name = request.POST.get('shop_name')  # Получаем имя магазина из POST-запроса
        shop = Shop.objects.get(name=shop_name) # Ищем магазин с указанным именем


        Sale.objects.create(
            purchase_amount=purchase_amount,
        
            the_number_of_bonuses_to_be_debited=the_number_of_bonuses_to_be_debited,

            sum_of_purchase=sum_of_purchase,
            accumulated_bonuses=accumulated_bonuses,
        
            customer=customer,
            percent_of_discount=percent_of_discount,
            current_balance=current_balance,
            
            dt_of_sale=dt_of_sale,
            time_of_sale=time_of_sale,
            shop=shop) # связываем объект Sale с выбранным магазином
        
        return redirect('/ls')


    context = {
        "customer": customer,
        "shops": shops
    }
    return render(request, "ls/customer_detail.html", context)
