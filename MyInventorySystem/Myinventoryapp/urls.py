from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [ 
    path('view_supplier/<int:id>/', views.view_supplier, name='view_supplier'),
    path('view_bottles/<int:id>/', views.view_bottles, name='view_bottles'),
    path('view_bottle_details/<int:id>/<int:pk>/', views.view_bottle_details, name='view_bottle_details'),
    path('delete_bottle/<int:id>/<int:pk>/', views.delete_bottle, name='delete_bottle'),
    path('add_bottle/<int:id>/', views.add_bottle, name='add_bottle'),
    path('', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('manage_account/<int:id>/', views.manage_account, name='manage_account'),
    path('change_password/<int:id>/', views.change_password, name='change_password'),
    path('delete_account/<int:id>/', views.delete_account, name='delete_account'),
]