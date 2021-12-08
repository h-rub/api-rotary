from rest_framework import serializers
from authentication.models import CustomUser
from polls.models import Options, Polls, Vote

from datetime import datetime

class PollsSerializer(serializers.ModelSerializer):

    created_by = serializers.SerializerMethodField('get_full_name')
    options = serializers.SerializerMethodField('get_options')
    votes = serializers.SerializerMethodField('get_votes')

    class Meta:
        model = Polls
        fields = ['pk', 'title', 'isClosed', 'created', 'modified', 'created_by', 'options', 'votes']

    def get_full_name(self, Polls):
        _id = Polls.created_by.user.pk
        user = CustomUser.objects.get(id=_id)
        full_name = str(user)
        return full_name

    def get_options(self, Polls):
        _id = Polls.pk
        poll = Polls.__class__.objects.get(pk = _id)
        option = Options.objects.all().filter(poll = poll).values()
        return option

    def get_votes(self, Polls):
        _id = Polls.pk
        poll = Polls.__class__.objects.get(pk = _id)
        vote = Vote.objects.all().filter(poll = poll).values()
        return vote