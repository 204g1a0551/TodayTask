from django.urls import path,include
from Heros import views
urlpatterns = [
    path('balaya/<int:id>',views.balaya),
    path('chiru/<int:id>',views.chiru),
    path('mahesh/<int:id>', views.mahesh),
]