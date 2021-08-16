from graph_builder.models import Character, Word
PATH_TO_CHARDICT = "/Users/tysonprice/mandarin_vocab_builder/char_dict.txt"
PATH_TO_WORDDICT = "/Users/tysonprice/mandarin_vocab_builder/word_dict.txt"


#clear tabels of characters
Character.objects.all().delete()
#import and populate
for line in open(PATH_TO_CHARDICT, "r").readlines()[:4000]:
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
        Character(symbol = tokens[1],
                  rank = int(tokens[0]),
                  definition= tokens[5],
                  pronunciation= tokens[4]).save()


"""
#check for duplicates : this code is inefficient and dobule/triple/etc. prints; can be improved
for char in Character.objects.all():
    multiplicity = Character.objects.filter(symbol = char.symbol).count()
    if multiplicity > 1:
        print("WARNING: " + char.symbol + "is duplicated " + str(multiplicity) +" times")
"""



#clear tabels of words
Word.objects.all().delete()
#import and popluate
"""
only imports words with characters in character table. 
if characters appear multiple times in character table, uses only one instance in table.
which instance might be sensitive to order of entries in table. this could be fixed by sorting 
the querysets char1 and char2 are defined to be.
"""
chars = Character.objects.all()
for line in open(PATH_TO_WORDDICT, "r").readlines()[:20000]:
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

        char1 = chars.filter(symbol = tokens[1][0])
        char2 = chars.filter(symbol=tokens[1][1])

        if char1.count()*char2.count() > 0:
            Word(first_char = char1.first(),
                 second_char = char2.first(),
                 rank=int(tokens[0])
                 ).save()

