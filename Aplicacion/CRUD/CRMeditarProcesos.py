from django.shortcuts import render
# LLAMAR ARCHIVOS LOCALES
from Aplicacion.forms import *
from Aplicacion.models import *
from django.db.models import Sum
from Aplicacion.views import servicioActivo,grupo_user

def EditarOportunidad(request, ID):
    grupos = grupo_user(request)
    ServiciosWeb = servicioActivo()
    TOportunidad = tblCRMOportunidades.objects.get(ID = ID)
    
    FiltrarVendedor = TOportunidad.IDVendedor.ID
    FiltrarContacto = TOportunidad.IDContacto.ID
    FiltrarProducto = TOportunidad.IDProducto.ID
    FiltrarEstadoVenta  = TOportunidad.IDEstadoVenta.ID
    
    FiltradoVendedor = tblCRMVendedores.objects.get(ID=FiltrarVendedor)
    FiltradoContacto = tblCRMContactos.objects.get(ID=FiltrarContacto)
    FiltradoProducto = tblProductos.objects.get(ID=FiltrarProducto)
    FiltradoEstadoVenta = tblCRMEstadoOportu.objects.get(ID=FiltrarEstadoVenta)
    
    FVendedor = tblCRMVendedores.objects.all()
    FContacto = tblCRMContactos.objects.all()
    FProductos= tblProductos.objects.exclude(ID = 1)
    FEstatusOportu = tblCRMEstadoOportu.objects.all()
        
    return render(request, 'CRM Proceso/edit.html',{'grupos': grupos,'ServiciosWeb': ServiciosWeb, 
    'FVendedor':FVendedor, 'FContacto':FContacto, 'FProductos':FProductos, 'FEstatusOportu':FEstatusOportu, 'TOportunidad':TOportunidad,
    'FiltradoVendedor':FiltradoVendedor, 'FiltradoContacto':FiltradoContacto, 'FiltradoProducto':FiltradoProducto, 'FiltradoEstadoVenta':FiltradoEstadoVenta })