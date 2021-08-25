from django.db import models
from django.contrib.auth.models import User


class Character(models.Model):
    known_by = models.ManyToManyField(User, through='ColorChoice')
    points_to = models.ManyToManyField("self", symmetrical=False, through='Word')
    symbol = models.CharField(max_length=1)
    rank = models.IntegerField(default=0)
    definition = models.CharField(max_length=1000)
    pronunciation = models.CharField(max_length=40)

    def get_color(self, user):
        color_choice = self.colorchoice_set.filter(user=user)
        if color_choice.count() > 0:
            return color_choice.first().color
        return ""

    def __str__(self):
        return self.symbol


class Word(models.Model):
    first_char = models.ForeignKey(Character, related_name='is_first_char', on_delete=models.CASCADE)
    second_char = models.ForeignKey(Character, related_name='is_second_char', on_delete=models.CASCADE)
    rank = models.IntegerField(default=0)
    definition = models.CharField(max_length=1000)
    pronunciation = models.CharField(max_length=40)

    def __str__(self):
        return self.first_char.symbol + self.second_char.symbol


class ColorChoice(models.Model):
    char = models.ForeignKey(Character, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    color = models.CharField(max_length=25, default="DCDCDC")

    def __str__(self):
        return self.user.username + ":" + self.char.symbol + ":" + self.color
