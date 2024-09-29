from django.db import models

# Create your models here.

class UserList(models.Model):
    id = models.IntegerField(primary_key=True)
    chat_id = models.IntegerField(verbose_name='Номер пользователя')

    def __str__(self):
        return str(self.chat_id)

    class Meta:
        ordering = ["id"]
        verbose_name = 'Администраторы ТГ'
        verbose_name_plural = 'Администратор ТГ'