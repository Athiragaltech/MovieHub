from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'), 
    path('contact1',views.contact1,name='contact1'),
    path('view/',views.view,name='view'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('edit/<int:id>',views.edit),
    path('update/<int:id>',views.update,name='update'),
    path('blog/<int:id>',views.continu,name='continu'),
    path('continu/<int:id>',views.continu,name='continu')
]