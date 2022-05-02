from django.urls import path 
from . import views 

urlpatterns = [
    path('vet_account', views.signup, name='signup'),
]