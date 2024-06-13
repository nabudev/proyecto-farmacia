from django.db import models

class ObraSocial(models.Model):
    nombre= models.CharField(max_length=45)
    descuento= models.IntegerField(null=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Obras Sociales"

class Cliente (models.Model):
    dni= models.IntegerField(primary_key=True)
    apellido= models.CharField(max_length=45)
    nombre= models.CharField(max_length=45)
    domicilio= models.CharField(max_length=30)
    telefono= models.IntegerField(null=True)
    obra_social= models.ForeignKey(ObraSocial, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__ (self):
        return f'{self.apellido} {self.nombre}'
    
class CuentaParticular(models.Model):
    cliente= models.ForeignKey(Cliente, on_delete=models.CASCADE)
    saldo= models.IntegerField(null=True, blank=True)
    
    def __str__ (self):
        return f'Titular: {self.cliente}, Saldo: {self.saldo}'
    
    class Meta:
        verbose_name_plural = "Cuentas Particulares"
