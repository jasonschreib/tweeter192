# Generated by Django 3.2.9 on 2021-12-02 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweeterApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
