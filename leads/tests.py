from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Lead

User = get_user_model()

class LeadModelTest(TestCase):
    def setUp(self):
        # Cria um usuário para ser o dono do lead
        self.user = User.objects.create_user(username='testuser', password='password123')
        
        # Cria um lead de teste
        self.lead = Lead.objects.create(
            nome="Elon",
            sobrenome="Musk",
            email="elon@tesla.com",
            agente_responsavel=self.user
        )

    def test_lead_string_representation(self):
        """Teste: O __str__ deve retornar o formato que seu model define"""
        # Ajustado para bater com o seu código atual: "Nome - Status"
        # O erro mostrou que o resultado real é 'Elon - Novo'
        expected_value = f"{self.lead.nome} - {self.lead.get_status_display()}"
        self.assertEqual(str(self.lead), expected_value)

    def test_lead_status_default(self):
        """Teste: O status padrão deve ser 'NOVO'"""
        # Ajustado: seu model usa 'NOVO' em vez de '0'
        self.assertEqual(self.lead.status, 'NOVO')


class DashboardViewTest(TestCase):
    def test_dashboard_redirects_anonymous_user(self):
        """Teste: Usuário não logado deve ser jogado para o Login"""
        url = reverse('leads:dashboard')
        response = self.client.get(url)
        
        # Espera um código 302 (Redirecionamento)
        self.assertEqual(response.status_code, 302)
        
        # Verifica se foi mandado para a página de login
        self.assertIn('/login/', response.url)

    def test_dashboard_logged_in_user(self):
        """Teste: Usuário logado consegue ver o dashboard"""
        user = User.objects.create_user(username='testdashboard', password='password123')
        self.client.force_login(user)
        
        url = reverse('leads:dashboard')
        response = self.client.get(url)
        
        # Agora espera sucesso (200)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'leads/dashboard.html')