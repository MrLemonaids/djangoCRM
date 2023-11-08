from django.urls import path
from . import views

urlpatterns = [
    path('add_lead/', views.add_lead, name='add_lead'),
    path('leads_list', views.leads_list, name='leads_list'),
    path('lead_details/<int:pk>', views.lead_details, name='lead_details'),
    path('lead_delete/<int:pk>', views.lead_delete, name='lead_delete'),
    path('lead_edit/<int:pk>', views.lead_edit, name='lead_edit'),
]