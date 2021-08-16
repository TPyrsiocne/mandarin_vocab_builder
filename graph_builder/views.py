import random
from django.http import HttpResponse
from django.shortcuts import render
from graph_builder.models import Word, Character


def index(request):
    context = {"characters" : Character.objects.all()}
    return render(request, "graph_builder/index.html", context)


def graph_build(request, char):
    this_char = Character.objects.filter(symbol = char).first()
    word_enders = this_char.points_to.filter(rank__range = (0, this_char.rank))
    word_starters = Character.objects.filter(points_to = this_char, rank__range = (0, this_char.rank))
    this_char_deff = this_char.definition


    context = {
        'this_char' : this_char,
        'this_char_deff' : this_char_deff,
        'word_starters' : word_starters,
        'word_enders' : word_enders,

        'next' : this_char.rank + 1,#is it possible to incriment/decrement value in template?
        'random' : random.choice(range(2000)) + 1,
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