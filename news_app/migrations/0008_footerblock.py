from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0007_advertisement'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterBlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(choices=[('flickr', 'Flickr Images'), ('about', 'About / Contact')], max_length=20, unique=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='footer/')),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Footer block',
                'verbose_name_plural': 'Footer blocks',
            },
        ),
    ]
