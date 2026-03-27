from django.shortcuts import render
# LLAMAR ARCHIVOS LOCALES
from Aplicacion.forms import *
from Aplicacion.models import *
from django.db.models import Sum
from Aplicacion.views import servicioActivo,grupo_user
from django.utils import timezone
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< TABLAS DE CATALOGOS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# --------------------------------------------------------CLIENTES---------------------------------------------------------
def FormularioOportunidades(request):
    grupos = grupo_user(request)
    ServiciosWeb = servicioActivo()
    FVendedor = tblCRMVendedores.objects.all()
    FContacto = tblCRMContactos.objects.all()
    FProductos= tblProductos.objects.exclude(ID = 1)
    FEstatusOportu = tblCRMEstadoOportu.objects.all()
    FechaDeHoy = timezone.localtime(timezone.now()).strftime('%Y-%m-%d') 
    
    return render(request, 'CRM Proceso/form.html',{'grupos': grupos,'ServiciosWeb': ServiciosWeb, 'FVendedor':FVendedor, 'FContacto':FContacto, 'FProductos':FProductos, 
    'FEstatusOportu':FEstatusOportu, 'FechaDeHoy':FechaDeHoy})