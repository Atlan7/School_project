from django.db import models

from datetime import datetime

from slugify import slugify as slugify_ru


class Theme(models.Model):
    """ Тема из физики """
    name = models.CharField(max_length=225)
    slug = models.SlugField('Slug for theme', unique=True, max_length=300)

    def save(self,*args, **kwargs):
        if not self.slug:
            slug = slugify_ru(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'


class Formula(models.Model):
    """ Формула """     

    # Размерность 
    OPTIONS = [
        ('Вт', 'Ватты'),
        ('Дж', 'Джоули'),
        ('Кл', 'Кулоны'),
        ('Па', 'Паскали'),
        ('H', 'Ньютоны'),
        ('Ф', 'Фараты'),
        ('К', 'Кельвины'),
    ]

    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    name = models.CharField(max_length=225)
    description = models.TextField()
    dimension = models.CharField(OPTIONS, max_length=2)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    formula_img = models.ImageField(upload_to=f'formulas/author_{author.name}/')

    def __str__(self):
        return f'{self.theme} - {self.name}'

    class Meta:
        verbose_name = 'Формула'
        verbose_name_plural = 'Формулы'


class Author(models.Model):
    """ Автор формулы/закона/теории """
    first_name = models.CharField(max_length=225)
    second_name = models.CharField(max_length=225)
    date_of_birth = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.second_name}'
#
#    def get_age(self):
#        return datetime.today().year - self.date_of_birth.year

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
