import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news_app", "0017_newsimage"),
    ]

    operations = [
        migrations.AddField(
            model_name="newsimage",
            name="video",
            field=models.FileField(blank=True, null=True, upload_to="news/videos"),
        ),
    ]
