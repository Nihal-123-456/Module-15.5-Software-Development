from django.shortcuts import render, redirect
from musician.models import *
from album.models import *

def album_list(request):
    albums = Album.objects.all()
    return render(request, 'base.html',{'albums': albums})


