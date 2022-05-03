from rest_framework import serializers
from blog.models import Blog
# Right Your Serializers Down Below

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'