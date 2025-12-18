from django.db import models

# Create your models here.
class dataFormModels(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    isRead = models.BooleanField(default=False)

    def __str__(self):
        return self.name