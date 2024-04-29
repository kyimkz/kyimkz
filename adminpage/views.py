from django.shortcuts import render, redirect
from core.models import CartOrder, Product, Category
from django.db.models import Sum
from userauths.models import User

import datetime

def dashboard(request):
    revenue = CartOrder.objects.aggregate(price=Sum("price"))
    total_order = CartOrder.objects.all()
    all_products = Product.objects.all()
    all_categories = Category.objects.all()
    customers = User.objects.all().order_by("-id")

    month = datetime.datetime.now().month

    monthly_income = CartOrder.objects.filter(order_date__month=month).aggregate(price=Sum("price"))

    context = {
        "revenue":revenue,
        "total_order":total_order,
        "all_products":all_products,
        "all_categories":all_categories,
        "customers":customers,
        "monthly_income":monthly_income,
    }

    return render(request, "adminpage/dashboard.html", context)