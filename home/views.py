from rest_framework.views import APIView
from .models import Task
from .serializers import TaskSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import logging


logger = logging.getLogger(__name__)


class GetAllTasks(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, id= None):
        try:
            if id is not None:
                try:
                    task = Task.objects.get(id=id)
                except Task.DoesNotExist:
                    return Response({'Message': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
                ser = TaskSerializer(task)
                return Response(ser.data, status=status.HTTP_200_OK)
            task = Task.objects.all()
            ser = TaskSerializer(task, many = True)
            return Response(ser.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f'Error while getting Task : {e}')
            return Response({'Message', 'error'}, status=status.HTTP_400_BAD_REQUEST)
            
            
    def post(self,request):
        try:
            ser = TaskSerializer(data=request.data)
            if ser.is_valid():
                ser.save()
                return Response({'Message', 'ok'}, status=status.HTTP_201_CREATED)
            return Response({'Message', ser.error_messages}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f'Error creating Task',{e})
            return Response({'Message': 'error'}, status=status.HTTP_400_BAD_REQUEST)
    
    
    def put(self,request,id):
        try:
            task = Task.objects.get(id=id)
            ser = TaskSerializer(task, data=request.data)
            if ser.is_valid():
                ser.save()
                return Response({'Message', 'ok'}, status=status.HTTP_201_CREATED)
            return Response({'Message', ser.error_messages}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f'Error creating Task',{e})
            return Response({'Message': 'error'}, status=status.HTTP_400_BAD_REQUEST)
            
    
    def delete(self,request,id):
        try:
            task = Task.objects.get(id=id).delete()
            return Response({'Message', 'ok'}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f'Error creating Task',{e})
            return Response({'Message': 'error'}, status=status.HTTP_400_BAD_REQUEST)