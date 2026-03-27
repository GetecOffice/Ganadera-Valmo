from django.shortcuts import render
# LLAMAR ARCHIVOS LOCALES
from Aplicacion.forms import *
from Aplicacion.models import *
from django.db.models import F
from django.db.models import Sum
from Aplicacion.views import servicioActivo,grupo_user

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< TABLAS DE CATALOGOS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# --------------------------------------------------------CLIENTES---------------------------------------------------------
def TablaAcciones(request):
    grupos = grupo_user(request)
    ServiciosWeb = servicioActivo()
    TAcciones = tblCRMAcciones.objects.all()
    return render(request, 'CRM Catalogos/Acciones/index.html',{'grupos': grupos,'ServiciosWeb': ServiciosWeb,'TAcciones': TAcciones})

def TablaTipoContacto(request):
    grupos = grupo_user(request)
    ServiciosWeb = servicioActivo()
    TTipoContacto = tblCRMTipoContacto.objects.all()
    return render(request, 'CRM Catalogos/Tipo Contacto/index.html',{'grupos': grupos,'ServiciosWeb': ServiciosWeb,'TTipoContacto': TTipoContacto})

def TablaRutas(request):
    grupos = grupo_user(request)
    ServiciosWeb = servicioActivo()
    TRutas = tblCRMRutas.objects.all()
    return render(request, 'CRM Catalogos/Rutas/index.html',{'grupos': grupos,'ServiciosWeb': ServiciosWeb,'TRutas': TRutas})

def TablaEstadoOportunidad(request):
    grupos = grupo_user(request)
    ServiciosWeb = servicioActivo()
    TEstadoOportu = tblCRMEstadoOportu.objects.all()
    return render(request, 'CRM Catalogos/Estado Oportunidad/index.html',{'grupos': grupos,'ServiciosWeb': ServiciosWeb,'TEstadoOportu': TEstadoOportu})

def TablaVendedores(request):
    grupos = grupo_user(request)
    ServiciosWeb = servicioActivo()
    TVendedores = tblCRMVendedores.objects.all()
    return render(request, 'CRM Catalogos/Vendedores/index.html',{'grupos': grupos,'ServiciosWeb': ServiciosWeb,'TVendedores': TVendedores})

def TablaContacto(request):
    grupos = grupo_user(request)
    ServiciosWeb = servicioActivo()
    TContactos = tblCRMContactos.objects.values('ID', 'IDRuta_id', 'IDCliente_id', 'IDTipo_id', 'Nombre',
    'PrimerApellido', 'SegundoApellido', 'FechaCumple', 'Direccion', 'Numero', 'Colonia', 'Localidad', 
    'Municipio', 'Estado', 'Pais', 'CP', 'Referencia', 'NoCelular', 'email', 'TelOficina',
    'IDCliente_id__Nombre', 'IDRuta_id__Descripcion', 'IDTipo_id__Descripcion'       
)
    return render(request, 'CRM Catalogos/Contacto/index.html',{'grupos': grupos,'ServiciosWeb': ServiciosWeb,'TContactos': TContactos})

def TablaBitacoraInteres(request):
    grupos = grupo_user(request)
    ServiciosWeb = servicioActivo()
    TBitacoraInteracciones = tblCRMBitacoraInteracciones.objects.all()
    return render(request, 'CRM Catalogos/Bitacora/index.html',{'grupos': grupos,'ServiciosWeb': ServiciosWeb,'TGestionVentas': TBitacoraInteracciones})

