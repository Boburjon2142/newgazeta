from django.db import migrations


def remap_categories(apps, schema_editor):
    Category = apps.get_model('news_app', 'Category')
    News = apps.get_model('news_app', 'News')

    mapping = {
        "Mahalliy": "Oila",
        "Xorij": "Jamiyat",
        "Sport": "Turizm",
        "Texnologiya": "Tibbiyot",
    }

    # Ensure target categories exist
    for new_name in mapping.values():
        Category.objects.get_or_create(name=new_name)

    for old_name, new_name in mapping.items():
        try:
            old_cat = Category.objects.get(name=old_name)
        except Category.DoesNotExist:
            continue
        new_cat = Category.objects.get(name=new_name)
        News.objects.filter(category=old_cat).update(category=new_cat)
        # optionally remove old category if unused
        if not News.objects.filter(category=old_cat).exists():
            old_cat.delete()


def reverse_remap(apps, schema_editor):
    # No safe reverse because data may have changed; noop
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0010_seed_new_categories'),
    ]

    operations = [
        migrations.RunPython(remap_categories, reverse_code=reverse_remap),
    ]
