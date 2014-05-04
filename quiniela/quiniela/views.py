from django.http import HttpResponse
import datetime
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render
from quiniApp.models import Usuario, Prediccion
   
#Constantes:
PUNTOS_RESULTADO = 2
PUNTOS_GOLES = 2
PUNTOS_FASES = 2
PUNTOS_GOLEADOR = 3
def ptosarb(request):
  user=request.POST['user']
  ptos=request.POST['ptos']
  acc=request.POST['accion']
  
  if (acc == 'sumar'):
    usu=Usuario.objects.get(nombre=user)
    usu.puntos=usu.puntos+int(ptos)
    usu.save()
  else:
    usu=Usuario.objects.get(nombre=user)
    usu.puntos=usu.puntos-int(ptos)
    usu.save()
  return render (request, 'exito.html')
  
#View que despliega la pagina de inicio del sistema
def home(request):
  gente= Usuario.objects.exclude(nombre = 'admin18183030').order_by('puntos')
  gente2=gente.reverse()
  
  return render (request,'home.html', {'gente' : gente2})
  
def guardarUsuario(request):
  nom=request.POST['nombre']
  cla=request.POST['clave']
  p= Usuario (nombre=nom, clave=cla, puntos = 0)
  p.save()
  return render (request, 'crecuenta.html')
  
def iniciarSesion(request):
  return render (request, 'iniciopersona.html')
  
