from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import RegisterUser
 

def crear(request):
	template_name = 'crear.html'
	context = {}
	return render(request, template_name ,context)

def descubre(request):
	template_name = 'descubre.html'
	context = {}
	return render(request,template_name,context)

def detalle(request):
	template_name = 'detallesEvento.html'
	context = {}
	return render(request,template_name,context)


class Register(View):
	def get(self, request):
		template_name = 'index.html'
		form = RegisterUser()
		context = {
			'form':form
		}
		return render(request, template_name, context)

	def post(self, request):
		form = RegisterUser(request.POST)
		if form.is_valid():
			form.save()
			return redirect('index')	
		else:
			return redirect('registro')