# Generated by Django 4.2.3 on 2023-09-30 16:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='이미지')),
                ('content', models.TextField(verbose_name='내용')),
                ('created_at', models.DateTimeField(verbose_name='작성일')),
                ('view_count', models.IntegerField(verbose_name='조회수')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='이름')),
                ('age', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(20)], verbose_name='나이')),
                ('part', models.CharField(choices=[('백엔드', '백엔드'), ('프론트엔드', '프론트엔드')], max_length=10, verbose_name='파트')),
                ('interest_field', models.TextField(blank=True, verbose_name='관심 분야')),
                ('website_url', models.URLField(unique=True, verbose_name='내 사이트 URL')),
            ],
        ),
    ]
