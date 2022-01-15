from django.shortcuts import render
def musica_online (request):
    return render (request, 'proyecto_web_musica_app/musica_online.html')

def programas (request):
    return render (request, 'proyecto_web_musica_app/programas.html')

def inicio (request):
    return render (request,'proyecto_web_musica_app/inicio.html')


