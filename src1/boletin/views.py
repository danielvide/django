# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import RegForm

# Create your views here.
def inicio(request):
	form = RegForm()
	context= {
		"form": form,
	}
	return render(request,"inicio.html",context)