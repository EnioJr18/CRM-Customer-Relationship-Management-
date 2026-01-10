from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from .models import Lead, Interaction
from .forms import LeadForm, InteractionForm


def dashboard(request):
    total_leads = Lead.objects.count()
    leads_por_status = Lead.objects.values('status').annotate(total=Count('status'))
    leads_por_prioridade = Lead.objects.values('prioridade').annotate(total=Count('prioridade'))
    interacoes_recentes = Interaction.objects.select_related('lead').order_by('-data_interacao')[:5]

    contexto = {
        'total_leads': total_leads,
        'leads_por_status': leads_por_status,
        'leads_por_prioridade': leads_por_prioridade,
        'interacoes_recentes': interacoes_recentes,
    }

    return render(request, 'leads/dashboard.html', contexto)


def criar_lead(request):
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            lead = form.save(commit=False)
            lead.agente_responsavel = request.user
            lead.save()
            return redirect('leads:dashboard')
    else:
        form = LeadForm()
    
    return render(request, 'leads/criar_lead.html', {'form': form})

def lead_detail(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    interacoes = Interaction.objects.filter(lead=lead).order_by('-data_interacao')
    if request.method == 'POST':
        form = InteractionForm(request.POST)
        if form.is_valid():
            interacao = form.save(commit=False)
            interacao.lead = lead
            interacao.save()
            return redirect('leads:lead_detail', pk=lead.pk)
    else:
        form = InteractionForm()

    contexto = {
        'lead': lead,
        'interacoes': interacoes,
        'form': form,
    }
    return render(request, 'leads/lead_detail.html', contexto)
