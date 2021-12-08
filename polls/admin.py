from django.contrib import admin

from polls.models import Options, Polls, Vote

# Register your models here.
admin.site.register(Polls)
admin.site.register(Options)
admin.site.register(Vote)