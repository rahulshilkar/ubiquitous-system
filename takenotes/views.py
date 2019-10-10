# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Notes
from .forms import NoteForm


# Create your views here.
def index(request):
    noted = Notes.objects.all()

    context = {'noted': noted}
    return render(request, 'index.html/', context)

def add(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
        
    else:
        form = NoteForm()

    context = {'form' : form}
    return render(request, 'add.html/', context)