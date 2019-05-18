# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import RegModelForm ,ContactForm
from .models import Registrado
# Create your views here.
def inicio(request):
	titulo= "que dise el tio"
	if request.user.is_authenticated():
		titulo= "Illo bienvenido %s " %(request.user)
	form = RegModelForm(request.POST or None)

	context= {
		"titulo": titulo,
		"form": form,
	}

	if form.is_valid():
		instance=form.save(commit=False)
		nombre=form.cleaned_data.get("nombre")
		email=form.cleaned_data.get("email")
		if not instance.nombre:
			instance.nombre= "Anonimo"
		instance.save()
		context = {
			"titulo": "Gracias %s " %(nombre)
		}
		if not nombre:
			context={
				"titulo": "Gracias %s " %(email)
			}
		#form_data=form.cleaned_data
		#abc=form_data.get("email")
		#abc2=form_data.get("nombre")
		#obj=Registrado.objects.create(email=abc,nombre=abc2)
		
	
	return render(request,"inicio.html",context)


def contact(request):
	form= ContactForm(request.POST or None)
	if form.is_valid():
		for key,value in form.cleaned_data.iteritems():
			print key,value
		#email= form.cleaned_data.get("email")
		#mensaje= form.cleaned_data.get("mensaje")
		#nombre= form.cleaned_data.get("nombre")
	context= {
		"form": form,
	}
	return render(request,"forms.html",context)