# Generated by Django 3.2.6 on 2021-08-11 09:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('worksearch', '0002_alter_post_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date_added',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
