from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import AddLeadForm
from .models import Lead
# Create your views here.
@login_required
def add_lead(request):
    form = AddLeadForm()
    if request.method == 'POST':
        form = AddLeadForm(request.POST)
        if form.is_valid():
            lead = form.save(commit=False)
            lead.created_by = request.user
            lead.save()
            return redirect('home')
        else:
            form = AddLeadForm()
            return render(request, 'add_lead.html', {'form': form})

    return render(request, 'add_lead.html', {'form':form})

@login_required
def leads_list(request):
    leads = Lead.objects.filter(created_by = request.user)
    return render(request, 'leads_list.html', {'leads': leads})

@login_required
def lead_details(request,pk):
    lead = Lead.objects.get(pk=pk)

    return render(request, 'lead_details.html', {'lead': lead})

@login_required
def lead_delete(request,pk):
    lead = Lead.objects.get(pk=pk)
    lead.delete()
    messages.success(request, 'The lead has successfully been delete')
    return redirect('leads_list')

@login_required
def lead_edit(request,pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
    if request.method=='POST':
        form = AddLeadForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            messages.success(request, 'Changes saved.')
        return redirect('leads_list')
    else:
        form = AddLeadForm(instance=lead)
    return render(request, 'lead_edit.html', {'form': form})