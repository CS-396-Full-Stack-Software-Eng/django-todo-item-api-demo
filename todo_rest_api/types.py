import strawberry_django
from strawberry import auto, ID

from .models import TodoItem as TodoItemModel

@strawberry_django.type(TodoItemModel)
class TodoItem:
  id: ID
  value: auto
  completed: auto

@strawberry_django.input(TodoItemModel, partial=True)
class TodoItemInput:
  value: str
  completed: auto