import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news_app", "0016_remove_category_name_en_remove_category_name_ru_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="NewsImage",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("image", models.ImageField(upload_to="news/images")),
                ("created_time", models.DateTimeField(auto_now_add=True)),
                (
                    "news",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="images", to="news_app.news"),
                ),
            ],
            options={
                "ordering": ["created_time", "id"],
            },
        ),
    ]
