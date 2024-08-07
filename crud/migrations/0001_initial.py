# Generated by Django 4.2 on 2024-06-29 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('content', models.CharField(max_length=100)),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('finish_time', models.DateTimeField()),
                ('is_complete', models.BooleanField(default=False)),
            ],
        ),
    ]
