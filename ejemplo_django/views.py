from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola! Bienvenido a mi primer sitio web")