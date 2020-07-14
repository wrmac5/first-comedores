from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render
from Comedores.copa_de_leche.models import escuela
from Comedores.copa_de_leche.forms import formularioIngresoEsc
#from django.template import Template, Context

# Create your views here.

def listado(request):

    listado = escuela.objects.all()
 
    return render(request, 'index.html',{"lista":listado})

def buscar(request):
    
    if request.method=="POST":
        nombre=request.POST["txtescuela"]
        cue_esc=request.POST["txtcue"]
        deleg=request.POST["txtdelegacion"]
        local=request.POST["txtlocalidad"]
        nivel_esc=request.POST["txtnivel"]
        modal=request.POST["txtmodalidad"]
        

        todos = escuela.objects.all()
        query_nombre = todos.filter(establecimiento__icontains = nombre)
        query_cue = query_nombre.filter(cue__icontains = cue_esc)
        query_deleg = query_cue.filter(delegacion__icontains = deleg)
        query_local = query_deleg.filter(localidad__icontains = local)
        query_nivel = query_local.filter(nivel__icontains = nivel_esc)
       

        resultado = query_nivel.filter(modalidad__icontains = modal)

        return render(request, 'index.html',{ "lista": resultado })

    else:
        return HttpResponse("no pasa nada gentes")


def responsable(request):
    listado = escuela.objects.all()
    if request.method=="POST":
        
        #Preguntamos que opcion marco el usuario
        #***************************************
        eleccion = request.POST['opcion']
        
        if eleccion=='res':
            resp=request.POST["txtresp"]
            if resp=="":
                listado = listado.filter(responsable__isnull = True)
            else:
                listado = listado.filter(responsable__icontains = resp)
            return render(request, "responsables.html", {"lista": listado})
        
        
        elif eleccion=='sub':
            subresp=request.POST["txtsubresp"]
            if subresp=="":
                listado = listado.filter(sub_responsable__isnull = True)
            else:
                listado = listado.filter(sub_responsable__icontains = subresp)
            return render(request, "responsables.html", {"lista": listado})
        else:

            return render(request, 'responsables.html', {"lista":listado})
    else:
        return render(request, 'responsables.html', {"lista":listado})



def eliminar_f1(request):

    listado = escuela.objects.all()
    if request.method == "POST":
        id_esc= request.POST["txtid"]
        esc_query=listado.get(id = id_esc)
        
        return render(request, "eliminar.html", {"registro":esc_query, "lista": listado})
        

    else:
        return render(request, "eliminar.html", {"lista": listado})

def eliminar(request):

    if request.method =="POST":
        id_esc= request.POST["txtid"]
       
        borrar=escuela.objects.get(id = id_esc)
        borrar.delete()
       
        listado = escuela.objects.all()
        return render(request, "eliminar.html", {"lista": listado})


def modificar_f1(request):

    listado = escuela.objects.all()
    if request.method == "POST":
        id_esc= request.POST["txtid"]
        
        esc_query=escuela.objects.get(id = id_esc)
        
        return render(request, "modificar.html", {"registro":esc_query, "lista": listado})
        #except escuela.DoestNotExist:
        #    return render(request, "vacio.html")
        #except escuela.MutipleObjectsReturned:
        #    return render(request, "modificar.html")

    else:
        return render(request, "modificar.html", {"lista": listado})

def modificar(request):

    listado= escuela.objects.all()
    if request.method == "POST":
       
            id_frm = request.POST['txtid']
            escu_frm = request.POST['txtescuela']
            cue_frm = request.POST['txtcue']
            deleg_frm = request.POST['txtdelegacion']
            local_frm = request.POST['txtlocalidad']
            nivel_frm = request.POST['txtnivel']
            nro_cuenta_frm = request.POST['txtnro_cuenta']
            resp_frm = request.POST['txtresponsable']
            resp_dni_frm = request.POST['txtdni']
            sub_resp_frm = request.POST['txtsub_res']
            sub_resp_dni_frm = request.POST['txtsub_res_dni']
            reso_frm = request.POST['txtreso']

            reg_escuela = escuela(id = id_frm, establecimiento = escu_frm, cue = cue_frm, delegacion = deleg_frm,
            nivel = nivel_frm, localidad = local_frm, nro_cuenta = nro_cuenta_frm,
            responsable = resp_frm, responsable_dni = resp_dni_frm,
            sub_responsable = sub_resp_frm, sub_responsable_dni = sub_resp_dni_frm, 
            reso = reso_frm)

            reg_escuela.save()
            return render(request,'modificar.html', {"lista": listado})
             
    
    else:
        return HttpResponse("Los datos ni idea ")
        #miFormulario=formularioIngresoEsc()
        #return render(request, 'modificar.html', {"formulario":miFormulario})

    #return HttpResponse("nose que onda con los datos")



def ingresoEscuelas(request):
    
    listado = escuela.objects.all()
    if request.method =="POST":

        #miFormulario = formularioIngresoEsc(request.POST)

        #if miFormulario.is_valid():
        #    request.POST = miFormulario.cleaned_data

            escu_frm = request.POST['txtescuela']
            cue_frm = request.POST['txtcue']
            deleg_frm = request.POST['txtdelegacion']
            local_frm = request.POST['txtlocalidad']
            modal_frm = request.POST['txtmodalidad']
            nivel_frm = request.POST['txtnivel']
            nro_cuenta_frm = request.POST['txtnro_cuenta']
            resp_frm = request.POST['txtresponsable']
            resp_dni_frm = request.POST['txtres_dni']
            sub_resp_frm = request.POST['txtsub_res']
            sub_resp_dni_frm = request.POST['txtsub_res_dni']
            reso_frm = request.POST['txtreso']

            reg_escuela = escuela(establecimiento = escu_frm, cue = cue_frm, delegacion = deleg_frm,
            nivel = nivel_frm, localidad = local_frm, modalidad = modal_frm, nro_cuenta = nro_cuenta_frm,
            responsable = resp_frm, responsable_dni = resp_dni_frm,
            sub_responsable = sub_resp_frm, sub_responsable_dni = sub_resp_dni_frm, 
            reso = reso_frm)

            reg_escuela.save()
            
            return render(request, "ingresar.html", {"lista":listado})
            


    else:
       # miFormulario = formularioIngresoEsc()
    
        return render(request, "ingresar.html",{"lista":listado})


def contacto(request):
    return render(request, "contacto.html")