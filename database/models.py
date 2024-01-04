from django.db import models

class Articles(models.Model):
    name = models.CharField('ФИО', max_length=50, blank=False)
    location = models.CharField('Локация', max_length=50, blank=False)
    subdivision = models.CharField('Подразделение', max_length=50)
    department = models.CharField('Отдел', max_length=50)
    group = models.CharField('Группа', max_length=50, blank=False)
    position = models.CharField('Должность', max_length=50, blank=False)
    kindofwork = models.CharField('Тип работы', max_length=50, blank=False)

    def __str__(self):
        return self.location

    class Meta:
        verbose_name = 'База сотрудников'
        verbose_name_plural = 'База сотрудников'