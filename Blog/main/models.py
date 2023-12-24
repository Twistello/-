from django.db import models

# Create your models
class Post(models.Model):
    '''Данные о посте'''
    author = models.CharField("Имя автора", max_length=30)
    theme = models.CharField('Тема поста',max_length=50)
    article = models.TextField('Текст поста', max_length=300)
    date = models.DateTimeField('Дата публикации')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return f'{self.theme}, {self.author}'


