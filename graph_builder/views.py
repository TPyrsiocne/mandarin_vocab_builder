from django.shortcuts import render
from graph_builder.models import Word, Character, Char_Deff

def index(request):
    return HttpResponse("Hello, world. You're at the index.")

def graph_build(request, char):
    this_char = Character.objects.get(symbol = char)
    this_char_deff = Char_Deff.objects.get(character__symbol = char)
    """
      how do I sort QuerySets bassed on the other chars' rank?
      how to filter words by rank
    """
    char_initial_words = Word.objects.filter(symbols__startswith = char)
    char_final_words = Word.objects.filter(symbols__endswith = char)


    """
    there might be a better way to do this using filter
    """
    rank_limit = this_char.rank
    word_starters = []
    for word in char_final_words:
        starter = Character.objects.get(symbol=word.symbols[0])
        if starter.rank <= rank_limit:
            word_starters.append(starter)

    word_enders = []
    for word in char_initial_words:
        ender = Character.objects.get(symbol=word.symbols[1])
        if ender.rank <= rank_limit:
            word_enders.append(ender)


    context = {
        'this_char' : this_char,
        'this_char_deff' : this_char_deff,
        'word_starters' : word_starters,
        'word_enders' : word_enders,
        }
    return render(request, "graph_builder/graph_build.html", context)

"""
maybe I could have a graph building 
view which desplays a character's graph and deffinition
and then a word def displaying view
which would be linked to when you click an edege.

another idea would be to have defintions be mosueover text or seomthing
"""