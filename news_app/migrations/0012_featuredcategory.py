from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0011_remap_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturedCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_order', models.PositiveIntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='featured_slots', to='news_app.category')),
            ],
            options={
                'verbose_name': 'Featured category',
                'verbose_name_plural': 'Featured categories',
                'ordering': ['display_order', 'id'],
            },
        ),
    ]