def rnue(request):
  
  #Partido 1
  f1=request.POST['fase']
  e1=request.POST['equipo1']
  e2=request.POST['equipo2']
  if (request.POST['g1'] <> '') and (request.POST['g2'] <> ''):
    g1=int (request.POST['g1'])
    g2=int(request.POST['g2'])
  
    #Obtendre partidos que cumplan con ese criterio
    partidos=Prediccion.objects.filter(equipo1=e1,equipo2=e2,fase=f1)
    partidos2=Prediccion.objects.filter(equipo1=e2,equipo2=e1,fase=f1)
    #if (len(partidos2) > 0):
      #return render (request, 'inicioerroneo.html')
    
    for a in partidos:
      if (int(a.gol1) > int(a.gol2)) and (g1 > g2):
	#Obtengo al usuario.
	usu=Usuario.objects.get(nombre=a.usuario)
	usu.puntos=usu.puntos+PUNTOS_RESULTADO
	if (int(a.gol1) == g1) and (int(a.gol2) == g2):
	  usu.puntos=usu.puntos+PUNTOS_GOLES
	usu.save()
      if (int(a.gol2) > int(a.gol1)) and (g2 > g1):
	#Obtengo al usuario.
	usu=Usuario.objects.get(nombre=a.usuario)
	usu.puntos=usu.puntos+PUNTOS_RESULTADO
	if (int(a.gol1) == g1) and (int(a.gol2) == g2):
	  usu.puntos=usu.puntos+PUNTOS_GOLES
	usu.save()
      if (int(a.gol2) == int(a.gol1)) and (g2 == g1):
	#Obtengo al usuario.
	usu=Usuario.objects.get(nombre=a.usuario)
	usu.puntos=usu.puntos+PUNTOS_RESULTADO
	if (int(a.gol1) == g1) and (int(a.gol2) == g2):
	  usu.puntos=usu.puntos+PUNTOS_GOLES
	usu.save()
	
    for a in partidos2:
      if (int(a.gol1) > int(a.gol2)) and (g2 > g1):
	#Obtengo al usuario.
	usu=Usuario.objects.get(nombre=a.usuario)
	usu.puntos=usu.puntos+PUNTOS_RESULTADO
	if (int(a.gol1) == g2) and (int(a.gol2) == g1):
	  usu.puntos=usu.puntos+PUNTOS_GOLES
	usu.save()
      if (int(a.gol2) > int(a.gol1)) and (g1 > g2):
	#Obtengo al usuario.
	usu=Usuario.objects.get(nombre=a.usuario)
	usu.puntos=usu.puntos+PUNTOS_RESULTADO
	if (int(a.gol1) == g2) and (int(a.gol2) == g1):
	  usu.puntos=usu.puntos+PUNTOS_GOLES
	usu.save()
      if (int(a.gol1) == int(a.gol2)) and (g2 == g1):
	#Obtengo al usuario.
	usu=Usuario.objects.get(nombre=a.usuario)
	usu.puntos=usu.puntos+PUNTOS_RESULTADO
	if (int(a.gol1) == g2) and (int(a.gol2) == g1):
	  usu.puntos=usu.puntos+PUNTOS_GOLES
	usu.save()

	
   #Partido 2
  f1=request.POST['fase1']
  e1=request.POST['equipo11']
  e2=request.POST['equipo22']
  if (request.POST['g11'] <> '') and (request.POST['g22'] <> ''):
    g1=int (request.POST['g11'])
    g2=int(request.POST['g22'])
  
    #Obtendre partidos que cumplan con ese criterio
    partidos=Prediccion.objects.filter(equipo1=e1,equipo2=e2,fase=f1)
    partidos2=Prediccion.objects.filter(equipo1=e2,equipo2=e1,fase=f1)
    
    for a in partidos:
      if (int(a.gol1) > int(a.gol2)) and (g1 > g2):
	#Obtengo al usuario.
	usu=Usuario.objects.get(nombre=a.usuario)
	usu.puntos=usu.puntos+PUNTOS_RESULTADO
	if (int(a.gol1) == g1) and (int(a.gol2) == g2):
	  usu.puntos=usu.puntos+PUNTOS_GOLES
	usu.save()
      if (int(a.gol2) > int(a.gol1)) and (g2 > g1):
	#Obtengo al usuario.
	usu=Usuario.objects.get(nombre=a.usuario)
	usu.puntos=usu.puntos+PUNTOS_RESULTADO
	if (int(a.gol1) == g1) and (int(a.gol2) == g2):
	  usu.puntos=usu.puntos+PUNTOS_GOLES
	usu.save()
      if (int(a.gol2) == int(a.gol1)) and (g2 == g1):
	#Obtengo al usuario.
	usu=Usuario.objects.get(nombre=a.usuario)
	usu.puntos=usu.puntos+PUNTOS_RESULTADO
	if (int(a.gol1) == g1) and (int(a.gol2) == g2):
	  usu.puntos=usu.puntos+PUNTOS_GOLES
	usu.save()
	
    for a in partidos2:
      if (int(a.gol1) > int(a.gol2)) and (g2 > g1):
	#Obtengo al usuario.
	usu=Usuario.objects.get(nombre=a.usuario)
	usu.puntos=usu.puntos+PUNTOS_RESULTADO
	if (int(a.gol1) == g2) and (int(a.gol2) == g1):
	  usu.puntos=usu.puntos+PUNTOS_GOLES
	usu.save()
      if (int(a.gol2) > int(a.gol1)) and (g1 > g2):
	#Obtengo al usuario.
	usu=Usuario.objects.get(nombre=a.usuario)
	usu.puntos=usu.puntos+PUNTOS_RESULTADO
	if (int(a.gol1) == g2) and (int(a.gol2) == g1):
	  usu.puntos=usu.puntos+PUNTOS_GOLES
	usu.save()
      if (int(a.gol2) == int(a.gol1)) and (g1 == g2):
	#Obtengo al usuario.
	usu=Usuario.objects.get(nombre=a.usuario)
	usu.puntos=usu.puntos+PUNTOS_RESULTADO
	if (int(a.gol1) == g2) and (int(a.gol2) == g1):
	  usu.puntos=usu.puntos+PUNTOS_GOLES
	usu.save()
     
   #Partido 3
  f1=request.POST['fase11']
  e1=request.POST['equipo111']
  e2=request.POST['equipo222']
  if (request.POST['g111'] <> '') and (request.POST['g222'] <> ''):
    g1=int (request.POST['g111'])
    g2=int(request.POST['g222'])
  
    #Obtendre partidos que cumplan con ese criterio
    partidos=Prediccion.objects.filter(equipo1=e1,equipo2=e2,fase=f1)
    partidos2=Prediccion.objects.filter(equipo1=e2,equipo2=e1,fase=f1)
    
    for a in partidos:
      if (int(a.gol1) > int(a.gol2)) and (g1 > g2):
	#Obtengo al usuario.
	usu=Usuario.objects.get(nombre=a.usuario)
	usu.puntos=usu.puntos+PUNTOS_RESULTADO
	if (int(a.gol1) == g1) and (int(a.gol2) == g2):
	  usu.puntos=usu.puntos+PUNTOS_GOLES
	usu.save()
      if (int(a.gol2) > int(a.gol1)) and (g2 > g1):
	#Obtengo al usuario.
	usu=Usuario.objects.get(nombre=a.usuario)
	usu.puntos=usu.puntos+PUNTOS_RESULTADO
	if (int(a.gol1) == g1) and (int(a.gol2) == g2):
	  usu.puntos=usu.puntos+PUNTOS_GOLES
	usu.save()
      if (int(a.gol2) == int(a.gol1)) and (g2 == g1):
	#Obtengo al usuario.
	usu=Usuario.objects.get(nombre=a.usuario)
	usu.puntos=usu.puntos+PUNTOS_RESULTADO
	if (int(a.gol1) == g1) and (int(a.gol2) == g2):
	  usu.puntos=usu.puntos+PUNTOS_GOLES
	usu.save()
	
    for a in partidos2:
      if (int(a.gol1) > int(a.gol2)) and (g2 > g1):
	#Obtengo al usuario.
	usu=Usuario.objects.get(nombre=a.usuario)
	usu.puntos=usu.puntos+PUNTOS_RESULTADO
	if (int(a.gol1) == g2) and (int(a.gol2) == g1):
	  usu.puntos=usu.puntos+PUNTOS_GOLES
	usu.save()
      if (int(a.gol2) > int(a.gol1)) and (g1 > g2):
	#Obtengo al usuario.
	usu=Usuario.objects.get(nombre=a.usuario)
	usu.puntos=usu.puntos+PUNTOS_RESULTADO
	if (int(a.gol1) == g2) and (int(a.gol2) == g1):
	  usu.puntos=usu.puntos+PUNTOS_GOLES
	usu.save()
      if (int(a.gol2) == int(a.gol1)) and (g1 == g2):
	#Obtengo al usuario.
	usu=Usuario.objects.get(nombre=a.usuario)
	usu.puntos=usu.puntos+PUNTOS_RESULTADO
	if (int(a.gol1) == g2) and (int(a.gol2) == g1):
	  usu.puntos=usu.puntos+PUNTOS_GOLES
	usu.save()
	
  #Partido 4
  f1=request.POST['fase111']
  e1=request.POST['equipo1111']
  e2=request.POST['equipo2222']
  if (request.POST['g1111'] <> '') and (request.POST['g2222'] <> ''):
    g1=int (request.POST['g1111'])
    g2=int(request.POST['g2222'])
  
    #Obtendre partidos que cumplan con ese criterio
    partidos=Prediccion.objects.filter(equipo1=e1,equipo2=e2,fase=f1)
    partidos2=Prediccion.objects.filter(equipo1=e2,equipo2=e1,fase=f1)
    
    for a in partidos:
      if (int(a.gol1) > int(a.gol2)) and (g1 > g2):
	#Obtengo al usuario.
	usu=Usuario.objects.get(nombre=a.usuario)
	usu.puntos=usu.puntos+PUNTOS_RESULTADO
	if (int(a.gol1) == g1) and (int(a.gol2) == g2):
	  usu.puntos=usu.puntos+PUNTOS_GOLES
	usu.save()
      if (int(a.gol2) > int(a.gol1)) and (g2 > g1):
	#Obtengo al usuario.
	usu=Usuario.objects.get(nombre=a.usuario)
	usu.puntos=usu.puntos+PUNTOS_RESULTADO
	if (int(a.gol1) == g1) and (int(a.gol2) == g2):
	  usu.puntos=usu.puntos+PUNTOS_GOLES
	usu.save()
      if (int(a.gol2) == int(a.gol1)) and (g2 == g1):
	#Obtengo al usuario.
	usu=Usuario.objects.get(nombre=a.usuario)
	usu.puntos=usu.puntos+PUNTOS_RESULTADO
	if (int(a.gol1) == g1) and (int(a.gol2) == g2):
	  usu.puntos=usu.puntos+PUNTOS_GOLES
	usu.save()
	
    for a in partidos2:
      if (int(a.gol1) > int(a.gol2)) and (g2 > g1):
	#Obtengo al usuario.
	usu=Usuario.objects.get(nombre=a.usuario)
	usu.puntos=usu.puntos+PUNTOS_RESULTADO
	if (int(a.gol1) == g2) and (int(a.gol2) == g1):
	  usu.puntos=usu.puntos+PUNTOS_GOLES
	usu.save()
      if (int(a.gol2) > int(a.gol1)) and (g1 > g2):
	#Obtengo al usuario.
	usu=Usuario.objects.get(nombre=a.usuario)
	usu.puntos=usu.puntos+PUNTOS_RESULTADO
	if (int(a.gol1) == g2) and (int(a.gol2) == g1):
	  usu.puntos=usu.puntos+PUNTOS_GOLES
	usu.save()
      if (int(a.gol2) == int(a.gol1)) and (g1 == g2):
	#Obtengo al usuario.
	usu=Usuario.objects.get(nombre=a.usuario)
	usu.puntos=usu.puntos+PUNTOS_RESULTADO
	if (int(a.gol1) == g2) and (int(a.gol2) == g1):
	  usu.puntos=usu.puntos+PUNTOS_GOLES
	usu.save()
	
  #Partido Final
  f1=request.POST['faseFinal']
  e1=request.POST['equipoFinal']
  e2=request.POST['equipoFinal2']
  campeone=request.POST['campeoeo']
  if (request.POST['g1Final'] <> '') and (request.POST['g2Final'] <> ''):
    g1=int (request.POST['g1Final'])
    g2=int(request.POST['g2Final'])
  
    #Obtendre partidos que cumplan con ese criterio
    partidos=Prediccion.objects.filter(equipo1=e1,equipo2=e2,fase=f1)
    partidos2=Prediccion.objects.filter(equipo1=e2,equipo2=e1,fase=f1)
    for a in partidos:
      if (int(a.gol1) > int(a.gol2)) and (g1 > g2):
	#Obtengo al usuario.
	usu=Usuario.objects.get(nombre=a.usuario)
	usu.puntos=usu.puntos+PUNTOS_RESULTADO
	if (int(a.gol1) == g1) and (int(a.gol2) == g2):
	  usu.puntos=usu.puntos+PUNTOS_GOLES
	usu.save()
      if (int(a.gol2) > int(a.gol1)) and (g2 > g1):
	#Obtengo al usuario.
	usu=Usuario.objects.get(nombre=a.usuario)
	usu.puntos=usu.puntos+PUNTOS_RESULTADO
	if (int(a.gol1) == g1) and (int(a.gol2) == g2):
	  usu.puntos=usu.puntos+PUNTOS_GOLES
	usu.save()
      if (int(a.gol2) == int(a.gol1)) and (g2 == g1):
	#Obtengo al usuario.
	usu=Usuario.objects.get(nombre=a.usuario)
	
	#Veo si pego el campeon a pesar de sumar empate:
	campeon=Prediccion.objects.get(fase='finalCampeoeo')
	campeon=campeon.equipo1
	if (campeone == campeon):
	  usu.puntos=usu.puntos+PUNTOS_RESULTADO
	
	if (int(a.gol1) == g1) and (int(a.gol2) == g2):
	  usu.puntos=usu.puntos+PUNTOS_GOLES
	usu.save()
	
    for a in partidos2:
      if (int(a.gol1) > int(a.gol2)) and (g2 > g1):
	#Obtengo al usuario.
	usu=Usuario.objects.get(nombre=a.usuario)
	usu.puntos=usu.puntos+PUNTOS_RESULTADO
	if (int(a.gol1) == g2) and (int(a.gol2) == g1):
	  usu.puntos=usu.puntos+PUNTOS_GOLES
	usu.save()
      if (int(a.gol2) > int(a.gol1)) and (g1 > g2):
	#Obtengo al usuario.
	usu=Usuario.objects.get(nombre=a.usuario)
	usu.puntos=usu.puntos+PUNTOS_RESULTADO
	if (int(a.gol1) == g2) and (int(a.gol2) == g1):
	  usu.puntos=usu.puntos+PUNTOS_GOLES
	usu.save()
      if (int(a.gol2) == int(a.gol1)) and (g1 == g2):
	#Obtengo al usuario.
	usu=Usuario.objects.get(nombre=a.usuario)
	#Veo si pego el campeon a pesar de sumar empate:
	campeon=Prediccion.objects.get(fase='finalCampeoeo')
	campeon=campeon.equipo1
	if (campeone == campeon):
	  usu.puntos=usu.puntos+PUNTOS_RESULTADO
	if (int(a.gol1) == g2) and (int(a.gol2) == g1):
	  usu.puntos=usu.puntos+PUNTOS_GOLES
	usu.save()
	
  #Partido de Tercero
  f1=request.POST['faseTercero']
  e1=request.POST['equipoTercero']
  e2=request.POST['equipoTercero2']
  campeone=request.POST['terceoeo']
  if (request.POST['g1Tercero'] <> '') and (request.POST['g2Tercero'] <> ''):
    g1=int (request.POST['g1Tercero'])
    g2=int(request.POST['g2Tercero'])
  
    #Obtendre partidos que cumplan con ese criterio
    partidos=Prediccion.objects.filter(equipo1=e1,equipo2=e2,fase=f1)
    partidos2=Prediccion.objects.filter(equipo1=e2,equipo2=e1,fase=f1)
    for a in partidos:
      if (int(a.gol1) > int(a.gol2)) and (g1 > g2):
	#Obtengo al usuario.
	usu=Usuario.objects.get(nombre=a.usuario)
	usu.puntos=usu.puntos+PUNTOS_RESULTADO
	if (int(a.gol1) == g1) and (int(a.gol2) == g2):
	  usu.puntos=usu.puntos+PUNTOS_GOLES
	usu.save()
      if (int(a.gol2) > int(a.gol1)) and (g2 > g1):
	#Obtengo al usuario.
	usu=Usuario.objects.get(nombre=a.usuario)
	usu.puntos=usu.puntos+PUNTOS_RESULTADO
	if (int(a.gol1) == g1) and (int(a.gol2) == g2):
	  usu.puntos=usu.puntos+PUNTOS_GOLES
	usu.save()
      if (int(a.gol2) == int(a.gol1)) and (g2 == g1):
	#Obtengo al usuario.
	usu=Usuario.objects.get(nombre=a.usuario)
	
	#Veo si pego el campeon a pesar de sumar empate:
	campeon=Prediccion.objects.get(fase='terceroterceoeo')
	campeon=campeon.equipo1
	if (campeone == campeon):
	  usu.puntos=usu.puntos+PUNTOS_RESULTADO
	
	if (int(a.gol1) == g1) and (int(a.gol2) == g2):
	  usu.puntos=usu.puntos+PUNTOS_GOLES
	usu.save()
	
    for a in partidos2:
      if (int(a.gol1) > int(a.gol2)) and (g2 > g1):
	#Obtengo al usuario.
	usu=Usuario.objects.get(nombre=a.usuario)
	usu.puntos=usu.puntos+PUNTOS_RESULTADO
	if (int(a.gol1) == g2) and (int(a.gol2) == g1):
	  usu.puntos=usu.puntos+PUNTOS_GOLES
	usu.save()
      if (int(a.gol2) > int(a.gol1)) and (g1 > g2):
	#Obtengo al usuario.
	usu=Usuario.objects.get(nombre=a.usuario)
	usu.puntos=usu.puntos+PUNTOS_RESULTADO
	if (int(a.gol1) == g2) and (int(a.gol2) == g1):
	  usu.puntos=usu.puntos+PUNTOS_GOLES
	usu.save()
      if (int(a.gol2) == int(a.gol1)) and (g1 == g2):
	#Obtengo al usuario.
	usu=Usuario.objects.get(nombre=a.usuario)
	#Veo si pego el campeon a pesar de sumar empate:
	campeon=Prediccion.objects.get(fase='terceroterceoeo')
	campeon=campeon.equipo1
	if (campeone == campeon):
	  usu.puntos=usu.puntos+PUNTOS_RESULTADO
	if (int(a.gol1) == g2) and (int(a.gol2) == g1):
	  usu.puntos=usu.puntos+PUNTOS_GOLES
	usu.save()
    
    
  return render (request, 'exito.html')
  
