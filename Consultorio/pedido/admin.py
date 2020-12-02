from django.contrib import admin
from .models import producto,detalle,estado

# Register your models here.

admin.site.register(producto),
admin.site.register(detalle),
admin.site.register(estado),
