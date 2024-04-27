from crypt import methods
from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def recepie(request):
    if request.method == 'POST':
        data = request.POST
        recipies_name = data.get('recipies_name')
        description = data.get('description')
        recipie_image = request.FILES.get('recipie_image')
        recipies.objects.create(
            recipies_name = recipies_name,
            description = description,
            recipie_image = recipie_image,
        )
        return redirect('recepie')
    return render(request, 'recepie.html')

def view(request):
    recepie = recipies.objects.all()
    context = {'recepies' : recepie}
    return render( request, 'view.html', context)


def search(request):
    if request.method == 'GET':
        queryset = recipies.objects.all()
        query = request.GET.get('search')
        print(query)
        if query:
            queryset=queryset.filter(recipies_name__icontains= query)
            context = {'recepies' : queryset}
            return render(request, 'res.html', context)
        else:
            return render(request, 'recepie.html')

def re(request):
    return HttpResponseRedirect('/recepie')