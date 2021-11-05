from django.contrib import admin

from myclub.models import Comment, Like, Post

# Register your models here.
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comment)
