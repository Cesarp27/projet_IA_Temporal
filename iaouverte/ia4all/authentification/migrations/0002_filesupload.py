# Generated by Django 4.1.2 on 2023-03-09 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentification", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="FilesUpload",
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
                ("userid", models.IntegerField()),
                ("file", models.FileField(upload_to="")),
            ],
        ),
    ]
