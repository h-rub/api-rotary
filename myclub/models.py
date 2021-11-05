from django.db import models
from django.db.models.deletion import DO_NOTHING

from authentication.models import Profile

# Create your models here.
class Post(models.Model):
    posted_by = models.ForeignKey(Profile, on_delete=DO_NOTHING)
    content = models.CharField(blank=True, null=True, max_length=900)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.content}"

class Like(models.Model):
    liked_by = models.ForeignKey(Profile, on_delete=DO_NOTHING)
    post_liked = models.ForeignKey(Post, on_delete=DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.post_liked}"

class Comment(models.Model):
    commented_by = models.ForeignKey(Profile, on_delete=DO_NOTHING)
    post_commented = models.ForeignKey(Post, on_delete=DO_NOTHING)
    comment = models.CharField(blank=True, null=True, max_length=900)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.comment}"
    
    def get_comment(self):
        data = {
            'id': self.pk,
            'commented_by': self.commented_by,
            'comment': self.comment
        }
        return data

