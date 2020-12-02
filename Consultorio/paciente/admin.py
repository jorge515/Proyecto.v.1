from django.contrib import admin
from django.db import models
from paciente.models import Paciente,Medico,Historial,Turno,Estado

# Register your models here.

class PacienteAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=("nombre","apellido","historial")
    search_fields=("nombre","apellido")
    
class HistorialAdmin(admin.ModelAdmin):    
    list_filter=("descripcion",)

class TurnoAdmin(admin.ModelAdmin):
    list_display=("dia","hora")
    list_filter=("dia",)
    date_hierarchy=("dia")



admin.site.register(Paciente,PacienteAdmin),
admin.site.register(Medico),
admin.site.register(Historial,HistorialAdmin),
admin.site.register(Turno,TurnoAdmin),
admin.site.register(Estado)