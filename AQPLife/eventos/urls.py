from django.urls import path
from . import views
app_name='eventos'
urlpatterns = [
	path('',views.IndexView.as_view(),name='index_2'),
	path('<int:user_id>/gestionar_evento', views.Gestionar_EventoDetailView.as_view(),name='gestionar_evento'),
	path('<int:evento_id>/evento',views.EventoDetailView.as_view(),name='evento'),
	path('<int:evento_id>/modificar_evento',views.ModificarEventoDetailView.as_view(),name='modificar_evento'),
	path('<int:user_id>/crear_evento',views.CrearEventoDetailView.as_view(), name='crear_evento'),
	path('<int:evento_id>/gestionar_actividad',views.Gestionar_ActividadDetailView.as_view(),name='gestionar_actividad'),
	path('<int:evento_id>/gestionar_ambiente',views.Gestionar_AmbienteDetailView.as_view(),name='gestionar_ambiente'),
	path('<int:evento_id>/gestionar_material',views.Gestionar_MaterialDetailView.as_view(),name='gestionar_material'),
	path('<int:evento_id>/gestionar_paquete',views.Gestionar_PaqueteDetailView.as_view(),name='gestionar_paquete'),
	path('<int:evento_id>/ver_evento',views.Ver_EventoDetailView.as_view(),name='ver_evento'),

]