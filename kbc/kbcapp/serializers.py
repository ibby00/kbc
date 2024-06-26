
from rest_framework import serializers

from .models import KbcApp


class KbcAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = KbcApp
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']