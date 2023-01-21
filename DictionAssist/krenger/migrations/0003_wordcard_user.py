# Generated by Django 4.1.5 on 2023-01-20 21:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("krenger", "0002_rename_word_wordcard_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="wordcard",
            name="user",
            field=models.ForeignKey(
                default=False,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]