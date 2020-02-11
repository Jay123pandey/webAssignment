from django.shortcuts import render, redirect
from app.models.customer import Customer
from app.forms.customerform import CustomerForm
from django.http import HttpResponse,JsonResponse
from app.authentication import Authenticate

@Authenticate.user_valid
def index(request):
    customers = Customer.objects.all()
    return render(request, "customer/index.html", {'customers': customers})

@Authenticate.user_valid
def search(request):
	Customers=Customer.objects.filter(Customer_name__contains=request.GET['search']).values()
	return JsonResponse(list(Customers),safe=False)

@Authenticate.user_valid
def create(request):
    if request.method == "POST":
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect("/customer")
            except:
                pass
    else:
        form = CustomerForm()
    return render(request, "customer/create.html", {'form': form})

@Authenticate.valid_user_include_id
def edit(request, id):
    customer = Customer.objects.get(Customer_id=id)
    return render(request, "customer/edit.html", {'customer': customer})

@Authenticate.valid_user_include_id
def update(request, id):
    customer = Customer.objects.get(Customer_id=id)
    form = CustomerForm(request.POST, request.FILES, instance=customer)
    if form.is_valid():
        form.save()
        return redirect('/customer')
    return render(request, "customer/edit.html", {'customer': customer})


def delete(request, id):
    customer = Customer.objects.get(Customer_id=id)
    customer.delete()
    return redirect("/customer")
