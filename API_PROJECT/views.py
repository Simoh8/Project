from django.shortcuts import render
from. import forms
from django.http import HttpRequest, HttpResponse


# Create your views here.
def initiate_payment(request: HttpRequest) -> HttpResponse:
    if request.method== "POST":
        if payment_form.is_valid():
           payment= payment_form.save()
           render(request, 'make_payment.html', {'payment': payment})
  
        else:
            payment_form= forms.PaymentForm()
        return render(request, 'intiate_payments.html', {'payment': payment_form})
    
