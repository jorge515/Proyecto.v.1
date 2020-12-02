
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.generic import ListView, CreateView,UpdateView,DeleteView
from django.utils.decorators import method_decorator
from .models import Paciente
from .forms import PacienteForm


# Create your views here.

class PacienteListView(ListView):
    Model = Paciente
    template_name = 'list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Pacientes'
        context['create_url'] = reverse_lazy('create')
        context['list_url'] = reverse_lazy('listado')
        context['entity'] = 'Paciente'
        return context

class PacienteCreateView(CreateView):
   model = Paciente
   form_class = PacienteForm
   template_name = 'create.html'
   success_url = reverse_lazy('listado')

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['title'] = 'Alta de pacientes'
       context['entity'] = 'Paciente'
       context['create_url'] = reverse_lazy('create')
       context['action'] = 'add'
       return context

class PacienteUpdateView(UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'create.html'
    success_url = reverse_lazy('listado')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar paciente'
        context['entity'] = 'Categorias'
        context['list_url'] = reverse_lazy('listado')
        context['action'] = 'edit'
        return context

class PacienteDeleteView(DeleteView):
    model = Paciente
    template_name = 'delete.html'
    success_url = reverse_lazy('listado')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de un paciente'
        context['entity'] = 'pacientes'
        context['list_url'] = reverse_lazy('listado')
        return context

    
