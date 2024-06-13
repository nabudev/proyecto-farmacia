from django.db import models
from medicamentos.models import Medicamento
# Create your models here.
class Proveedor(models.Model):
    apellido= models.CharField(max_length=45)
    nombre= models.CharField(max_length=45)
    telefono= models.IntegerField(null=True)
    direccion= models.CharField(max_length=30)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido} - Telefono: {self.telefono}'
    
    class Meta:
        verbose_name_plural = "Proveedores"
    
class StockProveedor(models.Model):
    proveedor= models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    medicamento= models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.proveedor} - {self.medicamento}'
    
    class Meta:
        verbose_name_plural = "Stock de proveedores"
