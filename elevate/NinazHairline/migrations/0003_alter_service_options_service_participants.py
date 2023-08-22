# Generated by Django 4.2.4 on 2023-08-22 14:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('NinazHairline', '0002_topic_service_host_message_service_topic'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['-updated', '-created']},
        ),
        migrations.AddField(
            model_name='service',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='participants', to=settings.AUTH_USER_MODEL),
        ),
    ]
