from rest_framework import serializers
from myclub.models import Comment, Post, Like
from authentication.models import CustomUser, Profile

from datetime import datetime

class PostsSerializer(serializers.ModelSerializer):

    posted_by = serializers.SerializerMethodField('get_full_name')
    profile_image = serializers.SerializerMethodField('get_profile_picture')
    likes_count = serializers.SerializerMethodField('get_likes_count')
    comments_count = serializers.SerializerMethodField('get_comments_count')
    comments = serializers.SerializerMethodField('get_all_comments')
    time_ago = serializers.SerializerMethodField('get_time_ago')

    # TODO Is Liked By Me
    is_liked_by_me = serializers.SerializerMethodField('get_liked_by_me')

    class Meta:
        model = Post
        fields = ['pk', 'profile_image', 'time_ago', 'content', 'created', 'posted_by', 'is_liked_by_me', 'likes_count', 'comments_count', 'comments']

    def get_profile_picture(self, Post):
        _id = Post.posted_by.pk
        picture = Post.posted_by.profile_picture
        return str(picture)

    def convert_elapsed_seconds(self, seconds):
        days = int(seconds / 60 / 60 / 24)
        seconds -= days * 60 * 60 * 24
        hours = int(seconds / 60 / 60)
        seconds -= hours*60*60
        minutes = int(seconds/60)
        seconds -= minutes*60
        if minutes < 1 and seconds <= 60:
            time_ago = f"Hace un momento"
        elif minutes >= 1 and minutes < 2:
            time_ago = f"Hace un minuto"
        elif days >=1:
            time_ago = f"Hace {days} días"
        elif hours < 1:
            time_ago = f"Hace {minutes} minutos"
        elif hours >= 1 and hours < 2:
            time_ago = f"Hace {hours} hora"
        elif hours >= 2:
            time_ago = f"Hace {hours} horas"
        return time_ago

    def get_time_ago(self, Post):
        created_date = Post.created
        now_date = datetime.utcnow()
        difference = now_date.replace(tzinfo=None) - created_date.replace(tzinfo=None) 
        seconds = difference.total_seconds()
        resp = self.convert_elapsed_seconds(seconds)
        return resp

    def is_liked_by_me(self, Post):
        """
        Method to get true or false if the post is liked by the user
        The id from the user logged is received on post petition
        """
        print(self.request)
        return str(self.request)

    def get_full_name(self, Post):
        _id = Post.posted_by.user.pk
        user = CustomUser.objects.get(id=_id)
        full_name = str(user)
        return full_name

    def get_likes_count(self, Post):
        post = Post.pk
        likes = Like.objects.all().filter(post_liked=post).count()
        return int(likes)

    def get_comments_count(self, Post):
        post = Post.pk
        comment_count = Comment.objects.all().filter(post_commented=post).count()
        return int(comment_count)
    
    def get_all_comments(self, Post):
        post = Post.pk
        comment_reference = Comment.objects.all().filter(post_commented=post)

        all_comments = []
        
        for comment in comment_reference:
            post_commented = comment.post_commented.pk
            commented_by = comment.commented_by
            all_comments.append({
                'id_comment' : comment.pk,
                'commented_by' : str(commented_by),
                'comment': comment.comment,
                'post_commented': post_commented,
                'created': comment.created
            })
        
        return all_comments