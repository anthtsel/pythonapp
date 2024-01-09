from django.db import models

class HangmanGame(models.Model):
    word = models.CharField(max_length=50)
    guessed_letters = models.CharField(max_length=26, default='', blank=True)
    attempts_left = models.IntegerField(default=6)

    def display_word(self):
        return ''.join(letter if letter in self.guessed_letters else '_' for letter in self.word)

