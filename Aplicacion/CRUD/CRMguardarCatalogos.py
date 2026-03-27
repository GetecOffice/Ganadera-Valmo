from django.shortcuts import render, redirect
from django.contrib import messages
# LLAMAR ARCHIVOS LOCALES
from Aplicacion.forms import *
from Aplicacion.models import *
from django.db.models import Sum
from Aplicacion.views import servicioActivo,grupo_user

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< TABLAS DE CATALOGOS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# --------------------------------------------------------CLIENTES---------------------------------------------------------
def guardarAcciones(request):
    Descripcion_v = request.POST['descripcion'].upper()    
    # Descripcion_v = request.POST['descripcion'].upper()    
    existente = tblCRMAcciones.objects.filter(Descripcion=Descripcion_v).exists()
    if existente:
        errorCol = 'error'
        messages.error(request, f'La accion "{Descripcion_v}" ya ha sido registrado antreriormente')
        columnas = {'errorCol':errorCol}
        return render(request, "CRM Catalogos/Acciones/form.html", columnas)
    else:
        tblCRMAcciones.objects.create(Descripcion=Descripcion_v)
        messages.success(request, f'La accion "{Descripcion_v}" se ha registrado exitosamente')

    if request.method == 'POST':
        if 'salir' in request.POST:
            return redirect('TCRM_Acciones')
        elif 'agregar' in request.POST:
            return redirect('FCRM_Acciones')
    else:
        return redirect('TCRM_Acciones')
   

def guardarTipoContacto(request):
    Descripcion_v = request.POST['descripcion'].upper()    
    abreviacion_v = request.POST['abreviacion'].upper()    
    existente = tblCRMTipoContacto.objects.filter(Descripcion=Descripcion_v).exists()
    if existente:
        errorCol = 'error'
        messages.error(request, f'El tipo de contacto "{Descripcion_v}" ya ha sido registrado antreriormente')
        columnas = {'errorCol':errorCol}
        return render(request, "CRM Catalogos/Tipo Contacto/form.html", columnas)
    else:
        tblCRMTipoContacto.objects.create(Descripcion=Descripcion_v, NomCorto = abreviacion_v)
        messages.success(request, f'El tipo de contacto "{Descripcion_v}" se ha registrado exitosamente')

    if request.method == 'POST':
        if 'salir' in request.POST:
            return redirect('TCRM_TipoContacto')
        elif 'agregar' in request.POST:
            return redirect('FCRM_TipoContacto')
    else:
        return redirect('TCRM_TipoContacto')


def guardarRutas(request):
    Descripcion_v = request.POST['descripcion'].upper()    
    abreviacion_v = request.POST['abreviacion'].upper()    
    existente = tblCRMRutas.objects.filter(Descripcion=Descripcion_v).exists()
    if existente:
        errorCol = 'error'
        messages.error(request, f'El tipo de contacto "{Descripcion_v}" ya ha sido registrado antreriormente')
        columnas = {'errorCol':errorCol}
        return render(request, "CRM Catalogos/Rutas/form.html", columnas)
    else:
        tblCRMRutas.objects.create(Descripcion=Descripcion_v, NomCorto = abreviacion_v)
        messages.success(request, f'El tipo de contacto "{Descripcion_v}" se ha registrado exitosamente')

    if request.method == 'POST':
        if 'salir' in request.POST:
            return redirect('TCRM_Rutas')
        elif 'agregar' in request.POST:
            return redirect('FCRM_Rutas')
    else:
        return redirect('TCRM_Rutas')


def guardarEstadoOportunidad(request):
    Descripcion_v = request.POST['descripcion'].upper()    
    abreviacion_v = request.POST['abreviacion'].upper()    
    existente = tblCRMEstadoOportu.objects.filter(Descripcion=Descripcion_v).exists()
    if existente:
        errorCol = 'error'
        messages.error(request, f'El tipo de contacto "{Descripcion_v}" ya ha sido registrado antreriormente')
        columnas = {'errorCol':errorCol}
        return render(request, "CRM Catalogos/Estado Oportunidad/form.html", columnas)
    else:
        tblCRMEstadoOportu.objects.create(Descripcion=Descripcion_v, NomCorto = abreviacion_v)
        messages.success(request, f'El tipo de contacto "{Descripcion_v}" se ha registrado exitosamente')

    if request.method == 'POST':
        if 'salir' in request.POST:
            return redirect('TCRM_EstadoOportunidad')
        elif 'agregar' in request.POST:
            return redirect('FCRM_EstadoOportunidad')
    else:
        return redirect('TCRM_EstadoOportunidad')


def guardarVendedores(request):
    abreviacion_v = request.POST['abreviacion'].upper()    
    nombre_v = request.POST['nombre'].upper()  
    apellidos_v = request.POST['apellidos'].upper()    
    email_v = request.POST['email']
    celular_v = request.POST['celular']    

    tblCRMVendedores.objects.create(NomCorto = abreviacion_v, Nombre = nombre_v, Apellidos = apellidos_v, email = email_v, Celular = celular_v)
    messages.success(request, f'El vendedor "{nombre_v} {apellidos_v}" se ha registrado exitosamente')

    if request.method == 'POST':
        if 'salir' in request.POST:
            return redirect('TCRM_Vendedores')
        elif 'agregar' in request.POST:
            return redirect('FCRM_Vendedores')
    else:
        return redirect('TCRM_Vendedores')

