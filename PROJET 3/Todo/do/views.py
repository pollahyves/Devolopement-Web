from django.shortcuts import render,redirect
from .form import FormTask
from .models import Task
from django.db.models import Sum

# Create your views here.
 
def index(request):
    form = FormTask(request.POST or None) # notre formulaire doit contenir au depart le nom de ce que on a envoyer dans le formulaire ou rien si on a encore rien envoyer dans le formulaire
    if form.is_valid():
        form.save()
    form = FormTask()
    list = Task.objects.all()
    total = Task.objects.all().aggregate(Sum('bank'))
   
    contex = {
        'form':form,
        'taches':list,
       'total':total
    }
    return render(request,'index.html',contex) 

def update(request,my_id):
    # on va recuperer un un element dans la base de donnes
    obj = Task.objects.get(id=my_id)
    # on va utiliser le formulaire
    form = FormTask(request.POST or None,instance = obj)# ici le formulaire va directement prendre linstance de object que nous venons de recuperer et on va pouvoir la modifier.bons sa ne serait plus vide comme au depart
    if form.is_valid():
        form.save()
        return redirect('acceuil')    
    # envoyer le formulaire dans la page update.html
    contex = {
        'form':form
    }
    return render(request,'update.html',contex)

def supprimer(request,my_id):
    # on va recuperer un un element dans la base de donnes
    obj = Task.objects.get(id=my_id)
    obj.delete()
    return redirect('acceuil')    
