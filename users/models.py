from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    image = models.ImageField(upload_to="media/users_images", default="media/default.jpg", blank=True, null=True, verbose_name='аватар')
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
    def __str__(self):
        return self.username