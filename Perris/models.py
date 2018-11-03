from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class Cliente(models.Model):
	user= models.OneToOneField(User, on_delete = models.CASCADE)
	run = models.CharField('RUN',max_length=30)
	fono_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',message="Telefono debe estar en el formato correcto '+999999999'")
	fono_numero = models.CharField('Telefono',validators=[fono_regex], max_length=17, blank=True)

	def __str__(self):
		datos = {
			'run':self.user.run,
			'nombre':self.nombre,
			'apellido':self.apellido,
			'email':self.email,
			'telefono':self.telefono
		}
		return datos

class Rescatado(models.Model):
	codigo=models.AutoField(primary_key=True)
	nombre=models.CharField(max_length=30)
	raza=models.CharField(max_length=20)	
	descripcion=models.CharField(max_length=20)
	estado=models.CharField(max_length=20)

class Adopcion(models.Model):
	run=models.ForeignKey(Cliente,on_delete=models.CASCADE)
	codigo=models.ForeignKey(Rescatado,on_delete=models.CASCADE)