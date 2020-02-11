from django.shortcuts import render, redirect
from app.models.payment import Payment
from app.forms.paymentform import PaymentForm
from app.models.customer import Customer
from app.authentication import Authenticate

@Authenticate.user_valid
def index(request):
    payments = Payment.objects.all()
    return render(request, "payment/index.html", {'payments': payments})

@Authenticate.user_valid
def create(request):
    customers = Customer.objects.all()
    if request.method == "POST":
        form = PaymentForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect("/payment")
            except:
                pass
    else:
        form = PaymentForm()
    return render(request, "payment/create.html", {'form': form,'customers':customers})
