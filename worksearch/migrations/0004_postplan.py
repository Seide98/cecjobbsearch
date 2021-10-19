# Generated by Django 3.2.6 on 2021-08-11 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worksearch', '0003_post_date_added'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('link', models.CharField(max_length=255)),
                ('date_added', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
