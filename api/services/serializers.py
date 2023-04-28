from rest_framework import serializers

from api.services.models import Comment, Reaction

class ReactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reaction
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    
    comment_id = serializers.IntegerField(source='id', read_only=True)

    class Meta:
        model = Comment
        fields = ["user", "post", "comment","comment_id"]
        extra_kwargs = {
            "user": {"write_only": True},
            "post": {"write_only": True},
            "comment": {"write_only": True}
        }