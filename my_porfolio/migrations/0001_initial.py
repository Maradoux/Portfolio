# Generated by Django 5.1.6 on 2025-03-05 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='project/')),
                ('link', models.CharField(blank=True, max_length=200, null=True)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
