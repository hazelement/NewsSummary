# Generated by Django 2.2 on 2019-04-22 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urldigestiondbmodel',
            name='publish_date',
            field=models.TextField(default=''),
        ),
    ]