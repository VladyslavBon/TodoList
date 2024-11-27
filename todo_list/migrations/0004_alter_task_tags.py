# Generated by Django 5.1.3 on 2024-11-27 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo_list", "0003_alter_task_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="tags",
            field=models.ManyToManyField(related_name="tasks", to="todo_list.tag"),
        ),
    ]