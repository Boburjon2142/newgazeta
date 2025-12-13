from django.db import migrations


def seed_categories(apps, schema_editor):
    Category = apps.get_model('news_app', 'Category')
    names = [
        "Jamiyat",
        "Jarayon",
        "Faoliyat",
        "Iqtisodiyot",
        "Tibbiyot",
        "Turizm",
        "Oila",
        "Biznes",
    ]
    for name in names:
        Category.objects.get_or_create(name=name)


def unseed_categories(apps, schema_editor):
    Category = apps.get_model('news_app', 'Category')
    names = [
        "Jamiyat",
        "Jarayon",
        "Faoliyat",
        "Iqtisodiyot",
        "Tibbiyot",
        "Turizm",
        "Oila",
        "Biznes",
    ]
    Category.objects.filter(name__in=names).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0009_aboutpage'),
    ]

    operations = [
        migrations.RunPython(seed_categories, reverse_code=unseed_categories),
    ]
