# Generated by Django 3.2.6 on 2021-08-11 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worksearch', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='link',
            field=models.CharField(max_length=255),
        ),
    ]