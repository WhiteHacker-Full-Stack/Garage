from django.urls import path
from .views import asosiypage,about,client,contact,products

urlpatterns =[
    path('', asosiypage,name= 'index'),
    path ( 'about/',about),
    path ('client/',client),
    path ('contact/',contact),
    path ('products/',products),
]
