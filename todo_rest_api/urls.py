from django.urls import path
from .views import (TodoItemView)
from strawberry.django.views import AsyncGraphQLView
from .schema import schema

urlpatterns = [
  path('todo-items', TodoItemView.as_view()),
  path('graphql', AsyncGraphQLView.as_view(schema=schema))
]