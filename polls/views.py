from django.shortcuts import render
import json

from django.http.response import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from authentication.models import CustomUser, Profile

from polls.models import Options, Polls, Vote
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


class SaveVote(APIView):
    def post(self, request):
        poll_id = request.data['poll_id']
        voted_by = request.data['voted_by']
        option_id = request.data['voto']
        user = CustomUser.objects.get(pk=voted_by)
        profile = Profile.objects.get(user=user.pk)
        poll = Polls.objects.get(pk=poll_id)
        option = Options.objects.get(pk = option_id)
        #is_liked = bool(request.data['is_completed'])
        created = Vote.objects.create(voted_by = profile, poll = poll, option = option)
        return Response({"msg":f"Poll {poll_id} voted by {voted_by} - Voto: {option}"}, status=status.HTTP_200_OK)