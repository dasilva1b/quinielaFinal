from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=130)
    clave = models.CharField(max_length=130)
    puntos = models.IntegerField()
    
    def __unicode__(self):
      return 'Nombre: "%s" Puntos: %d'%(self.nombre,self.puntos)
      
class Prediccion(models.Model):
  fase = models.CharField(max_length=130)
  equipo1 = models.CharField(max_length=130)
  equipo2 = models.CharField(max_length=130)
  gol1 = models.CharField(max_length=130)
  gol2 = models.CharField(max_length=130)
  usuario= models.CharField(max_length=130) 
  
  def __unicode__(self):
      return ' %s %s vs %s %s'%(self.equipo1,self.gol1,self.equipo2,self.gol2)