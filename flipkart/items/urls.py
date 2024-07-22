from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('mobiles/<int:id>',views.mview),
    path('laptop/<int:id>',views.lview),
    path('airpods/<int:id>',views.aview)
]