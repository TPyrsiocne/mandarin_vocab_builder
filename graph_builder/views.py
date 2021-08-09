from django.http import HttpResponse
from graph_builder.models import Word, Character, Char_Deff

def index(request):
    return HttpResponse("Hello, world. You're at the index.")

def graph_build(request, char):
    char_deff = Char_Deff.objects.get(character__symbol = char)
    """
      how do I sort QuerySets bassed on the other chars' rank?
      how to filter words by rank
    """
    char_inital_words = Word.objects.filter(symbols__startswith = char)
    char_final_words = Word.objects.filter(symbols__endswith = char)


    """ the folowing formating will be later done with a template"""
    a = ""
    for i in char_inital_words:
        a = a + "----> " + i.symbols[1] + "<br>"

    b = ""
    for i in char_final_words:
        b = b + "<br>" + i.symbols[0] + " ----> "

    return HttpResponse(char + "<br><br>" + char_deff.pronunciation + "<br>" + char_deff.definition +
                        "<br><br><br>"+"LINKS FROM<br>"+ char + a +"<br><br> LINKS TO" + b +char)


"""
maybe I could have a graph building 
view which desplays a character's graph and deffinition
and then a word def displaying view
which would be linked to when you click an edege.

another idea would be to have defintions be mosueover text or seomthing
"""