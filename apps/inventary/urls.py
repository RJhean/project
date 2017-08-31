from django.conf.urls import url
from . import views

from apps.inventary.views import InventaryListView, InventaryCreateView, InventaryUpdate, InventoryDelete

app_name = 'inventary'

urlpatterns = [
  #  url(r'^$', views.index),
    url(r'^listar$', InventaryListView.as_view(), name='listar'),
    url(r'^crear$', InventaryCreateView.as_view(), name='crear'),
    url(r'^editar/(?P<pk>\d+)/$', InventaryUpdate.as_view(), name='editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', InventoryDelete.as_view(), name='eliminar'),

]
