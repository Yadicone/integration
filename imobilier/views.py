from django.shortcuts import render 

from imobilier import models
from .forms  import  EmployéForm
# Create your views here.
def index(request):
    return render(request, 'index.html',)

# imobilier/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Employé
from .forms import EmployéForm

def index(request):
    return render(request, 'index.html')

def liste_employés(request):
    employés = Employé.objects.all()
    return render(request, 'liste_employés.html', {'employés': employés})

def detail_employé(request, employé_id):
    employé = get_object_or_404(Employé, id=employé_id)
    return render(request, 'detail_employé.html', {'employé': employé})

def ajout_employé(request):
    if request.method == 'POST':
        form = EmployéForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_employés')
    else:
        form = EmployéForm()
    return render(request, 'ajout_employé.html', {'form': form})

def modifier_employé(request, employé_id):
    employé = get_object_or_404(Employé, id=employé_id)
    if request.method == 'POST':
        form = EmployéForm(request.POST, instance=employé)
        if form.is_valid():
            form.save()
            return redirect('liste_employés')
    else:
        form = EmployéForm(instance=employé)
    return render(request, 'modifier_employé.html', {'form': form})

def supprimer_employé(request, employé_id):
    employé = get_object_or_404(Employé, id=employé_id)
    if request.method == 'POST':
        employé.delete()
        return redirect('liste_employés')
    return render(request, 'supprimer_employé.html', {'employé': employé})
