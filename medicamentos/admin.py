from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Laboratorio)
admin.site.register(CompuestoGenerico)
admin.site.register(MarcaComercial)
admin.site.register(PresentacionMedicamento)
admin.site.register(Medicamento)