def rnue2(request):
  e1=request.POST['equipo1']
  e2=request.POST['equipo2']
  e3=request.POST['equipo3']
  e4=request.POST['equipo4']
  e5=request.POST['equipo5']
  e6=request.POST['equipo6']
  e7=request.POST['equipo7']
  e8=request.POST['equipo8']
  
  e9=request.POST['equipo9']
  e10=request.POST['equipo10']
  e11=request.POST['equipo11']
  e12=request.POST['equipo12']
  e13=request.POST['equipo13']
  e14=request.POST['equipo14']
  e15=request.POST['equipo15']
  e16=request.POST['equipo16']
  
  temp=Prediccion.objects.filter(fase = 'octavos', equipo1 = e1)
  temp2=Prediccion.objects.filter(fase='octavos', equipo2 = e1)
  
  for a in temp:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
  for a in temp2:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
    
  temp=Prediccion.objects.filter(fase = 'octavos', equipo1 = e2)
  temp2=Prediccion.objects.filter(fase='octavos', equipo2 = e2)
  
  for a in temp:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
  for a in temp2:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
    
  temp=Prediccion.objects.filter(fase = 'octavos', equipo1 = e3)
  temp2=Prediccion.objects.filter(fase='octavos', equipo2 = e3)
  
  for a in temp:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
  for a in temp2:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save() 
    
  
  temp=Prediccion.objects.filter(fase = 'octavos', equipo1 = e4)
  temp2=Prediccion.objects.filter(fase='octavos', equipo2 = e4)
  
  for a in temp:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
  for a in temp2:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
  
  
  temp=Prediccion.objects.filter(fase = 'octavos', equipo1 = e5)
  temp2=Prediccion.objects.filter(fase='octavos', equipo2 = e5)
  
  for a in temp:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
  for a in temp2:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
  
  
  temp=Prediccion.objects.filter(fase = 'octavos', equipo1 = e6)
  temp2=Prediccion.objects.filter(fase='octavos', equipo2 = e6)
  
  for a in temp:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
  for a in temp2:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
  
  
  temp=Prediccion.objects.filter(fase = 'octavos', equipo1 = e7)
  temp2=Prediccion.objects.filter(fase='octavos', equipo2 = e7)
  
  for a in temp:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
  for a in temp2:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
  
  
  temp=Prediccion.objects.filter(fase = 'octavos', equipo1 = e8)
  temp2=Prediccion.objects.filter(fase='octavos', equipo2 = e8)
  
  for a in temp:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
  for a in temp2:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
  
  temp=Prediccion.objects.filter(fase = 'octavos', equipo1 = e9)
  temp2=Prediccion.objects.filter(fase='octavos', equipo2 = e9)
  
  for a in temp:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
  for a in temp2:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
  
  temp=Prediccion.objects.filter(fase = 'octavos', equipo1 = e10)
  temp2=Prediccion.objects.filter(fase='octavos', equipo2 = e10)
  
  for a in temp:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
  for a in temp2:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
  
  
  temp=Prediccion.objects.filter(fase = 'octavos', equipo1 = e11)
  temp2=Prediccion.objects.filter(fase='octavos', equipo2 = e11)
  
  for a in temp:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
  for a in temp2:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
  
  
  temp=Prediccion.objects.filter(fase = 'octavos', equipo1 = e12)
  temp2=Prediccion.objects.filter(fase='octavos', equipo2 = e12)
  
  for a in temp:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
  for a in temp2:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
  
  temp=Prediccion.objects.filter(fase = 'octavos', equipo1 = e13)
  temp2=Prediccion.objects.filter(fase='octavos', equipo2 = e13)
  
  for a in temp:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
  for a in temp2:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
  
  temp=Prediccion.objects.filter(fase = 'octavos', equipo1 = e14)
  temp2=Prediccion.objects.filter(fase='octavos', equipo2 = e14)
  
  for a in temp:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
  for a in temp2:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
  
  temp=Prediccion.objects.filter(fase = 'octavos', equipo1 = e16)
  temp2=Prediccion.objects.filter(fase='octavos', equipo2 = e16)
  
  for a in temp:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
  for a in temp2:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
  
  temp=Prediccion.objects.filter(fase = 'octavos', equipo1 = e15)
  temp2=Prediccion.objects.filter(fase='octavos', equipo2 = e15)
  
  for a in temp:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
  for a in temp2:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
  
  return render (request, 'exito.html')

