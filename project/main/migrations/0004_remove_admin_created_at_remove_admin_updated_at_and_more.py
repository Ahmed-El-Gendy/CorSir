# Generated by Django 5.1.2 on 2024-10-31 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_usercourse_done'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='admin',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='course',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='course',
            name='video',
        ),
        migrations.RemoveField(
            model_name='usercourse',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='course',
            name='video_url',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]