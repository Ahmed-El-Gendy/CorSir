from django.db import models
from django.contrib.auth.models import User

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='custom_admin_user')
    def __str__(self):
        return self.user.username
