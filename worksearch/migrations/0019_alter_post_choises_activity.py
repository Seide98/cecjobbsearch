# Generated by Django 3.2.6 on 2021-08-23 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worksearch', '0018_rename_ws_activity_post_choises_activity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='choises_activity',
            field=models.CharField(choices=[('Work application', 'Work application'), ('Registration of interest', 'Registration of interest'), ('Other activity', 'Other activity')], default='Work application', max_length=25),
        ),
    ]