def rnue3(request):
  e1=request.POST['equipo1']
  e2=request.POST['equipo2']
  e3=request.POST['equipo3']
  e4=request.POST['equipo4']
  e5=request.POST['equipo5']
  e6=request.POST['equipo6']
  e7=request.POST['equipo7']
  e8=request.POST['equipo8']
  
  
  temp=Prediccion.objects.filter(fase = 'cuartos', equipo1 = e1)
  temp2=Prediccion.objects.filter(fase='cuartos', equipo2 = e1)
  
  for a in temp:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
  for a in temp2:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
    
  temp=Prediccion.objects.filter(fase = 'cuartos', equipo1 = e2)
  temp2=Prediccion.objects.filter(fase='cuartos', equipo2 = e2)
  
  for a in temp:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
  for a in temp2:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
    
  temp=Prediccion.objects.filter(fase = 'cuartos', equipo1 = e3)
  temp2=Prediccion.objects.filter(fase='cuartos', equipo2 = e3)
  
  for a in temp:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
  for a in temp2:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save() 
    
  
  temp=Prediccion.objects.filter(fase = 'cuartos', equipo1 = e4)
  temp2=Prediccion.objects.filter(fase='cuartos', equipo2 = e4)
  
  for a in temp:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
  for a in temp2:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
  
  
  temp=Prediccion.objects.filter(fase = 'cuartos', equipo1 = e5)
  temp2=Prediccion.objects.filter(fase='cuartos', equipo2 = e5)
  
  for a in temp:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
  for a in temp2:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
  
  
  temp=Prediccion.objects.filter(fase = 'cuartos', equipo1 = e6)
  temp2=Prediccion.objects.filter(fase='cuartos', equipo2 = e6)
  
  for a in temp:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
  for a in temp2:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
  
  
  temp=Prediccion.objects.filter(fase = 'cuartos', equipo1 = e7)
  temp2=Prediccion.objects.filter(fase='cuartos', equipo2 = e7)
  
  for a in temp:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
  for a in temp2:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
  
  
  temp=Prediccion.objects.filter(fase = 'cuartos', equipo1 = e8)
  temp2=Prediccion.objects.filter(fase='cuartos', equipo2 = e8)
  
  for a in temp:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
  for a in temp2:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
  return render (request, 'exito.html')
  
def rnue4(request):
  e1=request.POST['equipo1']
  e2=request.POST['equipo2']
  e3=request.POST['equipo3']
  e4=request.POST['equipo4']
  
  
  temp=Prediccion.objects.filter(fase = 'semis', equipo1 = e1)
  temp2=Prediccion.objects.filter(fase='semis', equipo2 = e1)
  
  for a in temp:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
  for a in temp2:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
    
  temp=Prediccion.objects.filter(fase = 'semis', equipo1 = e2)
  temp2=Prediccion.objects.filter(fase='semis', equipo2 = e2)
  
  for a in temp:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
  for a in temp2:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
    
  temp=Prediccion.objects.filter(fase = 'semis', equipo1 = e3)
  temp2=Prediccion.objects.filter(fase='semis', equipo2 = e3)
  
  for a in temp:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
  for a in temp2:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save() 
    
  
  temp=Prediccion.objects.filter(fase = 'semis', equipo1 = e4)
  temp2=Prediccion.objects.filter(fase='semis', equipo2 = e4)
  
  for a in temp:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
  for a in temp2:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
    
  return render (request, 'exito.html')
  
def rnue5(request):
  e1=request.POST['equipo1']
  e2=request.POST['equipo2']
  
  
  temp=Prediccion.objects.filter(fase = 'final', equipo1 = e1)
  temp2=Prediccion.objects.filter(fase='final', equipo2 = e1)
  
  for a in temp:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
  for a in temp2:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
    
  temp=Prediccion.objects.filter(fase = 'final', equipo1 = e2)
  temp2=Prediccion.objects.filter(fase='final', equipo2 = e2)
  
  for a in temp:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
  for a in temp2:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
     
  return render (request, 'exito.html')
  
