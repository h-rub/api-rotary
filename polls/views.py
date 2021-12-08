from django.shortcuts import render
import json

from django.http.response import HttpResponse

# Create your views here.
def ping(request):
    responseData = {"msg":f"Pong"}
    return HttpResponse(json.dumps(responseData), content_type="application/json")