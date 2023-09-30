from django.db import models
from django.core.validators import MinValueValidator

class Post (models.Model):

    image = models.ImageField(verbose_name='이미지')
    content = models.TextField('내용')
    created_at = models.DateTimeField('작성일')
    view_count = models.IntegerField('조회수')

class Profile(models.Model):
    BACKEND = '백엔드'
    FRONTEND = '프론트엔드'
    PART_CHOICES = [
        (BACKEND, '백엔드'),
        (FRONTEND, '프론트엔드'),
    ]

    name = models.CharField('이름', max_length=100)
    age = models.PositiveIntegerField('나이', validators=[MinValueValidator(20)])
    part = models.CharField('파트', max_length=10,choices=PART_CHOICES)
    interest_field = models.TextField('관심 분야', blank=True)
    website_url = models.URLField('내 사이트 URL', unique=True)

# Create your models here.
