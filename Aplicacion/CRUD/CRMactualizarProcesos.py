from django.shortcuts import redirect, render
from django.contrib import messages
# LLAMAR ARCHIVOS LOCALES
from Aplicacion.forms import *
from Aplicacion.models import *
from django.db.models import Sum
from Aplicacion.views import servicioActivo,grupo_user


def ActualizarOportunidades(request):
    id = request.POST['id']
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

    vendedor_instancia = tblCRMVendedores.objects.get(ID=vendedor_v)
    contacto_instancia = tblCRMContactos.objects.get(ID=contacto_v)
    producto_instancia = tblProductos.objects.get(ID=producto_v)
    venta_instancia = tblCRMEstadoOportu.objects.get(ID=venta_v)
            
    saves = tblCRMOportunidades.objects.get(ID=id)
    folio = saves.Clave
    saves.IDVendedor = vendedor_instancia
    saves.IDContacto = contacto_instancia
    saves.IDProducto = producto_instancia
    saves.IDEstadoVenta = venta_instancia
    saves.SelectActividad = actividad_v
    saves.SelectTipoGanado = tganado_v
    saves.SelectDestino = destino_v
    saves.SelectAlimentacion = alimentacion_v
    saves.Volumen = volumen_v
    saves.MontoOpo = monto_v
    saves.FechaCierreEstim = fechaCE_v
    saves.FechaDeCierre = fechaC_v

    saves.save()
        
    messages.success(request, f'La oportunidad "{folio}" se ha actualizado exitosamente.')
    return redirect('TCRM_Oportunidades')

def actualizarBitacoraInteres(request):
    grupos = grupo_user(request)
    ServiciosWeb = servicioActivo()
    TBitacoraInteracciones = tblCRMBitacoraInteracciones.objects.all()
    return render(request, 'CRM Catalogos/Bitacora/index.html',{'grupos': grupos,'ServiciosWeb': ServiciosWeb,'TGestionVentas': TBitacoraInteracciones})

