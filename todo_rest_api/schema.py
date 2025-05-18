import strawberry
import strawberry_django
from strawberry_django.optimizer import DjangoOptimizerExtension
from strawberry_django import mutations

from .types import TodoItem, TodoItemInput

@strawberry.type
class Query: 
  todo_items: list[TodoItem] = strawberry_django.field()

@strawberry.type
class Mutation:
  add_todo_item: TodoItem = mutations.create(TodoItemInput)

schema = strawberry.Schema(
  query=Query,
  mutation=Mutation,
  extensions=[DjangoOptimizerExtension]
)