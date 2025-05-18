from rest_framework import serializers
from .models import TodoItem

class TodoItemSerializer(serializers.ModelSerializer):
  class Meta:
    # Add the model
    model = TodoItem
    # Add fields that can be accessed with the api
    fields = ["value", "completed"]