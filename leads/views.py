from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from .models import Lead, Interaction
from .forms import LeadForm, InteractionForm
import csv
from django.http import HttpResponse


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


def lead_create(request):
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            lead = form.save(commit=False)
            lead.agente_responsavel = request.user
            lead.save()
            return redirect('leads:dashboard')
    else:
        form = LeadForm()
    
    return render(request, 'leads/lead_create.html', {'form': form})

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


def lead_list(request):
    leads = Lead.objects.all().order_by('-criado_em')
    return render(request, 'leads/lead_list.html', {'leads': leads})


def lead_update(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    form = LeadForm(request.POST or None, instance=lead)
    if form.is_valid():
        form.save()
        return redirect('leads:lead_detail', pk=lead.pk)
    
    return render(request, 'leads/lead_create.html', {'form': form, 'lead': lead})

def lead_delete(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    
    if request.method == 'POST':
        lead.delete()
        return redirect('leads:lead_list')
    
    return render(request, 'leads/lead_delete.html', {'lead': lead})

def interaction_delete(request, pk):
    interacao = get_object_or_404(Interaction, pk=pk)
    lead_pk = interacao.lead.pk
    
    if request.method == 'POST':
        interacao.delete()
        return redirect('leads:lead_detail', pk=lead_pk)
    
    return render(request, 'leads/interaction_delete.html', {'interacao': interacao})

def interaction_update(request, pk):
    interacao = get_object_or_404(Interaction, pk=pk)
    form = InteractionForm(request.POST or None, instance=interacao)
    if form.is_valid():
        form.save()
        return redirect('leads:lead_detail', pk=interacao.lead.pk)
    
    return render(request, 'leads/interaction_update.html', {'form': form, 'interacao': interacao})

def lead_search(request):
    query = request.GET.get('q')
    leads = Lead.objects.filter(nome__icontains=query) if query else Lead.objects.none()

    return render(request, 'leads/lead_list.html', {'leads': leads, 'query': query})

def leads_by_status(request, status):
    leads = Lead.objects.filter(status=status).order_by('-criado_em')

    return render(request, 'leads/lead_list.html', {'leads': leads, 'filtro': f'Status: {status}'})

def leads_by_priority(request, prioridade):
    leads = Lead.objects.filter(prioridade=prioridade).order_by('-criado_em')

    return render(request, 'leads/lead_list.html', {'leads': leads, 'filtro': f'Prioridade: {prioridade}'})

def recent_leads(request):
    leads = Lead.objects.all().order_by('-criado_em')[:10]

    return render(request, 'leads/lead_list.html', {'leads': leads, 'filtro': 'Leads Recentes'})

def leads_without_interactions(request):
    leads = Lead.objects.annotate(num_interactions=Count('interactions')).filter(num_interactions=0)

    return render(request, 'leads/lead_list.html', {'leads': leads, 'filtro': 'Leads sem Interações'})

def high_priority_leads(request):
    leads = Lead.objects.filter(prioridade='ALTA').order_by('-criado_em')

    return render(request, 'leads/lead_list.html', {'leads': leads, 'filtro': 'Leads de Alta Prioridade'})

def leads_by_agent(request, agent_id):
    leads = Lead.objects.filter(agente_responsavel__id=agent_id).order_by('-criado_em')
    return render(request, 'leads/lead_list.html', {'leads': leads, 'filtro': f'Leads do Agente {agent_id}'})

def interactions_timeline(request, lead_id):
    lead = get_object_or_404(Lead, pk=lead_id)
    interacoes = Interaction.objects.filter(lead=lead).order_by('-data_interacao')
    return render(request, 'leads/interactions_timeline.html', {'lead': lead, 'interacoes': interacoes})

def export_leads_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="leads.csv"'

    writer = csv.writer(response)
    writer.writerow(['Nome', 'Email', 'Telefone', 'Status', 'Prioridade', 'Agente Responsável', 'Criado Em'])

    leads = Lead.objects.all().values_list('nome', 'email', 'telefone', 'status', 'prioridade', 'agente_responsavel__username', 'criado_em')
    for lead in leads:
        writer.writerow(lead)

    return response

def export_interactions_csv(request, lead_id):
    lead = get_object_or_404(Lead, pk=lead_id)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="interactions_lead_{lead_id}.csv"'

    writer = csv.writer(response)
    writer.writerow(['Lead', 'Data', 'Nota']) 

    interacoes = Interaction.objects.filter(lead=lead).values_list('lead__nome', 'data_interacao', 'nota')
    
    for interacao in interacoes:
        writer.writerow(interacao)

    return response

