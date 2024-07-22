from django.urls import path
from . import views
urlpatterns = [
    path('user/<int:id>',views.main),
    path('admin/<int:id>',views.main1)
]