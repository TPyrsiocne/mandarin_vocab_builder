from graph_builder.models import Character, Word, Char_Deff, Word_Deff

""" 
PATH_TOCHARDICT was being interpereted relative to wherever
~% python manage.py shell < scripts/populate_tables.py 
command was run. fixed this by including entire file path
"""
PATH_TO_CHARDICT = "/Users/tysonprice/mandarin_vocab_builder/char_dict.txt"
PATH_TO_WORDDICT = "/Users/tysonprice/mandarin_vocab_builder/word_dict.txt"


#clear tabels of characters and their deffinitions
Character.objects.all().delete()
Char_Deff.objects.all().delete()
#import and populate
for line in open(PATH_TO_CHARDICT, "r").readlines()[:3000]:
    if line[0].isnumeric():
        tokens = line.split("\t")
        """
        token[0] == rank
        token[1] == char
        token[2] == individual raw frequency
        token[3] == cumulative frequency in precentile
        token[4] == pinyin(s)
        token[5] == english translation(s)
        
        all tokens are strings, mutiple deffinitions and pronuncations are deliomited by '/'. 
        """
        new_char = Character(symbol = tokens[1], rank = int(tokens[0]))
        new_char_deff = Char_Deff(character = new_char, definition= tokens[5], pronunciation= tokens[4], ordinal = 1)
        new_char.save()
        new_char_deff.save()

#clear tabels of words and their deffinitions
Word.objects.all().delete()
Word_Deff.objects.all().delete()
#import and popluate
for line in open(PATH_TO_WORDDICT, "r").readlines()[:3000]:
    if line[0].isnumeric():
        tokens = line.split("\t")
        """
        token[0] == rank
        token[1] == symbols
        token[2] == ?
        token[3] == ?
        token[4] == ?

        all tokens are strings. 
        """
        new_word = Word(symbols=tokens[1], rank=int(tokens[0]))
        new_word.save()
