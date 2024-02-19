from django.db import models

class Executor(models.Model):
    """
    Модель Исполнитель
    """
    name = models.CharField(max_length=50, verbose_name="Имя")

    def __str__(self):
        return self.name


class Task(models.Model):
    """
    Модель Задача
    """
    creation_date = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    executor = models.ForeignKey(Executor, on_delete=models.CASCADE, verbose_name="Исполнитель")
    priority = models.IntegerField(choices=[(1, 1), (2, 2), (3, 3)], verbose_name="Приоритет")
    title = models.CharField(max_length=50, verbose_name="Заголовок")
    comment = models.TextField(max_length=250, verbose_name="Комментарий")

    class Meta:
        ordering = ["-creation_date"]

    def __str__(self):
        return f"Задача {self.title }от {self.creation_date} исполнитель {self.executor} приоритет {self.priority}"
