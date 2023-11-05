from django.shortcuts import render
from .models import Computer
from .forms import ComputerForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView

# Create your views here.
class ComputerList(ListView):
    model = Computer
    template_name = 'computers.html'
    context_object_name = 'computers'
    
class ComputerCreate(CreateView):
    model = Computer
    form_class = ComputerForm
    template_name = 'create_computer.html'
    success_url = reverse_lazy('mainpage')
    
class ComputerDelete(DeleteView):
    model = Computer
    template_name ='delete_computer.html'
    pk_url_kwarg = 'computer_id'
    success_url = reverse_lazy('mainpage')