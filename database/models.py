from django.db import models

class Articles(models.Model):
    location = models.CharField('Локация', max_length=50)
    subdivision = models.CharField('Подразделение', max_length=50)
    department = models.CharField('Отдел', max_length=50)
    group = models.CharField('Группа', max_length=50)
    position = models.CharField('Должность', max_length=50)
    name = models.CharField('ФИО', max_length=50)
    kindofwork = models.CharField('Тип работы', max_length=50)

    def __str__(self):
        return self.location

    class Meta:
        verbose_name = 'База сотрудников'
        verbose_name_plural = 'База сотрудников'