from rest_framework import serializers
from authentication.models import CustomUser
from polls.models import Polls

from datetime import datetime

class PollsSerializer(serializers.ModelSerializer):

    created_by = serializers.SerializerMethodField('get_full_name')

    class Meta:
        model = Polls
        fields = ['pk', 'title', 'isClosed', 'created', 'modified', 'created_by']

    def get_full_name(self, Post):
        _id = Post.posted_by.user.pk
        user = CustomUser.objects.get(id=_id)
        full_name = str(user)
        return full_name