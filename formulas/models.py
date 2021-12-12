from django.db import models

from datetime import datetime



class Theme(models.Model):
    """ Тема из физики """
    name = models.CharField(max_length=225)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'


class Formula(models.Model):
    """ Формула """


    # Размерность 
    OPTIONS = [
        ('Вт, (Ватт)', 'Вт, (Ватт)'),
        ('Ом', 'Омы'),
        ('В, (Вольт)', 'В, (Вольт)'),
        ('Гц, (Герц)', 'Гц, (Герц)'),
        ('Дж, (Джоуль)', 'Дж, (Джоуль)'),
        ('Кл, (Кулоны)', 'Кл, (Кулоны)'),
        ('Па, (Паскаль)', 'Па, (Паскаль)'),
        ('H, (Ньютон)', 'H, (Ньютон)'),
        ('Ф, (Фарат)', 'Ф, (Фарат)'),
        ('К, (Кельвин)', 'К, (Кельвин)'),
        ('%', 'Проценты'),
        ('Сек', 'Cекунды'),
        ('м/c', 'Метры в секунду'),
        ('км/ч', 'Километры в час'),
        ('Дптр, (Диоптри) ', 'Дптр, (Диоптри) '),
        ('м^3', 'Метры кубические'),
        ('м^2', 'Метры квадратные'),
        ('°, (Градусы)', '°, (Градусы)'),
        ('°C, (Градусы Цельсия)', 'Градусы'),
    ]

    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    name = models.CharField(max_length=225)
    description = models.TextField()
    dimension = models.CharField(OPTIONS, max_length=20)
    formula_img = models.ImageField(upload_to='formulas/')

    def __str__(self):
        return f'{self.theme} - {self.name}'

    class Meta:
        verbose_name = 'Формула'
        verbose_name_plural = 'Формулы'
