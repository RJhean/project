from django.contrib import admin

from .models import Computer
from .models import Lugar
from .models import Oficina
from .models import Estado

# Register your models here.


admin.site.register(Computer)
admin.site.register(Lugar)
admin.site.register(Oficina)
admin.site.register(Estado)