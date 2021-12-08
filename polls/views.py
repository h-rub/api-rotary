from django.shortcuts import render
import json

from django.http.response import HttpResponse
from rest_framework.viewsets import ModelViewSet

from polls.models import Polls
from polls.serializer import PollsSerializer

# Create your views here.
def ping(request):
    responseData = {"msg":f"Pong"}
    return HttpResponse(json.dumps(responseData), content_type="application/json")

class GetPolls(ModelViewSet):
    serializer_class = PollsSerializer
    queryset = Polls.objects.all()

    def get_serializer_context(self):
        context = super(GetPolls, self).get_serializer_context()
        context.update({"request": self.request})
        return context