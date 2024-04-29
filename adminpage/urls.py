from django.urls import path
from adminpage import views

app_name = "adminpage"

urlpatterns = [
path('dashboard/', views.dashboard, name="dashboard"),
]
