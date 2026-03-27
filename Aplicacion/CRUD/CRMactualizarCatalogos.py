from django.shortcuts import render
# LLAMAR ARCHIVOS LOCALES
from Aplicacion.forms import *
from Aplicacion.models import *
from django.db.models import Sum
from Aplicacion.views import servicioActivo,grupo_user

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< TABLAS DE CATALOGOS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# --------------------------------------------------------CLIENTES---------------------------------------------------------
def actualizarAcciones(request):
    grupos = grupo_user(request)
    ServiciosWeb = servicioActivo()
    TAcciones = tblCRMAcciones.objects.all()
    return render(request, 'CRM Catalogos/Acciones/index.html',{'grupos': grupos,'ServiciosWeb': ServiciosWeb,'TAcciones': TAcciones})

def actualizarTipoContacto(request):
    grupos = grupo_user(request)
    ServiciosWeb = servicioActivo()
    TTipoContacto = tblCRMTipoContacto.objects.all()
    return render(request, 'CRM Catalogos/Tipo Contacto/index.html',{'grupos': grupos,'ServiciosWeb': ServiciosWeb,'TTipoContacto': TTipoContacto})

def actualizarRutas(request):
    grupos = grupo_user(request)
    ServiciosWeb = servicioActivo()
    TRutas = tblCRMRutas.objects.all()
    return render(request, 'CRM Catalogos/Rutas/index.html',{'grupos': grupos,'ServiciosWeb': ServiciosWeb,'TRutas': TRutas})

def actualizarEstadoOportunidad(request):
    grupos = grupo_user(request)
    ServiciosWeb = servicioActivo()
    TEstadoOportu = tblCRMEstadoOportu.objects.all()
    return render(request, 'CRM Catalogos/Estado Oportunidad/index.html',{'grupos': grupos,'ServiciosWeb': ServiciosWeb,'TEstadoOportu': TEstadoOportu})

def actualizarVendedores(request):
    grupos = grupo_user(request)
    ServiciosWeb = servicioActivo()
    TVendedores = tblCRMVendedores.objects.all()
    return render(request, 'CRM Catalogos/Vendedores/index.html',{'grupos': grupos,'ServiciosWeb': ServiciosWeb,'TVendedores': TVendedores})

def actualizarContacto(request):
    grupos = grupo_user(request)
    ServiciosWeb = servicioActivo()
    TOportunidades = tblCRMOportunidades.objects.all()
    return render(request, 'CRM Catalogos/Contacto/index.html',{'grupos': grupos,'ServiciosWeb': ServiciosWeb,'TOportunidades': TOportunidades})

def actualizarBitacoraInteres(request):
    grupos = grupo_user(request)
    ServiciosWeb = servicioActivo()
    TBitacoraInteracciones = tblCRMBitacoraInteracciones.objects.all()
    return render(request, 'CRM Catalogos/Bitacora/index.html',{'grupos': grupos,'ServiciosWeb': ServiciosWeb,'TGestionVentas': TBitacoraInteracciones})

