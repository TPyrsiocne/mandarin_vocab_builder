from django.db import models


class Character(models.Model):
    symbol = models.CharField(max_length = 1)
    rank = models.IntegerField(default = 0)


#definition formating to be decided
class Char_Deff(models.Model):
    character = models.ForeignKey(Character, on_delete = models.CASCADE)
    definition = models.CharField(max_length = 1000)
    pronunciation = models.CharField(max_length = 40)
    #ordinal ranks deffintions from first to last
    ordinal = models.IntegerField(default = 0)


class Word(models.Model):
    text = models.CharField(max_length=3)
    definition = models.CharField(max_length = 1000)
    rank = models.IntegerField(default = 0)


class Word_Deff(models.Model):
    word = models.ForeignKey(Word, on_delete = models.CASCADE)
    definition = models.CharField(max_length = 1000)
    pronunciation = models.CharField(max_length = 40)
    # ordinal ranks deffintions from first to last
    ordinal = models.IntegerField(default = 0)