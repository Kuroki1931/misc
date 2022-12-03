from rest_framework import serializers
from rest_framework.authtoken.models import Token
from core.models import Memo

class MemoSerializer(serializers.ModelSerializer):

    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)

    class Meta:
        model = Memo
        fields = ('id', 'title', 'img', 'memo', 'created_at', 'updated_at')