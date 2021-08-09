from django.shortcuts import render
from graph_builder.models import Word, Character, Char_Deff

def index(request):
    return HttpResponse("Hello, world. You're at the index.")

def graph_build(request, char):
    char_deff = Char_Deff.objects.get(character__symbol = char)
    """
      how do I sort QuerySets bassed on the other chars' rank?
      how to filter words by rank
    """
    char_initial_words = Word.objects.filter(symbols__startswith = char)
    char_final_words = Word.objects.filter(symbols__endswith = char)

    context = {
        'char' : char,
        'char_deff' : char_deff,
        'char_initial_words' : char_initial_words,
        'char_final_words' : char_final_words,
        }
    return render(request, "graph_builder/graph_build.html", context)

"""
maybe I could have a graph building 
view which desplays a character's graph and deffinition
and then a word def displaying view
which would be linked to when you click an edege.

another idea would be to have defintions be mosueover text or seomthing
"""