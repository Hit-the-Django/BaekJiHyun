from django.db import models

class Post (models.Model):

    image = models.ImageField(verbose_name='이미지')
    content = models.TextField('내용')
    created_at = models.DateTimeField('작성일')
    view_count = models.IntegerField('조회수')

# Create your models here.
