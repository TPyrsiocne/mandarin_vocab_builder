from django.db import models


class Character(models.Model):
    points_to = models.ManyToManyField("self", symmetrical=False, through='Word')
    symbol = models.CharField(max_length = 1)
    rank = models.IntegerField(default = 0)
    definition = models.CharField(max_length = 1000)
    pronunciation = models.CharField(max_length = 40)
    def __str__(self):
        return self.symbol


class Word(models.Model):
    first_char = models.ForeignKey(Character, related_name = 'is_first_char',on_delete=models.CASCADE)
    second_char = models.ForeignKey(Character, related_name='is_second_char', on_delete=models.CASCADE)
    rank = models.IntegerField(default = 0)
    definition = models.CharField(max_length = 1000)
    pronunciation = models.CharField(max_length = 40)
    def __str__(self):
        return self.first_char.symbol + self.second_char.symbol