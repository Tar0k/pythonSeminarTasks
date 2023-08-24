from django.db import models

# Create your models here.


class Contacts(models.Model):
    first_name = models.CharField(max_length=255, verbose_name="Имя")
    last_name = models.CharField(max_length=255, null=True, verbose_name="Фамилия")
    middle_name = models.CharField(max_length=255, null=True, verbose_name="Отчество")
    phone_number = models.CharField(max_length=255, verbose_name="Телефонный номер")

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
