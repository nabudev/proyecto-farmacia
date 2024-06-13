from django.db import models

# Create your models here.
class Laboratorio(models.Model):
    nombre= models.CharField(max_length=45)
    
    def __str__(self):
        return self.nombre

class CompuestoGenerico(models.Model):
    nombre= models.CharField(max_length=45)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Compuestos Genericos"
    
class MarcaComercial(models.Model):
    nombre= models.CharField(max_length=45)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Marcas Comerciales"
    
class PresentacionMedicamento(models.Model):
    tipo= models.CharField(max_length=25)
    
    def __str__(self):
        return self.tipo
    
    class Meta:
        verbose_name_plural = "Presentacion del medicamento"

class Medicamento(models.Model):
    marca_comercial= models.ForeignKey(MarcaComercial, on_delete=models.CASCADE)
    compuesto_generico= models.ForeignKey(CompuestoGenerico, on_delete=models.CASCADE)
    presentacion_medicamento= models.ForeignKey(PresentacionMedicamento, on_delete=models.CASCADE)
    dosificacion= models.CharField(max_length=25)
    cantidad= models.IntegerField(null=True)
    laboratorio= models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.marca_comercial} - {self.compuesto_generico} - {self.presentacion_medicamento} - {self.dosificacion}'
