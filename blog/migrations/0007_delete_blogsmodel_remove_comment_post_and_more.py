# Generated by Django 4.2.6 on 2023-11-02 18:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0006_health_hacks"),
    ]

    operations = [
        migrations.DeleteModel(
            name="BlogsModel",
        ),
        migrations.RemoveField(
            model_name="comment",
            name="post",
        ),
        migrations.RemoveField(
            model_name="health_hacks",
            name="user",
        ),
        migrations.DeleteModel(
            name="Image",
        ),
        migrations.RemoveField(
            model_name="post",
            name="author",
        ),
        migrations.DeleteModel(
            name="Comment",
        ),
        migrations.DeleteModel(
            name="Health_hacks",
        ),
        migrations.DeleteModel(
            name="Post",
        ),
    ]
