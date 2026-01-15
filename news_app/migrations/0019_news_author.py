from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news_app", "0018_newsimage_video"),
    ]

    operations = [
        migrations.AddField(
            model_name="news",
            name="author",
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
