from django.shortcuts import render, redirect
from app.models.order import Order
from app.forms.orderform import OrderForm
from app.models.customer import Customer
from app.models.item import Item
from app.authentication import Authenticate

@Authenticate.user_valid
def index(request):
    orders = Order.objects.all()
    return render(request, "order/index.html", {'orders': orders})

@Authenticate.user_valid
def create(request):
    customers = Customer.objects.all()
    items = Item.objects.all()
    print(request.method == "POST")
    if request.method == "POST":
        print(request.POST)
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect("/order")
            except:
                pass
    else:
        form = OrderForm()
    return render(request, "order/create.html", {'form': form, 'items': items, 'customers': customers})
@Authenticate.valid_user_include_id
def delete(request, id):
    order = Order.objects.get(id=id)
    order.delete()
    return redirect("/order")
