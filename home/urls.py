from . import views
from django.urls import path

urlpatterns = [
    path('home/',views.index,name='index'),
    path('home/undermaintainance',views.undermaintainance,name='undermaintainance'),
    path('generate_password/', views.generate_random_password, name='generate_random_password'),
]




