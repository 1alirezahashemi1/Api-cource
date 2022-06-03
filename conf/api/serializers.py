from rest_framework import serializers
from blog.models import Blog
from django.contrib.auth import get_user_model
# Right Your Serializers Down Below

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"