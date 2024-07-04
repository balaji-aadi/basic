from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
import logging

logger = logging.getLogger(__name__)


class RegisterUser(APIView):
    def post(self, request):
        try:
            ser = UserSerializer(data=request.data)
            if ser.is_valid():
                ser.save() 
                user = User.objects.get(username = ser.data['username'])
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'Message': 'ok', 'token': str(token)} , status=status.HTTP_201_CREATED)
                
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f'Error while getting Task : {e}')
            return Response({'Message', 'error'}, status=status.HTTP_400_BAD_REQUEST)
    