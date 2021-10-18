from django.db import models
from django.db.models.deletion import DO_NOTHING

from authentication.models import CustomUser

# Create your models here.
class Task(models.Model):
    _id_task = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=200, blank=True)
    is_completed = models.BooleanField(default=False)
    due_date = models.DateField(blank=True, null=True)
    time_date = models.TimeField(blank=True, null=True)

    asigned_to = models.ForeignKey(CustomUser, on_delete=DO_NOTHING)

    def __str__(self):
        return f"{self._id_task} - {self.title}"