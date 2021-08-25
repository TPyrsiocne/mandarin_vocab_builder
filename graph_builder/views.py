import random
from django.http import HttpResponse
from django.shortcuts import render, redirect
from graph_builder.models import Word, Character
from django.contrib.auth import login
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm


def dashboard(request):
    return render(request, "graph_builder/dashboard.html")


def register(request):
    if request.method == "GET":
        return render(request, 'graph_builder/register.html', {'form' : UserCreationForm})
    elif request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('dashboard'))
        else:
            return render(request, 'graph_builder/invalid_registration.html')


def index(request):
    context = {"characters" : Character.objects.all()}
    return render(request, "graph_builder/index.html", context)


def graph_build(request, char):
    this_char = Character.objects.filter(symbol = char).first()
    word_enders = this_char.points_to.filter(rank__range = (0, this_char.rank))
    word_starters = Character.objects.filter(points_to = this_char, rank__range = (0, this_char.rank))
    #what is Django doing with this command^
    this_char_deff = this_char.definition
    this_char_pronunciation = this_char.pronunciation

    context = {
        'this_char' : this_char,
        'this_char_deff' : this_char_deff,
        'this_char_pronunciation' : this_char_pronunciation,
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

def toggle(request, char_tag):
    current_user = request.user

    if char_tag.isdecimal():
        char_to_toggle = Character.objects.filter(rank=int(char_tag)).first()
    else:
        char_to_toggle = Character.objects.filter(symbol=char_tag).first()

    if current_user.is_authenticated:
        if current_user in char_to_toggle.known_by.all():
            char_to_toggle.known_by.remove(current_user)
        else:
            char_to_toggle.known_by.add(current_user)
    else:
        return redirect("/mandarin-graph/accounts/login/")

    return redirect("/mandarin-graph/" + char_tag +"/")