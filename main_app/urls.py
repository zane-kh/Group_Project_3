from importlib.resources import path
from unicodedata import name
from django.urls import path
from . import views 


urlpatterns = [
   path('', views.home, name='home'),
   path('about/', views.about, name='about'),
   path('patients/', views.patients_index, name='patients'),
   path('patients/<int:patient_id>/', views.patient_history, name='patient_history'),
   path('patients/create/', views.PatientCreate.as_view(), name='patients_create'),
   path('patients/<int:pk>/update', views.PatientUpdate.as_view(), name='patients_update'),
   path('patients/<int:pk>/delete', views.PatientDelete.as_view(), name='patients_delete'),
   path('services/', views.ServiceList.as_view(), name='services_index'),
   path('services/create', views.ServiceCreate.as_view(), name='service_create'),
   path('services/<int:pk>/', views.ServiceDetail.as_view(), name='service_detail'),
   path('services/<int:pk>/update', views.ServiceUpdate.as_view(), name='service_update'),
   path('services/<int:pk>/delete', views.ServiceDelete.as_view(), name='service_delete'),
]