from rest_framework import serializers
from blog.models import Blog
from django.contrib.auth.models import User
# Right Your Serializers Down Below

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"