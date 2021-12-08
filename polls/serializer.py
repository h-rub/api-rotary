from rest_framework import serializers
from polls.models import Polls

from datetime import datetime

class PollsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Polls
        fields = "__all__"