# Generated by Django 4.1.1 on 2023-01-07 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bmstu_lab', '0006_articles_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='photo',
            field=models.ImageField(default='None', upload_to='photos'),
        ),
    ]