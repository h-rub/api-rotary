import json
from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from authentication.models import Profile
from myclub.models import Like, Post

from myclub.serializer import PostsSerializer

# Create your views here.
def ping(request):
    responseData = {"msg":f"Pong"}
    return HttpResponse(json.dumps(responseData), content_type="application/json")

class GetPosts(ModelViewSet):
    serializer_class = PostsSerializer
    queryset = Post.objects.all()


class SaveReaction(APIView):
    def post(self, request):
        post_id = request.data['post_id']
        liked_by = request.data['liked_by'] 
        profile = Profile.objects.get(pk=liked_by)
        post = Post.objects.get(pk=post_id)
        #is_liked = bool(request.data['is_completed'])
        exists = Like.objects.filter(liked_by=profile, post_liked=post).exists()
        print(exists)
        if exists == True:
            post_deleted = Like.objects.get(liked_by = profile, post_liked = post).delete()
            post_db_deleted = str(post_deleted)
            return Response({"msg":f"Post {post_id} liked has been deleted"}, status=status.HTTP_200_OK)
        else:
            created = Like.objects.create(liked_by = profile, post_liked = post)
            return Response({"msg":f"Posts {post_id} liked by {liked_by} "}, status=status.HTTP_200_OK)


