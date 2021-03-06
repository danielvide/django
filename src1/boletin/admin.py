# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .forms import RegModelForm
# Register your models here.
from .models import Registrado

class AdminRegistrado(admin.ModelAdmin):
	list_display = ["__unicode__","nombre","timestamp"]
	form = RegModelForm
	list_filter = ["timestamp"]
	list_editable = ["nombre"]
	search_fields = ["email","nombre"]
	#class Meta:
	#	model= Registrado

admin.site.register(Registrado,AdminRegistrado)
