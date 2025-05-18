from django.db import models

# TodoItem Model
class TodoItem(models.Model):
  # Add the todo item value field
  value = models.CharField(max_length=1000)
  # Add the completed field
  completed = models.BooleanField(default=False, blank=True)

  # dunder method here that allows us to see stringified model
  # invoked with str(TodoItem instance)
  # helpful for debugging
  def __str__(self):
    return self.value