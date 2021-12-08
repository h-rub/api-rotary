from django.db import models
from django.db.models.deletion import DO_NOTHING

from authentication.models import Profile

class Polls(models.Model):
    created_by  = models.ForeignKey(Profile, on_delete=DO_NOTHING)
    title = models.CharField(max_length=300, blank=True)
    isClosed = models.BooleanField(default=False, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

class Options(models.Model):
    poll = models.ForeignKey(Polls, on_delete=DO_NOTHING)
    option = models.CharField(max_length=400, blank=True)

class Vote(models.Model):
    voted_by = models.ForeignKey(Profile, on_delete=DO_NOTHING)
    poll = models.ForeignKey(Polls, on_delete=DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)