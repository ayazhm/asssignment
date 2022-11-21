from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from .forms import *
from django.http import HttpResponseRedirect


def index(request):
    return render(request, 'main/index.html')

def type(request):
    title = 'Disease Types'
    queryset = Diseasetype.objects.all()
    context = {
        'title' : title,
        'queryset' : queryset
    }
    return render(request, 'main/diseasetype_page.html', context)

def disease(request):
    title = 'Disease'
    query = Disease.objects.all()
    context = {
        'title' : title,
        'query' : query
    }
    return render(request, 'main/disease.html', context)

def country(request):
    title = 'Country'
    query = Country.objects.all()
    context = {
        'title' : title,
        'query' : query
    }
    return render(request, 'main/country.html', context)

def users(request):
    title = 'Users'
    query = Users.objects.all()
    context = {
        'title' : title,
        'query' : query
    }
    return render(request, 'main/users.html', context)

def doctors(request):
    title = 'Doctors'
    query = Doctor.objects.all()
    context = {
        'title' : title,
        'query' : query
    }
    return render(request, 'main/doctors.html', context)

def specialize(request):
    title = 'Specialize'
    query = Specialize.objects.all()
    context = {
        'title' : title,
        'query' : query
    }
    return render(request, 'main/specialize.html', context)

def publicservant(request):
    title = 'Publicservant'
    query = Publicservant.objects.all()
    context = {
        'title' : title,
        'query' : query
    }
    return render(request, 'main/publicservants.html', context)

def discover(request):
    title = 'Discover'
    query = Discover.objects.all()
    context = {
        'title' : title,
        'query' : query
    }
    return render(request, 'main/discover.html', context)

def record(request):
    title = 'Record'
    query = Record.objects.all()
    context = {
        'title' : title,
        'query' : query
    }
    return render(request, 'main/record.html', context)

def delete_type(request, pk):
    item = Diseasetype.objects.get(id = pk)
    item.delete()
    title = 'Disease Types'
    query = Diseasetype.objects.all()
    context = {
        'title': title,
        'query': query
    }

    return redirect('../diseasetype')

def add_type(request):
    disease_type = request.POST['type_name']
    code = request.POST['type_number']

    type_info = Diseasetype(id=code, description=disease_type)
    type_info.save()

    return redirect('../diseasetype')

def update_type(request, pk):
    type = Diseasetype.objects.get(id=pk)
    form = typeForm(request.POST or None, instance=type)
    if form.is_valid():
        form.save()
        return redirect('../diseasetype')
    return render(request, 'main/update_type.html', {'type': type, 'form' : form})

def add_disease(request):
    disease_code = request.POST['code']
    pathogen = request.POST['pathogen']
    description = request.POST['description']
    type = request.POST['id']

    type_info = Disease(disease_code=disease_code, pathogen=pathogen, description=description)
    type_info.save()

    return redirect('../disease')

def update_disease(request, pk):
    type = Disease.objects.get(disease_code=pk)
    form = diseaseForm(request.POST or None, instance=type)
    if form.is_valid():
        form.save()
        return redirect('../disease')
    return render(request, 'main/update_disease.html', {'type': type, 'form' : form})

def delete_disease(request, pk):
    item = Disease.objects.get(disease_code=pk)
    item.delete()

    return redirect('../disease')

def add_country(request):
    cname = request.POST['country']
    popul = request.POST['population']

    type_info = Country(cname=cname, population=popul)
    type_info.save()

    return redirect('../country')

def delete_country(request, pk):
    item = Country.objects.get(cname=pk)
    item.delete()

    return redirect('../country')

def update_country(request, pk):
    type = Country.objects.get(cname=pk)
    form = countryForm(request.POST or None, instance=type)
    if form.is_valid():
        form.save()
        return redirect('../country')
    return render(request, 'main/update_country.html', {'type': type, 'form' : form})

def add_user(request):
    email = request.POST['email']
    name = request.POST['name']
    surname = request.POST['surname']
    phone = request.POST['phone']
    salary = request.POST['salary']

    type_info = Users(email=email, name=name, surname=surname, phone=phone, salary=salary)
    type_info.save()

    return redirect('../users')

def update_user(request, pk):
    type = Users.objects.get(email=pk)
    form = userForm(request.POST or None, instance=type)
    if form.is_valid():
        form.save()
        return redirect('../users')
    return render(request, 'main/update_user.html', {'type': type, 'form' : form})

def delete_user(request, pk):
    item = Users.objects.get(email=pk)
    item.delete()

    return redirect('../users')