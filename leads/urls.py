from django.urls import path
from .views import dashboard, lead_detail, lead_list, lead_create, lead_update, lead_delete, interaction_delete
from leads import views

app_name = 'leads'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('novo/', lead_create, name='lead_create'),
    path('<int:pk>/', lead_detail, name='lead_detail'),
    path('lista/', lead_list, name='lead_list'),
    path('<int:pk>/editar/', lead_update, name='lead_update'),
    path('<int:pk>/deletar/', lead_delete, name='lead_delete'),
    # Interações
    path('interacao/<int:pk>/editar/', views.interaction_update, name='interaction_update'),
    path('interacao/<int:pk>/deletar/', views.interaction_delete, name='interaction_delete'),
    
    # Busca e Filtros
    path('busca/', views.lead_search, name='lead_search'),
    path('recentes/', views.recent_leads, name='recent_leads'),
    path('sem-interacao/', views.leads_without_interactions, name='leads_without_interactions'),
    path('prioridade-alta/', views.high_priority_leads, name='high_priority_leads'),
    
    # Exportação
    path('exportar/csv/', views.export_leads_csv, name='export_leads_csv'),
    path('exportar/interacoes/<int:lead_id>/csv/', views.export_interactions_csv, name='export_interactions_csv'),
]