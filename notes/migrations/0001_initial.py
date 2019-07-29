# Generated by Django 2.2.3 on 2019-07-29 00:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(blank=True)),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]
