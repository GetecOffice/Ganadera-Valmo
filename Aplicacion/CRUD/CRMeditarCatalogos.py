from django.shortcuts import render
# LLAMAR ARCHIVOS LOCALES
from Aplicacion.forms import *
from Aplicacion.models import *
from django.db.models import Sum
from Aplicacion.views import servicioActivo,grupo_user

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< TABLAS DE CATALOGOS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# --------------------------------------------------------CLIENTES---------------------------------------------------------
def EditarAcciones(request, ID):
    grupos = grupo_user(request)
    ServiciosWeb = servicioActivo()
    TAcciones = tblCRMAcciones.objects.get(ID=ID)
    return render(request, 'CRM Catalogos/Acciones/edit.html',{'grupos': grupos,'ServiciosWeb': ServiciosWeb,'TAcciones': TAcciones})

def EditarTipoContacto(request, ID):
    grupos = grupo_user(request)
    ServiciosWeb = servicioActivo()
    TTipoContacto = tblCRMTipoContacto.objects.get(ID=ID)
    return render(request, 'CRM Catalogos/Tipo Contacto/edit.html',{'grupos': grupos,'ServiciosWeb': ServiciosWeb,'TTipoContacto': TTipoContacto})

def EditarRutas(request, ID):
    grupos = grupo_user(request)
    ServiciosWeb = servicioActivo()
    TRutas = tblCRMRutas.objects.get(ID=ID)
    return render(request, 'CRM Catalogos/Rutas/edit.html',{'grupos': grupos,'ServiciosWeb': ServiciosWeb,'TRutas': TRutas})

def EditarEstadoOportunidad(request, ID):
    grupos = grupo_user(request)
    ServiciosWeb = servicioActivo()
    TEstadoOportu = tblCRMEstadoOportu.objects.get(ID=ID)
    return render(request, 'CRM Catalogos/Estado Oportunidad/edit.html',{'grupos': grupos,'ServiciosWeb': ServiciosWeb,'TEstadoOportu': TEstadoOportu})

def EditarVendedores(request, ID):
    grupos = grupo_user(request)
    ServiciosWeb = servicioActivo()
    TVendedores = tblCRMVendedores.objects.get(ID=ID)
    return render(request, 'CRM Catalogos/Vendedores/edit.html',{'grupos': grupos,'ServiciosWeb': ServiciosWeb,'TVendedores': TVendedores})

def EditarContacto(request, ID):
    grupos = grupo_user(request)
    ServiciosWeb = servicioActivo()
    TContacto = tblCRMContactos.objects.get(ID = ID)
    FiltrarRutas = TContacto.IDRuta.ID
    FiltrarCliente = TContacto.IDCliente.ID
    FiltrarTipoContacto = TContacto.IDTipo.ID
    fecha = TContacto.FechaCumple
    
    FiltradoRutas = tblCRMRutas.objects.get(ID=FiltrarRutas)
    FiltradoCliente = tblClientes.objects.get(ID=FiltrarCliente)
    FiltradoTipoContacto = tblCRMTipoContacto.objects.get(ID=FiltrarTipoContacto)
    
    FRuta = tblCRMRutas.objects.all()
    FCliente = tblClientes.objects.all()
    FTipoContacto = tblCRMTipoContacto.objects.all()
    
    FPais = tblCRMContactos.objects.exclude(Pais__isnull=True).exclude(Pais='').values_list('Pais', flat=True).distinct().order_by('Pais')
    FEstado = tblCRMContactos.objects.exclude(Estado__isnull=True).exclude(Estado='').values_list('Estado', flat=True).distinct().order_by('Estado')
    FMunicipio = tblCRMContactos.objects.exclude(Municipio__isnull=True).exclude(Municipio='').values_list('Municipio', flat=True).distinct().order_by('Municipio')
    FLocalidad = tblCRMContactos.objects.exclude(Localidad__isnull=True).exclude(Localidad='').values_list('Localidad', flat=True).distinct().order_by('Localidad')
    FColonia = tblCRMContactos.objects.exclude(Colonia__isnull=True).exclude(Colonia='').values_list('Colonia', flat=True).distinct().order_by('Colonia')
    
    return render(request, 'CRM Catalogos/Contacto/edit.html',{'grupos': grupos,'ServiciosWeb': ServiciosWeb, 'FCliente':FCliente, 'FRuta':FRuta, 'FTipoContacto':FTipoContacto, 
    'FPais':FPais, 'FEstado':FEstado, 'FMunicipio':FMunicipio, 'FLocalidad':FLocalidad, 'FColonia':FColonia, 'TContacto':TContacto, 
    'FiltradoRutas':FiltradoRutas, 'FiltradoCliente':FiltradoCliente, 'FiltradoTipoContacto':FiltradoTipoContacto, 'fecha':fecha })

def EditarBitacoraInteres(request, ID):
    grupos = grupo_user(request)
    ServiciosWeb = servicioActivo()
    TBitacoraInteracciones = tblCRMBitacoraInteracciones.objects.get(ID=ID)
    return render(request, 'CRM Catalogos/Bitacora/edit.html',{'grupos': grupos,'ServiciosWeb': ServiciosWeb,'TGestionVentas': TBitacoraInteracciones})

