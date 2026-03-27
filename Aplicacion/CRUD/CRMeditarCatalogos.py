from django.shortcuts import render
# LLAMAR ARCHIVOS LOCALES
from Aplicacion.forms import *
from Aplicacion.models import *
from django.db.models import Sum
from Aplicacion.views import servicioActivo,grupo_user

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< TABLAS DE CATALOGOS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# --------------------------------------------------------CLIENTES---------------------------------------------------------
def EditarAcciones(request):
    grupos = grupo_user(request)
    ServiciosWeb = servicioActivo()
    TAcciones = tblCRMAcciones.objects.all()
    return render(request, 'CRM Catalogos/Acciones/form.html',{'grupos': grupos,'ServiciosWeb': ServiciosWeb,'TAcciones': TAcciones})

def EditarTipoContacto(request):
    grupos = grupo_user(request)
    ServiciosWeb = servicioActivo()
    TTipoContacto = tblCRMTipoContacto.objects.all()
    return render(request, 'CRM Catalogos/Tipo Contacto/form.html',{'grupos': grupos,'ServiciosWeb': ServiciosWeb,'TTipoContacto': TTipoContacto})

def EditarRutas(request):
    grupos = grupo_user(request)
    ServiciosWeb = servicioActivo()
    TRutas = tblCRMRutas.objects.all()
    return render(request, 'CRM Catalogos/Rutas/form.html',{'grupos': grupos,'ServiciosWeb': ServiciosWeb,'TRutas': TRutas})

def EditarEstadoOportunidad(request):
    grupos = grupo_user(request)
    ServiciosWeb = servicioActivo()
    TEstadoOportu = tblCRMEstadoOportu.objects.all()
    return render(request, 'CRM Catalogos/Estado Oportunidad/form.html',{'grupos': grupos,'ServiciosWeb': ServiciosWeb,'TEstadoOportu': TEstadoOportu})

def EditarVendedores(request):
    grupos = grupo_user(request)
    ServiciosWeb = servicioActivo()
    TVendedores = tblCRMVendedores.objects.all()
    return render(request, 'CRM Catalogos/Vendedores/form.html',{'grupos': grupos,'ServiciosWeb': ServiciosWeb,'TVendedores': TVendedores})

def EditarContacto(request):
    grupos = grupo_user(request)
    ServiciosWeb = servicioActivo()
    TOportunidades = tblCRMOportunidades.objects.all()
    return render(request, 'CRM Catalogos/Contacto/form.html',{'grupos': grupos,'ServiciosWeb': ServiciosWeb,'TOportunidades': TOportunidades})

def EditarBitacoraInteres(request):
    grupos = grupo_user(request)
    ServiciosWeb = servicioActivo()
    TBitacoraInteracciones = tblCRMBitacoraInteracciones.objects.all()
    return render(request, 'CRM Catalogos/Bitacora/form.html',{'grupos': grupos,'ServiciosWeb': ServiciosWeb,'TGestionVentas': TBitacoraInteracciones})

