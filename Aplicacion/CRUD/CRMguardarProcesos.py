from django.shortcuts import render, redirect
from django.contrib import messages
# LLAMAR ARCHIVOS LOCALES
from Aplicacion.forms import *
from Aplicacion.models import *
from django.db.models import Sum
from Aplicacion.views import servicioActivo,grupo_user

def guardarOportunidad(request):
    vendedor_v = request.POST['vendedor']
    contacto_v = request.POST['contacto']
    producto_v = request.POST['producto']
    venta_v = request.POST['venta']
    actividad_v = request.POST['actividad']
    tganado_v = request.POST['tganado']
    destino_v = request.POST['destino']
    alimentacion_v = request.POST['alimentacion']
    volumen_v = request.POST['volumen']
    monto_v = request.POST['monto']
    fechaCE_v = request.POST['fechaCE']
    fechaC_v = request.POST['fechaC']
          

    ultimo_id = tblCRMOportunidades.objects.order_by('-ID').first()
    if ultimo_id:
        ultimo_folio = ultimo_id.ID + 1
    else:
        ultimo_folio = 1
            
    # AQUI SE CREAR EL FOLIO PARA LAS TABLAS
    clave_int = int(ultimo_folio)
    formatoClave = 'F-{:06d}'.format(clave_int)

    if request.method == 'POST':
        if request.method == 'POST':
            if 'guardar-datos' in request.POST:
                guardar = True
            else:
                guardar = False
    else:
        guardar = False
    FAVendedor = tblCRMVendedores.objects.get(ID = vendedor_v)
    FAContacto = tblCRMContactos.objects.get(ID = contacto_v)
    FAProducto = tblProductos.objects.get(ID = producto_v)       
    FAVenta = tblCRMEstadoOportu.objects.get(ID = venta_v)       
    FVendedor = tblCRMVendedores.objects.all()
    FContacto = tblCRMContactos.objects.all()
    FProductos= tblProductos.objects.exclude(ID = 1)
    FEstatusOportu = tblCRMEstadoOportu.objects.all() 
 
    tblCRMOportunidades.objects.create(Clave = formatoClave, IDVendedor_id = vendedor_v, IDContacto_id = contacto_v, IDProducto_id = producto_v,
    IDEstadoVenta_id = venta_v, Volumen = volumen_v, SelectActividad = actividad_v, SelectTipoGanado = tganado_v,
    SelectDestino = destino_v, SelectAlimentacion = alimentacion_v, MontoOpo = monto_v, FechaCierreEstim = fechaCE_v, FechaDeCierre = fechaC_v,
    
    )
       
    messages.success(request, f'La oportunidad "{formatoClave}"se ha registrado exitosamente')        
    if request.method == 'POST':
        if 'salir' in request.POST:
            return redirect('TCRM_Oportunidades')
        elif 'agregar' in request.POST:
            if 'guardar-datos' in request.POST: 
                guardar = True
                columnas = {'FAVendedor':FAVendedor,'FAContacto':FAContacto,'FAProducto':FAProducto,'FAVenta':FAVenta,
                            'vendedor':vendedor_v,'contacto':contacto_v,'producto':producto_v,'venta':venta_v,
                'FVendedor':FVendedor,'FContacto':FContacto,'FProductos':FProductos,'FEstatusOportu':FEstatusOportu,
                'actividad': actividad_v,'tganado': tganado_v,'destino': destino_v, 'alimentacion': alimentacion_v,'volumen': volumen_v,'monto': monto_v, 
                'fechaCE': fechaCE_v, 'fechaC': fechaC_v, 'guardar': guardar}
                return render(request, "CRM Proceso/form.html", columnas)
            else:
                return redirect('FCRM_Oportunidades')
    else:
        return redirect('TCRM_Oportunidades')        