
from django.urls import path
from paciente.views import *
#from pedi.views import *

urlpatterns = [
    
    
    #path('',views.home,name="Home"),
    #path('turno/',views.turno, name="turno"),
    #path('pedido/',views.pedido,name="pedido"),
    #path('reportes/',views.reportes, name="reportes"),
    #path('ventas/',views.ventas, name="ventas"),
    path('paciente/',PacienteListView.as_view,name='list_paciente'),
    path('paciente_alta/',PacienteCreateView.as_view,name='alta_paciente'),
    path('paciente_update/<int:pk>/',PacienteUpdateView.as_view,name='upadate_paciente'),
    path('paciente_delete/<int:pk>/',PacienteDeleteView.as_view,name='delete_paciente'),
]
