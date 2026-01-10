from django.urls import path
from .views import dashboard, criar_lead, lead_detail

app_name = 'leads'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('criar/', criar_lead, name='criar_lead'),
    path('<int:pk>/', lead_detail, name='lead_detail'),
]