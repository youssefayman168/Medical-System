from django.db import models

# Create your models here.

class Activity (models.Model) : 
    sent_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    content = models.TextField()
    made_by = models.ForeignKey("users.User", on_delete=models.CASCADE)

    def __str__(self) : 
        return self.content
    