"""BillingSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from app.views import itemview, customerview, orderview, paymentview,views

urlpatterns = [
    path('item', itemview.index),
    path('item_create', itemview.create),
    path('item_edit/<int:id>', itemview.edit),
    path('item_update/<int:id>', itemview.update),
    path('item_delete/<int:id>', itemview.delete),

    path('customer', customerview.index),
    path('customer_create', customerview.create),
    path('customer_edit/<int:id>', customerview.edit),
    path('customer_update/<int:id>', customerview.update),
    path('customer_delete/<int:id>', customerview.delete),

    path('order', orderview.index),
    path('order_create', orderview.create),
    path('order_delete/<int:id>', orderview.delete),

    path('payment', paymentview.index),
    path('payment_create', paymentview.create),
    path('',views.index),
    path('layout',views.layout),
path('search',customerview.search),
    path('entry',views.entry)
]
