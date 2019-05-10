# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import RegForm

# Create your views here.
def inicio(request):
	form = RegForm(request.POST or None)
	if form.is_valid():
		form_data=form.cleaned_data
		print form_data.get("nombre")
		print form_data.get("edad")
	context= {
		"form": form,
	}
	return render(request,"inicio.html",context)