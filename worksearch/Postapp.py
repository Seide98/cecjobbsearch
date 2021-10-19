from rest_framework import serializers
from .models import Post, PostPlan

class Postapp(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['date_added', 'user']

class Postplan(serializers.ModelSerializer):
    class Meta:
        model = PostPlan
        fields = ['last_app_date', 'user']