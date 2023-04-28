from rest_framework import serializers

from api.services.models import Reaction

class ReactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reaction
        fields = "__all__"