def rnue7(request):
  e1=request.POST['equipo1']
  e2=request.POST['equipo2']
  
  
  temp=Prediccion.objects.filter(fase = 'tercero', equipo1 = e1)
  temp2=Prediccion.objects.filter(fase='tercero', equipo2 = e1)
  
  for a in temp:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
  for a in temp2:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
    
  temp=Prediccion.objects.filter(fase = 'tercero', equipo1 = e2)
  temp2=Prediccion.objects.filter(fase='tercero', equipo2 = e2)
  
  for a in temp:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
  for a in temp2:
    usu=Usuario.objects.get(nombre = a.usuario)
    usu.puntos=usu.puntos+PUNTOS_FASES
    usu.save()
     
  return render (request, 'exito.html')

def rnue6(request):
  gole= request.POST['goleador'].lower()
  tt=Prediccion.objects.filter(fase='goleador')
  for a in tt:
    if (a.equipo1 == gole):
      usu=Usuario.objects.get(nombre = a.usuario)
      usu.puntos = usu.puntos+PUNTOS_GOLEADOR
      usu.save()
  return render (request, 'exito.html')
  
  
def admine(request):
  nom=request.POST['nombre']
  cla=request.POST['clave']
  if (nom == 'admin18183030'):
    lista=Usuario.objects.filter(nombre = nom, clave = cla)
    if (len(lista) > 0):
      return render (request, 'admin.html')
  else:
    return render (request, 'inicioerroneo.html')
  
def verp(request):
  nom=request.POST['nombre']
  prg= Prediccion.objects.filter(usuario = nom)
  campeon= Prediccion.objects.filter(usuario = nom, fase = 'finalCampeoeo')[0]
  campeon2= Prediccion.objects.filter(usuario = nom, fase = 'final')[0]
  e1=campeon.equipo1
  e2=campeon2.equipo1
  e3=campeon2.equipo2
  champ=e1
  if (e1 <> e2):
    subchamp=e2
  else:
    subchamp=e3
  grupos=Prediccion.objects.filter(usuario = nom, fase = 'grupos')
  octavos=Prediccion.objects.filter(usuario = nom, fase = 'octavos')
  cuartos=Prediccion.objects.filter(usuario = nom, fase = 'cuartos')
  semis= Prediccion.objects.filter(usuario = nom, fase = 'semis')
  goleador1= Prediccion.objects.filter(usuario= nom, fase = 'goleador')
  goleador1=goleador1[0].equipo1
  tercero=Prediccion.objects.filter(usuario = nom, fase = 'tercero')
  return render (request, 'vistaprediccs.html', {'pre' : prg, 'campe':champ, 'subcampe':subchamp, 'grupos':grupos, 'oct':octavos, 'semis':semis
		, 'cuar':cuartos, 'gole':goleador1, 'terc':tercero})
  
def casosEspeciales(pais):
  if ((pais == 'costa rica')):
    return 'costarica'
  if ((pais == 'costa de marfil')):
    return 'costademarfil'
  if ((pais == 'brasil')):
    return 'brazil'
  else:
    return pais
  
