# Generated by Django 4.1.1 on 2022-12-11 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bmstu_lab', '0002_remove_articles_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='photo_link',
            field=models.CharField(default='no_link', max_length=100),
        ),
    ]
