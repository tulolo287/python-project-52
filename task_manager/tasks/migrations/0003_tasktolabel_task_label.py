# Generated by Django 5.2 on 2025-06-17 20:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("labels", "0001_initial"),
        ("tasks", "0002_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="TaskToLabel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "label",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="labels.label",
                    ),
                ),
                (
                    "task",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tasks.task",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="task",
            name="label",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                through="tasks.TaskToLabel",
                to="labels.label",
            ),
        ),
    ]