def procesar(request):
  usuario2=request.POST['nombre']
  clave2=request.POST['clave']
  
  lista= Usuario.objects.filter( nombre = usuario2, clave = clave2)
  if (len(lista) > 0 ):
    # Fase de grupos
    
    #Grupo A
    br=request.POST['Brazil'].lower()
    cr=request.POST['Croacia'].lower()
    brg=request.POST['BrazilGol'].lower()
    crg=request.POST['CroaciaGol'].lower()
    pr= Prediccion (fase = 'grupos', equipo1=br, equipo2=cr, gol1=brg, gol2=crg, usuario=usuario2)
    pr.save()
    
    me=request.POST['Mexico'].lower()
    ca=request.POST['Camerun'].lower()
    meg=request.POST['MexicoGol'].lower()
    cag=request.POST['CamerunGol'].lower()
    pr2= Prediccion (fase = 'grupos', equipo1=me, equipo2=ca, gol1=meg, gol2=cag, usuario=usuario2)
    pr2.save()
    
    
    me=request.POST['Brazil/1'].lower()
    ca=request.POST['Mexico/1'].lower()
    meg=request.POST['BrazilGol/1'].lower()
    cag=request.POST['MexicoGol/1'].lower()
    pr3= Prediccion (fase = 'grupos', equipo1=me, equipo2=ca, gol1=meg, gol2=cag, usuario=usuario2)
    pr3.save()
    
    me=request.POST['Camerun/1'].lower()
    ca=request.POST['Croacia/1'].lower()
    meg=request.POST['CamerunGol/1'].lower()
    cag=request.POST['CroaciaGol/1'].lower()
    pr4= Prediccion (fase = 'grupos', equipo1=me, equipo2=ca, gol1=meg, gol2=cag, usuario=usuario2)
    pr4.save()
    
    me=request.POST['Camerun/2'].lower()
    ca=request.POST['Brazil/2'].lower()
    meg=request.POST['CamerunGol/2'].lower()
    cag=request.POST['BrazilGol/2'].lower()
    pr5= Prediccion (fase = 'grupos', equipo1=me, equipo2=ca, gol1=meg, gol2=cag, usuario=usuario2)
    pr5.save()
    
    me=request.POST['Croacia/2'].lower()
    ca=request.POST['Mexico/2'].lower()
    meg=request.POST['CroaciaGol/2'].lower()
    cag=request.POST['MexicoGol/2'].lower()
    pr6= Prediccion (fase = 'grupos', equipo1=me, equipo2=ca, gol1=meg, gol2=cag, usuario=usuario2)
    pr6.save()
    
    #Grupo B
    br=request.POST['Espana'].lower()
    cr=request.POST['Holanda'].lower()
    brg=request.POST['EspanaGol'].lower()
    crg=request.POST['HolandaGol'].lower()
    pr= Prediccion (fase = 'grupos', equipo1=br, equipo2=cr, gol1=brg, gol2=crg, usuario=usuario2)
    pr.save()
    
    me=request.POST['Chile'].lower()
    ca=request.POST['Australia'].lower()
    meg=request.POST['ChileGol'].lower()
    cag=request.POST['AustraliaGol'].lower()
    pr2= Prediccion (fase = 'grupos', equipo1=me, equipo2=ca, gol1=meg, gol2=cag, usuario=usuario2)
    pr2.save()
    
    me=request.POST['Espana/1'].lower()
    ca=request.POST['Chile/1'].lower()
    meg=request.POST['EspanaGol/1'].lower()
    cag=request.POST['ChileGol/1'].lower()
    pr2= Prediccion (fase = 'grupos', equipo1=me, equipo2=ca, gol1=meg, gol2=cag, usuario=usuario2)
    pr2.save()
    
    me=request.POST['Australia/1'].lower()
    ca=request.POST['Holanda/1'].lower()
    meg=request.POST['AustraliaGol/1'].lower()
    cag=request.POST['HolandaGol/1'].lower()
    pr3= Prediccion (fase = 'grupos', equipo1=me, equipo2=ca, gol1=meg, gol2=cag, usuario=usuario2)
    pr3.save()
    
    me=request.POST['Australia/2'].lower()
    ca=request.POST['Espana/2'].lower()
    meg=request.POST['AustraliaGol/2'].lower()
    cag=request.POST['EspanaGol/2'].lower()
    pr4= Prediccion (fase = 'grupos', equipo1=me, equipo2=ca, gol1=meg, gol2=cag, usuario=usuario2)
    pr4.save()
    
    me=request.POST['Holanda/2'].lower()
    ca=request.POST['Chile/2'].lower()
    meg=request.POST['HolandaGol/2'].lower()
    cag=request.POST['ChileGol/2'].lower()
    pr5= Prediccion (fase = 'grupos', equipo1=me, equipo2=ca, gol1=meg, gol2=cag, usuario=usuario2)
    pr5.save()
    
    #Grupo C
    br=request.POST['Colombia'].lower()
    cr=request.POST['Grecia'].lower()
    brg=request.POST['ColombiaGol'].lower()
    crg=request.POST['GreciaGol'].lower()
    pr= Prediccion (fase = 'grupos', equipo1=br, equipo2=cr, gol1=brg, gol2=crg, usuario=usuario2)
    pr.save()
    
    me=request.POST['CostaDeMarfil'].lower()
    ca=request.POST['Japon'].lower()
    meg=request.POST['CostaDeMarfilGol'].lower()
    cag=request.POST['JaponGol'].lower()
    pr2= Prediccion (fase = 'grupos', equipo1=me, equipo2=ca, gol1=meg, gol2=cag, usuario=usuario2)
    pr2.save()
    
    me=request.POST['Colombia/1'].lower()
    ca=request.POST['CostaDeMarfil/1'].lower()
    meg=request.POST['ColombiaGol/1'].lower()
    cag=request.POST['CostaDeMarfilGol/1'].lower()
    pr2= Prediccion (fase = 'grupos', equipo1=me, equipo2=ca, gol1=meg, gol2=cag, usuario=usuario2)
    pr2.save()
    
    me=request.POST['Japon/1'].lower()
    ca=request.POST['Grecia/1'].lower()
    meg=request.POST['JaponGol/1'].lower()
    cag=request.POST['GreciaGol/1'].lower()
    pr3= Prediccion (fase = 'grupos', equipo1=me, equipo2=ca, gol1=meg, gol2=cag, usuario=usuario2)
    pr3.save()
    
    me=request.POST['Japon/2'].lower()
    ca=request.POST['Colombia/2'].lower()
    meg=request.POST['JaponGol/2'].lower()
    cag=request.POST['ColombiaGol/2'].lower()
    pr4= Prediccion (fase = 'grupos', equipo1=me, equipo2=ca, gol1=meg, gol2=cag, usuario=usuario2)
    pr4.save()
    
    me=request.POST['Grecia/2'].lower()
    ca=request.POST['CostaDeMarfil/2'].lower()
    meg=request.POST['GreciaGol/2'].lower()
    cag=request.POST['CostaDeMarfilGol/2'].lower()
    pr5= Prediccion (fase = 'grupos', equipo1=me, equipo2=ca, gol1=meg, gol2=cag, usuario=usuario2)
    pr5.save()
    
    #Grupo D
    br=request.POST['Uruguay'].lower()
    cr=request.POST['CostaRica'].lower()
    brg=request.POST['UruguayGol'].lower()
    crg=request.POST['CostaRicaGol'].lower()
    pr= Prediccion (fase = 'grupos', equipo1=br, equipo2=cr, gol1=brg, gol2=crg, usuario=usuario2)
    pr.save()
    
    me=request.POST['Inglaterra'].lower()
    ca=request.POST['Italia'].lower()
    meg=request.POST['InglaterraGol'].lower()
    cag=request.POST['ItaliaGol'].lower()
    pr2= Prediccion (fase = 'grupos', equipo1=me, equipo2=ca, gol1=meg, gol2=cag, usuario=usuario2)
    pr2.save()
    
    me=request.POST['Uruguay/1'].lower()
    ca=request.POST['Inglaterra/1'].lower()
    meg=request.POST['UruguayGol/1'].lower()
    cag=request.POST['InglaterraGol/1'].lower()
    pr2= Prediccion (fase = 'grupos', equipo1=me, equipo2=ca, gol1=meg, gol2=cag, usuario=usuario2)
    pr2.save()
    
    me=request.POST['Italia/1'].lower()
    ca=request.POST['CostaRica/1'].lower()
    meg=request.POST['ItaliaGol/1'].lower()
    cag=request.POST['CostaRicaGol/1'].lower()
    pr3= Prediccion (fase = 'grupos', equipo1=me, equipo2=ca, gol1=meg, gol2=cag, usuario=usuario2)
    pr3.save()
    
    me=request.POST['Italia/2'].lower()
    ca=request.POST['Uruguay/2'].lower()
    meg=request.POST['ItaliaGol/2'].lower()
    cag=request.POST['UruguayGol/2'].lower()
    pr4= Prediccion (fase = 'grupos', equipo1=me, equipo2=ca, gol1=meg, gol2=cag, usuario=usuario2)
    pr4.save()
    
    me=request.POST['CostaRica/2'].lower()
    ca=request.POST['Inglaterra/2'].lower()
    meg=request.POST['CostaRicaGol/2'].lower()
    cag=request.POST['InglaterraGol/2'].lower()
    pr5= Prediccion (fase = 'grupos', equipo1=me, equipo2=ca, gol1=meg, gol2=cag, usuario=usuario2)
    pr5.save()
    
    #Grupo E
    br=request.POST['Suiza'].lower()
    cr=request.POST['Ecuador'].lower()
    brg=request.POST['SuizaGol'].lower()
    crg=request.POST['EcuadorGol'].lower()
    pr= Prediccion (fase = 'grupos', equipo1=br, equipo2=cr, gol1=brg, gol2=crg, usuario=usuario2)
    pr.save()
    
    me=request.POST['Francia'].lower()
    ca=request.POST['Honduras'].lower()
    meg=request.POST['FranciaGol'].lower()
    cag=request.POST['HondurasGol'].lower()
    pr2= Prediccion (fase = 'grupos', equipo1=me, equipo2=ca, gol1=meg, gol2=cag, usuario=usuario2)
    pr2.save()
    
    me=request.POST['Suiza/1'].lower()
    ca=request.POST['Francia/1'].lower()
    meg=request.POST['SuizaGol/1'].lower()
    cag=request.POST['FranciaGol/1'].lower()
    pr2= Prediccion (fase = 'grupos', equipo1=me, equipo2=ca, gol1=meg, gol2=cag, usuario=usuario2)
    pr2.save()
    
    me=request.POST['Honduras/1'].lower()
    ca=request.POST['Ecuador/1'].lower()
    meg=request.POST['HondurasGol/1'].lower()
    cag=request.POST['EcuadorGol/1'].lower()
    pr3= Prediccion (fase = 'grupos', equipo1=me, equipo2=ca, gol1=meg, gol2=cag, usuario=usuario2)
    pr3.save()
    
    me=request.POST['Honduras/2'].lower()
    ca=request.POST['Suiza/2'].lower()
    meg=request.POST['HondurasGol/2'].lower()
    cag=request.POST['SuizaGol/2'].lower()
    pr4= Prediccion (fase = 'grupos', equipo1=me, equipo2=ca, gol1=meg, gol2=cag, usuario=usuario2)
    pr4.save()
    
    me=request.POST['Ecuador/2'].lower()
    ca=request.POST['Francia/2'].lower()
    meg=request.POST['EcuadorGol/2'].lower()
    cag=request.POST['FranciaGol/2'].lower()
    pr5= Prediccion (fase = 'grupos', equipo1=me, equipo2=ca, gol1=meg, gol2=cag, usuario=usuario2)
    pr5.save()
    
    #Grupo F
    br=request.POST['Argentina'].lower()
    cr=request.POST['Bosnia'].lower()
    brg=request.POST['ArgentinaGol'].lower()
    crg=request.POST['BosniaGol'].lower()
    pr= Prediccion (fase = 'grupos', equipo1=br, equipo2=cr, gol1=brg, gol2=crg, usuario=usuario2)
    pr.save()
    
    me=request.POST['Iran'].lower()
    ca=request.POST['Nigeria'].lower()
    meg=request.POST['IranGol'].lower()
    cag=request.POST['NigeriaGol'].lower()
    pr2= Prediccion (fase = 'grupos', equipo1=me, equipo2=ca, gol1=meg, gol2=cag, usuario=usuario2)
    pr2.save()
    
    me=request.POST['Argentina/1'].lower()
    ca=request.POST['Iran/1'].lower()
    meg=request.POST['ArgentinaGol/1'].lower()
    cag=request.POST['IranGol/1'].lower()
    pr2= Prediccion (fase = 'grupos', equipo1=me, equipo2=ca, gol1=meg, gol2=cag, usuario=usuario2)
    pr2.save()
    
    me=request.POST['Nigeria/1'].lower()
    ca=request.POST['Bosnia/1'].lower()
    meg=request.POST['NigeriaGol/1'].lower()
    cag=request.POST['BosniaGol/1'].lower()
    pr3= Prediccion (fase = 'grupos', equipo1=me, equipo2=ca, gol1=meg, gol2=cag, usuario=usuario2)
    pr3.save()
    
    me=request.POST['Nigeria/2'].lower()
    ca=request.POST['Argentina/2'].lower()
    meg=request.POST['NigeriaGol/2'].lower()
    cag=request.POST['ArgentinaGol/2'].lower()
    pr4= Prediccion (fase = 'grupos', equipo1=me, equipo2=ca, gol1=meg, gol2=cag, usuario=usuario2)
    pr4.save()
    
    me=request.POST['Iran/2'].lower()
    ca=request.POST['Bosnia/2'].lower()
    meg=request.POST['IranGol/2'].lower()
    cag=request.POST['BosniaGol/2'].lower()
    pr5= Prediccion (fase = 'grupos', equipo1=me, equipo2=ca, gol1=meg, gol2=cag, usuario=usuario2)
    pr5.save()
    
    #Grupo G
    br=request.POST['Alemania'].lower()
    cr=request.POST['Portugal'].lower()
    brg=request.POST['AlemaniaGol'].lower()
    crg=request.POST['PortugalGol'].lower()
    pr= Prediccion (fase = 'grupos', equipo1=br, equipo2=cr, gol1=brg, gol2=crg, usuario=usuario2)
    pr.save()
    
    me=request.POST['Ghana'].lower()
    ca=request.POST['EEUU'].lower()
    meg=request.POST['GhanaGol'].lower()
    cag=request.POST['EEUUGol'].lower()
    pr2= Prediccion (fase = 'grupos', equipo1=me, equipo2=ca, gol1=meg, gol2=cag, usuario=usuario2)
    pr2.save()
    
    me=request.POST['Alemania/1'].lower()
    ca=request.POST['Ghana/1'].lower()
    meg=request.POST['AlemaniaGol/1'].lower()
    cag=request.POST['GhanaGol/1'].lower()
    pr2= Prediccion (fase = 'grupos', equipo1=me, equipo2=ca, gol1=meg, gol2=cag, usuario=usuario2)
    pr2.save()
    
    me=request.POST['EEUU/1'].lower()
    ca=request.POST['Portugal/1'].lower()
    meg=request.POST['EEUUGol/1'].lower()
    cag=request.POST['PortugalGol/1'].lower()
    pr3= Prediccion (fase = 'grupos', equipo1=me, equipo2=ca, gol1=meg, gol2=cag, usuario=usuario2)
    pr3.save()
    
    me=request.POST['EEUU/2'].lower()
    ca=request.POST['Alemania/2'].lower()
    meg=request.POST['EEUUGol/2'].lower()
    cag=request.POST['AlemaniaGol/2'].lower()
    pr4= Prediccion (fase = 'grupos', equipo1=me, equipo2=ca, gol1=meg, gol2=cag, usuario=usuario2)
    pr4.save()
    
    me=request.POST['Portugal/2'].lower()
    ca=request.POST['Ghana/2'].lower()
    meg=request.POST['PortugalGol/2'].lower()
    cag=request.POST['GhanaGol/2'].lower()
    pr5= Prediccion (fase = 'grupos', equipo1=me, equipo2=ca, gol1=meg, gol2=cag, usuario=usuario2)
    pr5.save()
    
    #Grupo H
    br=request.POST['Belgica'].lower()
    cr=request.POST['Argelia'].lower()
    brg=request.POST['BelgicaGol'].lower()
    crg=request.POST['ArgeliaGol'].lower()
    pr= Prediccion (fase = 'grupos', equipo1=br, equipo2=cr, gol1=brg, gol2=crg, usuario=usuario2)
    pr.save()
    
    me=request.POST['Rusia'].lower()
    ca=request.POST['Corea'].lower()
    meg=request.POST['RusiaGol'].lower()
    cag=request.POST['CoreaGol'].lower()
    pr2= Prediccion (fase = 'grupos', equipo1=me, equipo2=ca, gol1=meg, gol2=cag, usuario=usuario2)
    pr2.save()
    
    me=request.POST['Belgica/1'].lower()
    ca=request.POST['Rusia/1'].lower()
    meg=request.POST['BelgicaGol/1'].lower()
    cag=request.POST['RusiaGol/1'].lower()
    pr2= Prediccion (fase = 'grupos', equipo1=me, equipo2=ca, gol1=meg, gol2=cag, usuario=usuario2)
    pr2.save()
    
    me=request.POST['Corea/1'].lower()
    ca=request.POST['Argelia/1'].lower()
    meg=request.POST['CoreaGol/1'].lower()
    cag=request.POST['ArgeliaGol/1'].lower()
    pr3= Prediccion (fase = 'grupos', equipo1=me, equipo2=ca, gol1=meg, gol2=cag, usuario=usuario2)
    pr3.save()
    
    me=request.POST['Corea/2'].lower()
    ca=request.POST['Belgica/2'].lower()
    meg=request.POST['CoreaGol/2'].lower()
    cag=request.POST['BelgicaGol/2'].lower()
    pr4= Prediccion (fase = 'grupos', equipo1=me, equipo2=ca, gol1=meg, gol2=cag, usuario=usuario2)
    pr4.save()
    
    me=request.POST['Argelia/2'].lower()
    ca=request.POST['Rusia/2'].lower()
    meg=request.POST['ArgeliaGol/2'].lower()
    cag=request.POST['RusiaGol/2'].lower()
    pr5= Prediccion (fase = 'grupos', equipo1=me, equipo2=ca, gol1=meg, gol2=cag, usuario=usuario2)
    pr5.save()
    
    
    #Octavos
    
    e1=casosEspeciales(request.POST['1A/oct'].lower())
    e2=casosEspeciales(request.POST['2B/oct'].lower())
    g1=request.POST['1AGol']
    g2=request.POST['2BGol']
    pp=Prediccion (fase = 'octavos', equipo1=e1, equipo2=e2, gol1=g1, gol2=g2, usuario=usuario2)
    pp.save()
    
    e1=casosEspeciales(request.POST['1C/oct'].lower())
    e2=casosEspeciales(request.POST['2D/oct'].lower())
    g1=request.POST['1CGol']
    g2=request.POST['2DGol']
    pp=Prediccion (fase = 'octavos', equipo1=e1, equipo2=e2, gol1=g1, gol2=g2, usuario=usuario2)
    pp.save()
    
    e1=casosEspeciales(request.POST['1B/oct'].lower())
    e2=casosEspeciales(request.POST['2A/oct'].lower())
    g1=request.POST['1BGol']
    g2=request.POST['2AGol']
    pp=Prediccion (fase = 'octavos', equipo1=e1, equipo2=e2, gol1=g1, gol2=g2, usuario=usuario2)
    pp.save()
    
    e1=casosEspeciales(request.POST['1D/oct'].lower())
    e2=casosEspeciales(request.POST['2C/oct'].lower())
    g1=request.POST['1DGol']
    g2=request.POST['2CGol']
    pp=Prediccion (fase = 'octavos', equipo1=e1, equipo2=e2, gol1=g1, gol2=g2, usuario=usuario2)
    pp.save()
    
    e1=casosEspeciales(request.POST['1E/oct'].lower())
    e2=casosEspeciales(request.POST['2F/oct'].lower())
    g1=request.POST['1EGol']
    g2=request.POST['2FGol']
    pp=Prediccion (fase = 'octavos', equipo1=e1, equipo2=e2, gol1=g1, gol2=g2, usuario=usuario2)
    pp.save()
    
    e1=casosEspeciales(request.POST['1G/oct'].lower())
    e2=casosEspeciales(request.POST['2H/oct'].lower())
    g1=request.POST['1GGol']
    g2=request.POST['2HGol']
    pp=Prediccion (fase = 'octavos', equipo1=e1, equipo2=e2, gol1=g1, gol2=g2, usuario=usuario2)
    pp.save()
    
    e1=casosEspeciales(request.POST['1F/oct'].lower())
    e2=casosEspeciales(request.POST['2E/oct'].lower())
    g1=request.POST['1FGol']
    g2=request.POST['2EGol']
    pp=Prediccion (fase = 'octavos', equipo1=e1, equipo2=e2, gol1=g1, gol2=g2, usuario=usuario2)
    pp.save()
    
    e1=casosEspeciales(request.POST['1H/oct'].lower())
    e2=casosEspeciales(request.POST['2G/oct'].lower())
    g1=request.POST['1HGol']
    g2=request.POST['2GGol']
    pp=Prediccion (fase = 'octavos', equipo1=e1, equipo2=e2, gol1=g1, gol2=g2, usuario=usuario2)
    pp.save()
    
    #Cuartos
    
    e1=casosEspeciales(request.POST['1A-2B/cuar'].lower())
    e2=casosEspeciales(request.POST['1C-2D/cuar'].lower())
    g1=request.POST['1A-2BGol']
    g2=request.POST['1C-2DGol']
    pp=Prediccion (fase = 'cuartos', equipo1=e1, equipo2=e2, gol1=g1, gol2=g2, usuario=usuario2)
    pp.save()
    
    e1=casosEspeciales(request.POST['1B-2A/cuar'].lower())
    e2=casosEspeciales(request.POST['1D-2C/cuar'].lower())
    g1=request.POST['1B-2AGol']
    g2=request.POST['1D-2CGol']
    pp=Prediccion (fase = 'cuartos', equipo1=e1, equipo2=e2, gol1=g1, gol2=g2, usuario=usuario2)
    pp.save()
    
    e1=casosEspeciales(request.POST['1E-2F/cuar'].lower())
    e2=casosEspeciales(request.POST['1G-2H/cuar'].lower())
    g1=request.POST['1E-2FGol']
    g2=request.POST['1G-2HGol']
    pp=Prediccion (fase = 'cuartos', equipo1=e1, equipo2=e2, gol1=g1, gol2=g2, usuario=usuario2)
    pp.save()
    
    e1=casosEspeciales(request.POST['1F-2E/cuar'].lower())
    e2=casosEspeciales(request.POST['1H-2G/cuar'].lower())
    g1=request.POST['1F-2EGol']
    g2=request.POST['1H-2GGol']
    pp=Prediccion (fase = 'cuartos', equipo1=e1, equipo2=e2, gol1=g1, gol2=g2, usuario=usuario2)
    pp.save()
    
    #Semis
    
    e1=casosEspeciales(request.POST['1s/semi'].lower())
    e2=casosEspeciales(request.POST['2s/semi'].lower())
    g1=request.POST['1sGol']
    g2=request.POST['2sGol']
    pp=Prediccion (fase = 'semis', equipo1=e1, equipo2=e2, gol1=g1, gol2=g2, usuario=usuario2)
    pp.save()
    
    e1=casosEspeciales(request.POST['3s/semi'].lower())
    e2=casosEspeciales(request.POST['4s/semi'].lower())
    g1=request.POST['3sGol']
    g2=request.POST['4sGol']
    pp=Prediccion (fase = 'semis', equipo1=e1, equipo2=e2, gol1=g1, gol2=g2, usuario=usuario2)
    pp.save()
    
    #Final

    e1= casosEspeciales(request.POST['1final'].lower())
    e2= casosEspeciales(request.POST['2final'].lower())
    g1= request.POST['1fGol']
    g2= request.POST['2fGol']
    campeoeo= request.POST['campeoeo']
    pp=Prediccion (fase = 'final', equipo1=e1, equipo2=e2, gol1=g1, gol2=g2, usuario=usuario2)
    pp1=Prediccion (fase = 'finalCampeoeo', equipo1=campeoeo, equipo2='xxx', gol1=g1, gol2=g2, usuario=usuario2)
    pp.save()
    pp1.save()
    
    #Goleador
    gole=request.POST['goleador'].lower()
    pp=Prediccion (fase = 'goleador', equipo1=gole, equipo2=1, gol1=2, gol2=3, usuario=usuario2)
    pp.save()
    
    #Tercer lugar
    e1= casosEspeciales(request.POST['1terc'].lower())
    e2= casosEspeciales(request.POST['2terc'].lower())
    g1= request.POST['1tGol']
    g2= request.POST['2tGol']
    campeoeo= request.POST['terceoeo']
    pp=Prediccion (fase = 'tercero', equipo1=e1, equipo2=e2, gol1=g1, gol2=g2, usuario=usuario2)
    pp1=Prediccion (fase = 'terceroterceoeo', equipo1=campeoeo, equipo2='xxx', gol1=g1, gol2=g2, usuario=usuario2)
    pp.save()
    pp1.save()
    
    return render(request, 'exito.html')
  else:
    return render(request, 'inicioerroneo.html')

