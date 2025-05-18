from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TodoItem
from .serializers import TodoItemSerializer 

class TodoItemView(APIView):
  def get(self, request, *args, **kwargs):
    todoItems = TodoItem.objects
    serializer = TodoItemSerializer(todoItems, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def post(self, request, *args, **kwargs):
    data = {
      'value': request.data.get('value'),
      'completed': request.data.get('completed')
    }

    serializer = TodoItemSerializer(data=data)

    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
