from django import forms
from .models import *





class CrearEventoForm(forms.ModelForm):
	class Meta:
		model=Evento
		fields=[
			'nombre',
			'tipo_evento',
			'fecha_inicio',
			'fecha_fin'
		]
		widgets={
			'nombre':forms.TextInput(attrs={'class':'input'}),
			'tipo_evento':forms.TextInput(attrs={'class':'input'}),
			'fecha_inicio':forms.TextInput(attrs={'class':'input'}),
			'fecha_fin':forms.TextInput(attrs={'class':'input'})
		}
class CrearAmbienteForm(forms.ModelForm):
	class Meta:
		model=Ambiente
		fields=[
			'evento',
			'nombre',
			'ubicacion',
			'capacidad'
		]
		widgets={
			'evento':forms.TextInput(attrs={'class':'input', 'style':'display:none' ,'type':'hidden'	}),
			'nombre':forms.TextInput(attrs={'class':'input'}),
			'ubicacion':forms.TextInput(attrs={'class':'input'}),
			'capacidad':forms.NumberInput(attrs={'class':'input'})
		}


class ModificarEventoForm(forms.ModelForm):
	class Meta:
		model=Evento
		fields=[
			'nombre',
			'tipo_evento',
			'fecha_inicio',
			'fecha_fin'
		]
		widgets={
			'nombre':forms.TextInput(attrs={'class':'input'}),
			'tipo_evento':forms.TextInput(attrs={'class':'input'}),
			'fecha_inicio':forms.TextInput(attrs={'class':'input'}),
			'fecha_fin':forms.TextInput(attrs={'class':'input'})
		}
class CrearAmbienteForm(forms.ModelForm):
	class Meta:
		model=Ambiente
		fields=[
			'evento',
			'nombre',
			'ubicacion',
			'capacidad'
		]
		widgets={
			'evento':forms.TextInput(attrs={'class':'input', 'style':'display:none' ,'type':'hidden'	}),
			'nombre':forms.TextInput(attrs={'class':'input'}),
			'ubicacion':forms.TextInput(attrs={'class':'input'}),
			'capacidad':forms.NumberInput(attrs={'class':'input'})
		}


class CrearActividadForm(forms.ModelForm):
	class Meta:
		model=Actividad
		fields=[
			'evento',
			'ambiente',
			'nombre',
			'fecha',
			'hora_inicio',
			'hora_fin'
		]
		widgets={
			'evento':forms.TextInput(attrs={'class':'input ', 'style':'display:none' ,'type':'hidden'}),
			'ambiente':forms.TextInput(attrs={'class':'autocomplete input-field','type':'text', 'id':'autocomplete-input'}),
			'nombre':forms.TextInput(attrs={'class':'input'}),
			'fecha':forms.TextInput(attrs={'class':'input'}),
			'hora_inicio':forms.TextInput(attrs={'class':'input'}),
			'hora_fin':forms.TextInput(attrs={'class':'input'})
		}

class CrearPaqueteForm(forms.ModelForm):
	actividad			= forms.ModelMultipleChoiceField(queryset = Actividad.objects.all())

	
	class Meta:
		model=Paquete
		fields=[
				'evento',
				'nombre',
				'costo',
				'actividad',
				'descripcion'
				
			]
		widgets={
			'evento':forms.TextInput(attrs={'class':'input ', 'style':'display:none' ,'type':'hidden'}),
			
		}
	def __init__(self,*args,**kwargs):
		evento=kwargs.pop('instance_evento',None)
		super(CrearPaqueteForm, self).__init__(*args, **kwargs)
		if evento:
			self.fields['evento'].initial=evento.id
			self.fields['actividad'] = forms.ModelMultipleChoiceField(queryset=Actividad.objects.filter(evento=evento.id))

class CrearPersonalForm(forms.ModelForm):
	categoria_personal 		=forms.ModelMultipleChoiceField(queryset=CategoriaPersonal.objects.all())
	class Meta:
		model=Personal
		fields=[
			'evento',
			'profile',
			'categoria_personal'
		]
		widgets={
			'evento':forms.TextInput(attrs={'class':'input ', 'style':'display:none' ,'type':'hidden'}),
				
		}
	def __init__(self,*args,**kwargs):
		evento=kwargs.pop('instance_evento',None)
		super(CrearPersonalForm, self).__init__(*args, **kwargs)
		if evento:
			self.fields['evento'].initial=evento.id


class PreInscribirseForm(forms.ModelForm):
	paquete = forms.ModelChoiceField(queryset=Paquete.objects.all())
	class Meta:
		model=Inscrito
		fields=[
			'profile',
			'evento',
			'paquete',
			'codigo_inscripcion',
			'estado_inscripcion'
		]
		widgets={
			'profile':forms.TextInput(attrs={'class':'input ', 'style':'display:none' ,'type':'hidden'}),
			'evento':forms.TextInput(attrs={'class':'input ', 'style':'display:none' ,'type':'hidden'}),	
			'estado_inscripcion':forms.TextInput(attrs={'class':'input ', 'style':'display:none' ,'type':'hidden'}),
		}
	def __init__(self,*args,**kwargs):
		evento=kwargs.pop('instance_evento',None)
		profile=kwargs.pop('instace_profile',None)
		super(PreInscribirseForm, self).__init__(*args, **kwargs)
		if evento:
			self.fields['profile'].initial				=profile.user
			self.fields['evento'].initial				=evento.id
			self.fields['estado_inscripcion'].initial	=False
			self.fields['paquete'] 						= forms.ModelChoiceField(queryset=Paquete.objects.filter(evento=evento.id))

"""
class InscribirseForm(forms.ModelForm):
	docstring for InscribirseForm
	class Meta:
		fields=[
			'codigo'
		]
		widgets={
			'profile':forms.TextInput(attrs={'class':'input ', 'style':'display:none' ,'type':'hidden'}),
		}
		"""