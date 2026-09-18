from django.db import models

# Create your models here.
from django.db import models

class Agente(models.Model):
    ESPECIALIDADES = [
        ('Residencial', 'Residencial'),
        ('Comercial', 'Comercial'),
        ('Industrial', 'Industrial'),
    ]

    nombre = models.CharField(max_length=150)
    especialidad = models.CharField(max_length=50, choices=ESPECIALIDADES)
    ciudad = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=5.0)
    activo_ahora = models.BooleanField(default=True)
    disponible_fin_semana = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre} - {self.especialidad}"
