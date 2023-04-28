from rest_framework import serializers

from api.post.models import Post
from api.account.models import User

class PostCreateSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),default=serializers.CurrentUserDefault(),required=False,write_only=True)

    class Meta:
        model = Post
        fields = "__all__" 