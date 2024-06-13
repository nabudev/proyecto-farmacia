from django.db import models
from clientes.models import Cliente
from medicamentos.models import Medicamento
# Create your models here.
class MetodoPago(models.Model):
    metodo= models.CharField(max_length=30)
    
    def __str__(self):
        return self.metodo
    
    class Meta:
        verbose_name_plural = "Metodos de pago"

class Venta(models.Model):
    cliente= models.ForeignKey(Cliente, on_delete=models.CASCADE)
    metodo_pago= models.ForeignKey(MetodoPago, on_delete=models.CASCADE)
    medicamento= models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    cantidad= models.IntegerField(null=True)
    precio_unitario= models.IntegerField(null=True)
    precio_total= models.IntegerField(null=True)
    
    def __str__(self):
        return f'{self.medicamento} - Cantidad: {self.cantidad} - Total: {self.precio_total}'
