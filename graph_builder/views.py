from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the index.")

def graph_build(request):
    return HttpResponse("this is graph_build")