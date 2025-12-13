from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0008_footerblock'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Biz haqimizda', max_length=200)),
                ('subtitle', models.CharField(blank=True, max_length=255)),
                ('body', models.TextField(blank=True)),
                ('bullet_one', models.CharField(blank=True, max_length=200)),
                ('bullet_two', models.CharField(blank=True, max_length=200)),
                ('bullet_three', models.CharField(blank=True, max_length=200)),
                ('hero_image', models.ImageField(blank=True, null=True, upload_to='about/')),
                ('is_active', models.BooleanField(default=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'About page',
                'verbose_name_plural': 'About pages',
            },
        ),
    ]
