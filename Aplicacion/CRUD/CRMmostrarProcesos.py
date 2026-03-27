from django.shortcuts import render
# LLAMAR ARCHIVOS LOCALES
from Aplicacion.forms import *
from Aplicacion.models import *
from django.db.models import Sum
from Aplicacion.views import servicioActivo,grupo_user

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< TABLAS DE CATALOGOS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# --------------------------------------------------------CLIENTES---------------------------------------------------------
def TablaOportunidades(request):
    grupos = grupo_user(request)
    TGestionVentas = tblCRMOportunidades.objects.all().values('ID','Clave','IDContacto__IDRuta__Descripcion', 'IDContacto_id__Nombre', 'IDContacto_id__PrimerApellido', 'IDContacto_id__SegundoApellido', 'IDContacto_id__email',
    'IDContacto_id__NoCelular', 'NombreProyecto', 'MontoOpo', 'FechaCierreEstim', 'FechaDeCierre', 'IDVendedor_id__Nombre', 'IDVendedor_id__Apellidos', 'IDProducto_id__Descripcion',
    'IDContacto_id__Localidad', 'IDEstadoVenta_id__Descripcion', 'IDContacto__IDTipo__Descripcion', 'Volumen', 'SelectActividad', 'SelectTipoGanado', 'SelectDestino', 'SelectAlimentacion')
    ServiciosWeb = servicioActivo()

    
    return render(request, 'CRM Proceso/index.html',{'grupos': grupos,'ServiciosWeb': ServiciosWeb,'TGestionVentas': TGestionVentas})