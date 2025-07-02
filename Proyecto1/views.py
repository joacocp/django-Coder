from django.http import HttpResponse


def saludo(request):
    return HttpResponse("Hola Mundo - este es un saludo nuevo")
