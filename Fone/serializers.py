from rest_framework import serializers

from .models import Fone


class FoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fone
        fields = "__all__"
