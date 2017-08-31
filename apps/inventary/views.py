from django.shortcuts import render
from apps.inventary.models import Computer
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy

from apps.inventary.forms import InventoryForm

from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

#def index(request):
#    return render ( request, 'inventario/index.html')


class InventaryListView(LoginRequiredMixin,ListView):
    login_url='users:login'
    model = Computer
    template_name = "inventario/index.html"
    paginate_by=10



class InventaryCreateView(LoginRequiredMixin, CreateView):
    login_url='users:login'
    model = Computer
    form_class = InventoryForm
    template_name = "inventario/crear.html"
    success_url=reverse_lazy('inventary:listar')


class InventaryUpdate(LoginRequiredMixin, UpdateView):
    login_url='users:login'

    model = Computer
    form_class = InventoryForm
    template_name = "inventario/crear.html"
    success_url = reverse_lazy('inventary:listar')

class InventoryDelete(LoginRequiredMixin, DeleteView):
    login_url='users:login'
    model= Computer
    template_name = "inventario/eliminar.html"
    success_url = reverse_lazy('inventary:listar')



