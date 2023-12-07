from django.shortcuts import render,redirect
from .models import *
from .forms import *

def add_musician(request):
    if request.method == 'POST':
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_musician')
    else:
        form = MusicianForm()
    return render(request, 'add_musician.html', {'form': form})

def edit_musician(request, id):
    musician = Musician.objects.get(pk=id)
    if request.method == 'POST':
        form = MusicianForm(request.POST, instance=musician)
        if form.is_valid():
            form.save()
            return redirect('add_musician')
    else:
        form = MusicianForm(instance=musician)
    return render(request, 'add_musician.html', {'form': form})

def delete_musician(request,id):
    musician = Musician.objects.get(pk=id)
    musician.delete()
    return redirect('home')