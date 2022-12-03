from rest_framework import serializers
from .models import User, PDF, Company, Ask, Question
from django.contrib.auth import get_user_model
from rest_framework.fields import ListField

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('email', 'password','username','id')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)

        return user

class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('id', 'company_name', 'company_number')

class PDFSerializer(serializers.ModelSerializer):

    class Meta:
        model = PDF
        fields = ('id', 'company', 'pdf_type', 'pdf_title', 'pdf', 'regist_date')

class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('id', 'title', 'question', 'regist_date')
        

class AskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ask
        fields = ('id', 'askto', 'ask', 'regist_date')
