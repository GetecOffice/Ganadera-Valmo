from django.shortcuts import redirect, render
from django.contrib import messages
# LLAMAR ARCHIVOS LOCALES
from Aplicacion.forms import *
from Aplicacion.models import *
from django.db.models import Sum
from Aplicacion.views import servicioActivo,grupo_user

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< TABLAS DE CATALOGOS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# --------------------------------------------------------CLIENTES---------------------------------------------------------

def actualizarAcciones(request):
    id = request.POST['id']
    descripcion = request.POST['descripcion'].title().strip()

    nombre_existente = tblCRMAcciones.objects.filter(Descripcion=descripcion).exclude(ID=id).exists()
    if nombre_existente:
        messages.error(request, f'La accion "{descripcion}" ya ha sido registrado anteriormente.')
        IDNumber = int(id)
        return redirect('ECRM_Acciones', IDNumber)
    else:
        saves = tblCRMAcciones.objects.get(ID=id)
        saves.Descripcion = descripcion
        saves.save()
        
        messages.success(request, f'La accion "{descripcion}" se ha actualizado exitosamente.')

    return redirect('TCRM_Acciones')

def actualizarTipoContacto(request):
    id = request.POST['id']
    descripcion_v = request.POST['descripcion'].title().strip()
    abreviacion_v = request.POST['abreviacion'].title().strip()

    nombre_existente = tblCRMTipoContacto.objects.filter(Descripcion=descripcion_v).exclude(ID=id).exists()
    if nombre_existente:
        messages.error(request, f'El tipo de contacto "{descripcion_v}" ya ha sido registrado anteriormente.')
        IDNumber = int(id)
        return redirect('ECRM_TipoContacto', IDNumber)
    else:
        saves = tblCRMTipoContacto.objects.get(ID=id)
        saves.Descripcion = descripcion_v
        saves.NomCorto = abreviacion_v
        saves.save()
        
        messages.success(request, f'El tipo de contacto "{descripcion_v}" se ha actualizado exitosamente.')

    return redirect('TCRM_TipoContacto')

def actualizarRutas(request):
    id = request.POST['id']
    descripcion_v = request.POST['descripcion'].title().strip()
    abreviacion_v = request.POST['abreviacion'].title().strip()

    nombre_existente = tblCRMRutas.objects.filter(Descripcion=descripcion_v).exclude(ID=id).exists()
    if nombre_existente:
        messages.error(request, f'La ruta"{descripcion_v}" ya ha sido registrado anteriormente.')
        IDNumber = int(id)
        return redirect('ECRM_Rutas', IDNumber)
    else:
        saves = tblCRMRutas.objects.get(ID=id)
        saves.Descripcion = descripcion_v
        saves.NomCorto = abreviacion_v
        saves.save()
        messages.success(request, f'La ruta"{descripcion_v}" se ha actualizado exitosamente.')
    return redirect('TCRM_Rutas')

def actualizarEstadoOportunidad(request):
    id = request.POST['id']
    descripcion_v = request.POST['descripcion'].title().strip()
    abreviacion_v = request.POST['abreviacion'].title().strip()

    nombre_existente = tblCRMEstadoOportu.objects.filter(Descripcion=descripcion_v).exclude(ID=id).exists()
    if nombre_existente:
        messages.error(request, f'El estado de oportunidad "{descripcion_v}" ya ha sido registrado anteriormente.')
        IDNumber = int(id)
        return redirect('ECRM_EstadoOportunidad', IDNumber)
    else:
        saves = tblCRMEstadoOportu.objects.get(ID=id)
        saves.Descripcion = descripcion_v
        saves.NomCorto = abreviacion_v
        saves.save()
        
        messages.success(request, f'El estado de oportunidad "{descripcion_v}" se ha actualizado exitosamente.')

    return redirect('TCRM_EstadoOportunidad')
    
def actualizarVendedores(request):
    id = request.POST['id']
    abreviacion_v = request.POST['abreviacion'].title().strip()
    nombre_v = request.POST['nombre'].title().strip()
    apellidos_v = request.POST['apellidos'].title().strip()
    email_v = request.POST['email']
    celular_v = request.POST['celular']

        
    saves = tblCRMVendedores.objects.get(ID=id)
    saves.NomCorto = abreviacion_v
    saves.Nombre = nombre_v
    saves.Apellidos = apellidos_v
    saves.email = email_v
    saves.Celular = celular_v
    saves.save()
        
    messages.success(request, f'El vendedor "{nombre_v} {apellidos_v}" se ha actualizado exitosamente.')

    return redirect('TCRM_Vendedores')
    
def actualizarContacto(request):
    id = request.POST['id']
    ruta_v = request.POST['ruta']
    cliente_v = request.POST['cliente']
    tcontacto_v = request.POST['tcontacto']
    nombre_v = request.POST['nombre'].title()
    papellido_v = request.POST['papellido'].title()
    sapellido_v = request.POST['sapellido'].title()
    fecha_v = request.POST['fecha']
    numeroC_v = request.POST['numeroC']
    email_v = request.POST['email']
    numeroO_v = request.POST['numeroO']
    direccion_v = request.POST['direccion'].title()
    numerod_v = request.POST['numerod']
    referencia_v = request.POST['referencia']
    cp_v = request.POST['cp']
    Pais_v = request.POST['Pais'].title()
    Estado_v = request.POST['Estado'].title()
    Municipio_v = request.POST['Municipio'].title()      
    Localidad_v = request.POST['Localidad'].title()            
    Colonia_v = request.POST['Colonia'].title() 

    ruta_instancia = tblCRMRutas.objects.get(ID=ruta_v)
    cliente_instancia = tblClientes.objects.get(ID=cliente_v)
    tcontacto_instancia = tblCRMTipoContacto.objects.get(ID=tcontacto_v)
            
    saves = tblCRMContactos.objects.get(ID=id)
    folio = saves.Clave
    saves.IDRuta = ruta_instancia
    saves.IDCliente = cliente_instancia
    saves.IDTipo = tcontacto_instancia
    saves.Nombre = nombre_v
    saves.PrimerApellido = papellido_v
    saves.SegundoApellido = sapellido_v
    saves.FechaCumple = fecha_v
    saves.NoCelular = numeroC_v
    saves.email = email_v
    saves.TelOficina = numeroO_v
    saves.Direccion = direccion_v
    saves.Numero = numerod_v
    saves.Referencia = referencia_v
    saves.CP = cp_v
    saves.Pais = Pais_v
    saves.Estado = Estado_v
    saves.Municipio = Municipio_v
    saves.Localidad = Localidad_v
    saves.Colonia = Colonia_v
    saves.save()
        
    messages.success(request, f'El Contacto "{folio}" se ha actualizado exitosamente.')
    return redirect('TCRM_Contacto')

def actualizarBitacoraInteres(request):
    grupos = grupo_user(request)
    ServiciosWeb = servicioActivo()
    TBitacoraInteracciones = tblCRMBitacoraInteracciones.objects.all()
    return render(request, 'CRM Catalogos/Bitacora/index.html',{'grupos': grupos,'ServiciosWeb': ServiciosWeb,'TGestionVentas': TBitacoraInteracciones})

