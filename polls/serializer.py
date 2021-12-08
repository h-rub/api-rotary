from rest_framework import serializers
from authentication.models import CustomUser
from polls.models import Polls

from datetime import datetime

class PollsSerializer(serializers.ModelSerializer):

    created_by = serializers.SerializerMethodField('get_full_name')
    options = serializers.SerializerMethodField('get_options')

    class Meta:
        model = Polls
        fields = ['pk', 'title', 'isClosed', 'created', 'modified', 'created_by', 'options']

    def get_full_name(self, Polls):
        _id = Polls.created_by.user.pk
        user = CustomUser.objects.get(id=_id)
        full_name = str(user)
        return full_name

    def get_options(self, Polls):
        _id = Polls.pk
        poll = Polls.objects.get(pk = _id)
        option = Polls.__class__.objects.all().filter(poll = poll)
        data = {"id_pk": _id, "options": option}
        return data