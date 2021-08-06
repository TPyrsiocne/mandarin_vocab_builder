from django.db import models


class Character(models.Model):
    symbol = models.CharField(max_length = 1)
    rank = models.IntegerField(default = 0)

    def __str__(self):
        return self.symbol


"""
Look into the idea of a get_next_ordinal method? 
(coudl apply to Word_Deff too)

What about having the *_Deff objects be 
extensions of a single class?
"""

class Char_Deff(models.Model):
    character = models.ForeignKey(Character, on_delete = models.CASCADE)
    definition = models.CharField(max_length = 1000)
    pronunciation = models.CharField(max_length = 40)
    #ordinal ranks deffintions from first to last
    ordinal = models.IntegerField(default = 0)

    def __str__(self):
        return self.definition[:40] + "..."


class Word(models.Model):
    symbols = models.CharField(max_length=3)
    rank = models.IntegerField(default = 0)

    def __str__(self):
        return self.symbols


class Word_Deff(models.Model):
    word = models.ForeignKey(Word, on_delete = models.CASCADE)
    definition = models.CharField(max_length = 1000)
    pronunciation = models.CharField(max_length = 40)
    # ordinal ranks deffintions from first to last
    ordinal = models.IntegerField(default = 0)

    def __str__(self):
        return self.definition[:40] + "..."