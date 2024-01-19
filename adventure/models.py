# adventure/models.py
from django.db import models

class Artifact(models.Model):
    name = models.CharField(max_length=255)

class Room(models.Model):
    name = models.CharField(max_length=255)
    riddle = models.TextField()
    riddle_answer = models.CharField(max_length=255)  # Add this line
    artifact = models.ForeignKey(Artifact, on_delete=models.CASCADE, null=True, blank=True)
    connected_room = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    directions = models.JSONField(default=dict)
