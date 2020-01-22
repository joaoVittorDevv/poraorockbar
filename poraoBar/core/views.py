from django.contrib import messages
from django.db import IntegrityError
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import EmailForm
from .models import Email


def index(request):

    if request.method == 'GET':
        return new(request)
    elif request.method == 'POST':
        return create(request)

def create(request):

    form = EmailForm(request.POST)
    if not form.is_valid():
        return render(request, 'index.html', {'form': form})
    elif form.is_valid():
        try:
            Email.objects.create(**form.cleaned_data)
            messages.success(request, "Inscrição realizada com sucesso")
        except IntegrityError as e:
            return new(request)
        return HttpResponseRedirect('/')

def new(request):
    return render(request, 'index.html', {'form': EmailForm()})