from django.urls import path
from .views import *
from act import views

urlpatterns = [
    
    path('logout/',logout,name='logout'),
    path('login/',login,name='log'),
    path('resgister/',register,name='reg'),

]