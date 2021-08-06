from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the index.")

def graph_build(request, txt):
    return HttpResponse("this is graph_build " + txt)


"""
maybe I could have a graph building 
view which desplays a character's graph and deffinition
and then a word def displaying view
which would be linked to when you click an edege.

another idea would be to have defintions be mosueover text or seomthing
"""