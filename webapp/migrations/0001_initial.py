# Generated by Django 4.2.1 on 2023-05-30 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Movies",
            fields=[
                ("index", models.IntegerField()),
                ("budget", models.IntegerField()),
                ("homepage", models.CharField(max_length=100)),
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("keywords", models.CharField(max_length=300)),
                ("original_title", models.CharField(max_length=200)),
                ("overview", models.TextField()),
                ("popularity", models.IntegerField()),
                ("production_companies", models.CharField(max_length=500)),
                ("production_countries", models.CharField(max_length=200)),
                ("release_date", models.CharField(max_length=100)),
                ("revenue", models.IntegerField()),
                ("runtime", models.IntegerField()),
                ("spoken_languages", models.CharField(max_length=300)),
                ("status", models.CharField(max_length=100)),
                ("tagline", models.TextField()),
                ("title", models.CharField(max_length=200)),
                ("vote_average", models.CharField(max_length=100)),
                ("vote_count", models.IntegerField()),
                ("cast", models.TextField()),
                ("crew", models.TextField()),
                ("director", models.TextField()),
            ],
        ),
    ]