def guardarContacto(request):
    ruta_v = request.POST['ruta']
    cliente_v = request.POST['cliente']
    tcontacto_v = request.POST['tcontacto']
    nombre_v = request.POST['nombre'].upper()
    papellido_v = request.POST['papellido'].upper()
    sapellido_v = request.POST['sapellido'].upper()
    fecha_v = request.POST['fecha']
    numeroC_v = request.POST['numeroC']
    email_v = request.POST['email']
    numeroO_v = request.POST['numeroO']
    direccion_v = request.POST['direccion'].upper()
    numerod_v = request.POST['numerod']
    referencia_v = request.POST['referencia']
    cp_v = request.POST['cp']
    Pais_v = request.POST['Pais'].upper()
    Estado_v = request.POST['Estado'].upper()
    Municipio_v = request.POST['Municipio'].upper()      
    Localidad_v = request.POST['Localidad'].upper()            
    Colonia_v = request.POST['Colonia'].upper()            

    ultimo_id = tblCRMContactos.objects.order_by('-ID').first()
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
    FACliente = tblClientes.objects.get(ID = cliente_v)
    FARuta = tblCRMRutas.objects.get(ID = ruta_v)
    FATipoContacto = tblCRMTipoContacto.objects.get(ID = tcontacto_v)       
    FCliente = tblClientes.objects.all()
    FRuta = tblCRMRutas.objects.all()
    FTipoContacto = tblCRMTipoContacto.objects.all()    
    FPais = tblCRMContactos.objects.exclude(Pais__isnull=True).exclude(Pais='').values_list('Pais', flat=True).distinct().order_by('Pais')
    FEstado = tblCRMContactos.objects.exclude(Estado__isnull=True).exclude(Estado='').values_list('Estado', flat=True).distinct().order_by('Estado')
    FMunicipio = tblCRMContactos.objects.exclude(Municipio__isnull=True).exclude(Municipio='').values_list('Municipio', flat=True).distinct().order_by('Municipio')
    FLocalidad = tblCRMContactos.objects.exclude(Localidad__isnull=True).exclude(Localidad='').values_list('Localidad', flat=True).distinct().order_by('Localidad')
    FColonia = tblCRMContactos.objects.exclude(Colonia__isnull=True).exclude(Colonia='').values_list('Colonia', flat=True).distinct().order_by('Colonia')     
    tblCRMContactos.objects.create(Clave = formatoClave, IDRuta_id = ruta_v, IDCliente_id = cliente_v, IDTipo_id = tcontacto_v,
    Nombre = nombre_v, PrimerApellido = papellido_v, SegundoApellido = sapellido_v, FechaCumple = fecha_v,
    Direccion = direccion_v, Numero = numerod_v, Colonia = Colonia_v, Localidad = Localidad_v, Municipio = Municipio_v,
    Estado = Estado_v, Pais = Pais_v, CP = cp_v, Referencia = referencia_v, NoCelular = numeroC_v, email = email_v, TelOficina = numeroO_v
    )
       
    messages.success(request, f'El Contacto {nombre_v} {papellido_v} {sapellido_v} se ha registrado exitosamente')        
    if request.method == 'POST':
        if 'salir' in request.POST:
            return redirect('TCRM_Contacto')
        elif 'agregar' in request.POST:
            if 'guardar-datos' in request.POST: 
                guardar = True
                columnas = {'FACliente':FACliente,'FARuta':FARuta,'FATipoContacto':FATipoContacto,'FCliente':FCliente,'FRuta':FRuta,'FTipoContacto':FTipoContacto,
                'FPais':FPais,'FEstado':FEstado,'FMunicipio':FMunicipio,'FLocalidad':FLocalidad,'FColonia':FColonia,
                'nombre': nombre_v,'papellido': papellido_v,'sapellido': sapellido_v, 'ruta': ruta_v,'cliente': cliente_v,'tcontacto': tcontacto_v, 
                'fecha': fecha_v, 'numero': numeroC_v,'numeroO': numeroO_v,'email': email_v, 'direccion': direccion_v,'numerod': numerod_v,
                'referencia': referencia_v, 'cp': cp_v,'Pais': Pais_v,'Estado': Estado_v,'Municipio': Municipio_v,'Localidad': Localidad_v,'Colonia': Colonia_v,
                'guardar': guardar}
                return render(request, "CRM Catalogos/Contacto/form.html", columnas)
            else:
                return redirect('FCRM_Contacto')
    else:
        return redirect('TCRM_Contacto')        


def guardarCliente(request):
    # PARAMETROS ENVIADOS DESDE EL FORMULARIO
    clave = request.POST['clave']
    nombre = request.POST['nombre'].upper()
    contacto = request.POST['contacto'].upper()
    direccion = request.POST['direccion'].upper()
    ciudad = request.POST['ciudad'].upper()
    rfc = request.POST['rfc']
    email = request.POST['email']
    numero = request.POST['numero']

    



    
def guardarBitacoraInteres(request):
    grupos = grupo_user(request)
    ServiciosWeb = servicioActivo()
    TBitacoraInteracciones = tblCRMBitacoraInteracciones.objects.all()
    return render(request, 'CRM Catalogos/Bitacora/index.html',{'grupos': grupos,'ServiciosWeb': ServiciosWeb,'TGestionVentas': TBitacoraInteracciones})

