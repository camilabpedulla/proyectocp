from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader 
from appfamilia.models import familia 

def familiares (request):

    familiar=familia.objects.all()

    lista_integrantes=[]

    for familias in familiar:
       data = f"{familias.nombre} ,tiene {familias.edad} años y nació el {familias.fecha_de_nacimiento}"
    
       lista_integrantes.append(data)

    datos= {"familiares":lista_integrantes}

    archivo = open (r"C:\Users\camil\OneDrive\Escritorio\proyectoentrega\proyectocp\proyectocp\Template\info.html","r")
    contenido_html =archivo.read()
    archivo.close ()

    plantilla= Template(contenido_html)
    contexto = Context(datos)

    documento_render=plantilla.render(contexto)


    return HttpResponse (documento_render)

