from django.shortcuts import render
# LLAMAR ARCHIVOS LOCALES
from Aplicacion.forms import *
from Aplicacion.models import *
from django.db.models import Sum
from Aplicacion.views import servicioActivo,grupo_user

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< TABLAS DE CATALOGOS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# --------------------------------------------------------CLIENTES---------------------------------------------------------
def FormularioAcciones(request):
    grupos = grupo_user(request)
    ServiciosWeb = servicioActivo()
    return render(request, 'CRM Catalogos/Acciones/form.html',{'grupos': grupos,'ServiciosWeb': ServiciosWeb})

def FormularioTipoContacto(request):
    grupos = grupo_user(request)
    ServiciosWeb = servicioActivo()
    return render(request, 'CRM Catalogos/Tipo Contacto/form.html',{'grupos': grupos,'ServiciosWeb': ServiciosWeb})

def FormularioRutas(request):
    grupos = grupo_user(request)
    ServiciosWeb = servicioActivo()
    return render(request, 'CRM Catalogos/Rutas/form.html',{'grupos': grupos,'ServiciosWeb': ServiciosWeb})

def FormularioEstadoOportunidad(request):
    grupos = grupo_user(request)
    ServiciosWeb = servicioActivo()
    return render(request, 'CRM Catalogos/Estado Oportunidad/form.html',{'grupos': grupos,'ServiciosWeb': ServiciosWeb})

def FormularioVendedores(request):
    grupos = grupo_user(request)
    ServiciosWeb = servicioActivo()
    return render(request, 'CRM Catalogos/Vendedores/form.html',{'grupos': grupos,'ServiciosWeb': ServiciosWeb})

def FormularioContacto(request):
    grupos = grupo_user(request)
    ServiciosWeb = servicioActivo()
    FCliente = tblClientes.objects.all()
    FRuta = tblCRMRutas.objects.all()
    FTipoContacto = tblCRMTipoContacto.objects.all()
    FPais = tblCRMContactos.objects.exclude(Pais__isnull=True).exclude(Pais='').values_list('Pais', flat=True).distinct().order_by('Pais')
    FEstado = tblCRMContactos.objects.exclude(Estado__isnull=True).exclude(Estado='').values_list('Estado', flat=True).distinct().order_by('Estado')
    FMunicipio = tblCRMContactos.objects.exclude(Municipio__isnull=True).exclude(Municipio='').values_list('Municipio', flat=True).distinct().order_by('Municipio')
    FLocalidad = tblCRMContactos.objects.exclude(Localidad__isnull=True).exclude(Localidad='').values_list('Localidad', flat=True).distinct().order_by('Localidad')
    FColonia = tblCRMContactos.objects.exclude(Colonia__isnull=True).exclude(Colonia='').values_list('Colonia', flat=True).distinct().order_by('Colonia')
    return render(request, 'CRM Catalogos/Contacto/form.html',{'grupos': grupos,'ServiciosWeb': ServiciosWeb, 'FCliente':FCliente, 'FRuta':FRuta, 'FTipoContacto':FTipoContacto, 
    'FPais':FPais, 'FEstado':FEstado, 'FMunicipio':FMunicipio, 'FLocalidad':FLocalidad, 'FColonia':FColonia})

def FormularioBitacoraInteres(request):
    grupos = grupo_user(request)
    ServiciosWeb = servicioActivo()
    TBitacoraInteracciones = tblCRMBitacoraInteracciones.objects.all()
    return render(request, 'CRM Catalogos/Bitacora/form.html',{'grupos': grupos,'ServiciosWeb': ServiciosWeb,'TGestionVentas': TBitacoraInteracciones})

