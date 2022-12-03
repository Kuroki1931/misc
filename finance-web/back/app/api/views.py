from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from .serializers import PDFSerializer, UserSerializer, CompanySerializer, QuestionSerializer, AskSerializer
from .models import PDF, Company, Ask, Question
from rest_framework.permissions import AllowAny
import stripe
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
import os
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

stripe.api_key = settings.STRIPE_KEY
# Create your views here.

@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def save_stripe_info(request):
    data = request.data
    email = data['email']
    payment_method_id = data['payment_method_id']
    extra_msg = ''

    customer_data = stripe.Customer.list(email=email).data
    
    # creating customer
    if len(customer_data) == 0:
        customer = stripe.Customer.create(
            email=email, 
            payment_method=payment_method_id,
            invoice_settings={
            'default_payment_method': payment_method_id
        }
    )
    else:
        customer = customer_data[0]
        extra_msg = "Customer already existed."

    stripe.Subscription.create(
        customer=customer,
        items=[
            {
                'price': 'price_1Ioec5HcV7uIYIgy581EHmAF'
            }
        ]
    )  
     
    return Response(status=status.HTTP_200_OK, 
      data={
        'message': 'Success', 
        'data': {'customer_id': customer.id, 'extra_msg': extra_msg}
        }
    )

class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (AllowAny,)

class PDFViewSet(viewsets.ModelViewSet):
    queryset = PDF.objects.all()
    serializer_class = PDFSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (AllowAny,)

class AskViewSet(viewsets.ModelViewSet):
    queryset = Ask.objects.all()
    serializer_class = AskSerializer




