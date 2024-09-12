from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('stkpush/', views.mpesa_stkpush, name='stkpush_view'),
    path('till_balance', views.till_balance_query, name='till_balance_query'),
]

