from rest_framework import serializers
from .models import Company
from rest_framework.fields import ListField

class StringArrayField(ListField):
    """
    String representation of an array field.
    """
    def to_representation(self, obj):
        obj = super().to_representation(self, obj)
        # convert list to string
        return ",".join([str(element) for element in obj])

    def to_internal_value(self, data):
        data = data.split(",")  # convert string to list
        return super().to_internal_value(self, data)


class CompanySerializer(serializers.ModelSerializer):
    keywords = serializers.JSONField()
    recruit = serializers.JSONField()
    news = serializers.JSONField()
    
    class Meta:
        model = Company
        fields = ['id', 'name', 'category', 'keywords', 'recruit', 'news']