# Generated by Django 4.1.7 on 2023-05-15 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goroskop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('full_text', models.TextField(verbose_name='Статья')),
                ('date', models.DateTimeField(verbose_name='Дата и Время')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Нововсти',
            },
        ),
        migrations.AlterModelOptions(
            name='artiles',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Нововсти'},
        ),
    ]
