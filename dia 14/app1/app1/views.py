from django.http import HttpResponse
from django.shortcuts import render

lista = ["fiorela", "camila", "vanessa", "sofia"]

def listar(request):
    return HttpResponse(lista)

def saludar(request):
    texto = f"hola, bienvenidos al curso de PYthon con Django"
    return HttpResponse(texto)

def saludar_nombre(resquest, nombre):
    texto = f"hola {nombre}"
    return HttpResponse(texto)

def factorial(resquest, numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado = resultado * i

    return HttpResponse(f"el factorial de {numero} es {resultado}")

def inicio_render(request):
    return render(request,'app1/inicio.html' )