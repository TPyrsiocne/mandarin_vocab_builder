from django.shortcuts import render
from graph_builder.models import Word, Character, Char_Deff

def index(request):
    return HttpResponse("Hello, world. You're at the index.")

def graph_build(request, char):

    this_char = Character.objects.filter(symbol = char)
    """if each character symbol only has one entry these error messages should not be tripped
        maybe dictionary should be better sanitizied"""
    if this_char.count()>1:
        print("WARNING: " + this_char.first().symbol + "has multiple entries in characters table")
    this_char = this_char.first()


    this_char_deff = Char_Deff.objects.filter(character__symbol = char)
    if this_char_deff.count()>1:
        print("WARNING: " + this_char_deff.first().character.symbol + "has multiple entries in characters table")
    this_char_deff = this_char_deff.first()

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
        starter = Character.objects.filter(symbol=word.symbols[0])
        if starter.count() > 1:
            print("WARNING: " + starter.first().symbol + "has multiple entries in characters table")

        if starter.count()>0 and starter.first().rank <= rank_limit:
            word_starters.append(starter.first())

    word_enders = []
    for word in char_initial_words:
        ender = Character.objects.filter(symbol=word.symbols[1])
        if ender.count() > 1:
            print("WARNING: " + ender.first().symbol + "has multiple entries in characters table")

        if ender.count()>0 and ender.first().rank <= rank_limit:
            word_enders.append(ender.first())


    context = {
        'this_char' : this_char,
        'this_char_deff' : this_char_deff,
        'word_starters' : word_starters,
        'word_enders' : word_enders,
        'next' : this_char.rank + 1,
        'previous' : max(this_char.rank - 1,1),
        }
    return render(request, "graph_builder/graph_build.html", context)

"""
maybe I could have a graph building 
view which desplays a character's graph and deffinition
and then a word def displaying view
which would be linked to when you click an edege.

another idea would be to have defintions be mosueover text or seomthing
"""


def graph_build_from_rank(request, char_rank):
    char = Character.objects.get(rank = char_rank).symbol
    return graph_build(request = request, char = char)