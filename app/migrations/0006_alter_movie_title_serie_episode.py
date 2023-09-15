# Generated by Django 4.1.2 on 2023-07-07 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0005_alter_category_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="title",
            field=models.CharField(max_length=128),
        ),
        migrations.CreateModel(
            name="Serie",
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
                ("title", models.CharField(max_length=128)),
                ("description", models.CharField(max_length=250)),
                ("year", models.IntegerField()),
                ("image", models.ImageField(blank=True, null=True, upload_to="images")),
                ("created_at", models.DateField(auto_now_add=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.category"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Episode",
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
                ("name", models.CharField(max_length=128)),
                ("link1", models.CharField(blank=True, max_length=250, null=True)),
                ("link2", models.CharField(blank=True, max_length=250, null=True)),
                ("link3", models.CharField(blank=True, max_length=250, null=True)),
                ("created_at", models.DateField(auto_now_add=True)),
                (
                    "serie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.serie"
                    ),
                ),
            ],
        ),
    ]