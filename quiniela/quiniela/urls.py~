from django.conf.urls.defaults import patterns, include, url
from quiniela.views import home, guardarUsuario, iniciarSesion, procesar, verp, admine, rnue, rnue2, rnue3, rnue4, rnue5, rnue6, rnue7, ptosarb
from django.contrib import admin
admin.autodiscover()


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'quiniela.views.home', name='home'),
    # url(r'^quiniela/', include('quiniela.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home),
    url(r'^creacioncuenta/',guardarUsuario),
    url(r'^iniciarsesion/',iniciarSesion),
    url(r'^procesarquiniela/',procesar),
    url(r'^verpredicc/',verp),
    url(r'^home/',home),
    url(r'^adminlogin/',admine),
    url(r'^resultadosnuevos/',rnue),
    url(r'^resultadosnuevos2/',rnue2),
    url(r'^resultadosnuevos3/',rnue3),
    url(r'^resultadosnuevos4/',rnue4),
    url(r'^resultadosnuevos5/',rnue5),
    url(r'^resultadosnuevos6/',rnue6),
    url(r'^resultadosnuevos7/',rnue7),
    url(r'^ptosarbitrarios/',ptosarb),
    
)
