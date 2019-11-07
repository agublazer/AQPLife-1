from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
# Create your views here.
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.views import View
from django.views.generic.detail import DetailView
from .views_user import *

class IndexView(View):
	list_eventos  = Evento.objects.all()
	template_name = 'eventos/index.html'
	context={
		'eventos_list':list_eventos,

	}
	def get(self, request, *args, **kwargs):
		return render(request, self.template_name,self.context )

	def post(self, request, *args, **kwargs):
		return render(request, self.template_name,self.context)


class Gestionar_EventoDetailView(DetailView):
	template_name='eventos/gestionar_evento.html'
	def get_context_data(self, **kwargs):
		context = super(Gestionar_EventoDetailView, self).get_context_data(**kwargs)
		context['personals'] = Personal.objects.filter(profile=self.object)
		return context


	def get_object(self):
		_id=self.kwargs.get("user_id")
		return get_object_or_404(Profile,user=_id)


class EventoDetailView(DetailView):
	template_name='eventos/evento.html'
	def  get_object(self):
		_id=self.kwargs.get("evento_id")
		return get_object_or_404(Evento,id=_id)


class ModificarEventoDetailView(DetailView):
	template_name		='eventos/modificar_evento.html'
	context 			={

	}
	def get_object(self):
		_id 			=self.kwargs.get("evento_id")
		return get_object_or_404(Evento,id=_id)
		
	def get(self, request, *args, **kwargs):
		
		evento_tmp 		=get_object_or_404(Evento,id=self.kwargs.get("evento_id"))
		form 			=ModificarEventoForm(request.POST or None, instance=evento_tmp)
		self.context['form']				=form
		return render(request, self.template_name,self.context )

	def post(self, request, *args, **kwargs):
		evento_tmp 		=get_object_or_404(Evento,id=self.kwargs.get("evento_id"))
		form 			=ModificarEventoForm(request.POST or None, instance=evento_tmp)
		if form.is_valid():
			print("entro post")
			form.save()
			return redirect('eventos:evento',evento_id=self.kwargs.get("evento_id"))
		evento_tmp 		=get_object_or_404(Evento,id=self.kwargs.get("evento_id"))
		form 			=ModificarEventoForm(request.POST or None, instance=evento_tmp)
		return render(request, self.template_name,self.context)
	
class CrearEventoDetailView(DetailView):
	template_name 		='eventos/crear_evento.html'
	context   			={

	}
	def  get_object(self):
		_id=self.kwargs.get("user_id")
		return get_object_or_404(Profile,user=_id)

	def get(self, request, *args, **kwargs):
		form 								=CrearEventoForm()
		self.context['form']				=form
		return render(request, self.template_name,self.context )

	def post(self, request, *args, **kwargs):
		form  			= CrearEventoForm(request.POST)
		if form.is_valid():
			evento 		=form.save();
			personal  	=Personal.objects.create(profile_id=self.kwargs.get("user_id"),evento_id=evento.id,categoria_personal_id=1)
		return render(request, self.template_name,self.context)

class Gestionar_MaterialDetailView(DetailView):
	template_name		='eventos/gestionar_material.html'
	context 			={

	}
	def  get_object(self):
		_id=self.kwargs.get("evento_id")
		return get_object_or_404(Evento,id=_id)

class Gestionar_AmbienteDetailView(DetailView):
	template_name		='eventos/gestionar_ambiente.html'
	context 			={
	}
	
	def get(self, request, *args, **kwargs):
		evento= Evento.objects.get(pk=self.kwargs.get("evento_id"))
		self.context['evento']				=evento
		form 								=CrearAmbienteForm()
		form.fields['evento'].initial		=evento.id
		self.context['form']				=form
		return render(request, self.template_name,self.context )

	def post(self, request, *args, **kwargs):
		form  			= CrearAmbienteForm(request.POST)
		evento= Evento.objects.get(pk=self.kwargs.get("evento_id"))	
		self.context['evento']				=evento
		if form.is_valid():
			ambiente 		=form.save();
		form 								=CrearAmbienteForm()
		self.context['form']				=form
		return render(request, self.template_name,self.context)


class Gestionar_ActividadDetailView(DetailView):
	template_name		='eventos/gestionar_actividad.html'
	context 			={

	}
	def get(self, request, *args, **kwargs):
		evento= Evento.objects.get(pk=self.kwargs.get("evento_id"))
		self.context['evento']				=evento
		form 								=CrearActividadForm()
		form.fields['evento'].initial		=evento.id
		self.context['form']				=form
		return render(request, self.template_name,self.context )

	def post(self, request, *args, **kwargs):
		form  			= CrearActividadForm(request.POST)
		evento= Evento.objects.get(pk=self.kwargs.get("evento_id"))	
		self.context['evento']				=evento
		
		print(form.data['ambiente'])
		if form.is_valid():
			
			print("entro")
			form.save()
		form 								=CrearActividadForm()
		form.fields['evento'].initial		=evento.id
		self.context['form']				=form
		return render(request, self.template_name,self.context)

class Gestionar_PaqueteDetailView(DetailView):
	"""docstring for Gestionar_paqueteDetailView"""
	template_name		='eventos/gestionar_paquete.html'
	context 			={

	}
	def get(self, request, *args, **kwargs):
		evento 						=	Evento.objects.get(pk=self.kwargs.get("evento_id"))
		self.context['evento']		=	evento
		return render(request,self.template_name,self.context)



	def post(self, request, *args, **kwargs):
		pass