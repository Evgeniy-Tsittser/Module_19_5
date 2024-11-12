# Generated by Django 5.1.3 on 2024-11-12 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
