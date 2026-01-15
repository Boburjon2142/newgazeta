from django.urls import reverse
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=News.Status.Published)

class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

# Create your models here.
class News(models.Model):

    class Status(models.TextChoices):
        Draft = "DF", "Draft"
        Published = "PB", "Published"

    title = models.CharField(max_length=250)
    slug =  models.SlugField(max_length=250)
    body = models.TextField()
    image = models.ImageField(upload_to='news/images')
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE
                                 )
    publish_time = models.DateTimeField(default=timezone.now)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_Time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.Draft,
                              )
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ["-publish_time"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("news_detail_page", args=[self.slug])

    @property
    def primary_image(self):
        if self.image:
            return self.image
        extra = getattr(self, "images", None)
        if extra:
            return extra.first().image if extra.exists() else None
        return None



class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.email

class ContactInfo(models.Model):
    title = models.CharField(max_length=200, default="Aloqa ma'lumotlari")
    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Contact info"
        verbose_name_plural = "Contact info"

    def __str__(self):
        return self.title or "Aloqa ma'lumotlari"
    
class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_time']

    def __str__(self):
        return f'Comment - {self.body} by {self.user}'
    
class ViewCount(models.Model):
    ip_adress = models.GenericIPAddressField()



class FooterBlock(models.Model):
    class FooterKey(models.TextChoices):
        FLICKR = "flickr", "Flickr Images"
        ABOUT = "about", "About / Contact"

    key = models.CharField(max_length=20, choices=FooterKey.choices, unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='footer/', blank=True, null=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Footer block"
        verbose_name_plural = "Footer blocks"

    def __str__(self):
        return self.title


class FeaturedCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='featured_slots')
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['display_order', 'id']
        verbose_name = "Featured category"
        verbose_name_plural = "Featured categories"

    def __str__(self):
        return f"{self.category.name} (order {self.display_order})"

class AboutPage(models.Model):
    title = models.CharField(max_length=200, default="Biz haqimizda")
    subtitle = models.CharField(max_length=255, blank=True)
    body = models.TextField(blank=True)
    bullet_one = models.CharField(max_length=200, blank=True)
    bullet_two = models.CharField(max_length=200, blank=True)
    bullet_three = models.CharField(max_length=200, blank=True)
    hero_image = models.ImageField(upload_to='about/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "About page"
        verbose_name_plural = "About pages"

    def __str__(self):
        return self.title
class Advertisement(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='ads/', blank=True, null=True)
    link = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=0)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['display_order', '-created_time']

    def __str__(self):
        return self.title

    @property
    def has_image(self):
        return bool(self.image)


class NewsImage(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="news/images")
    video = models.FileField(upload_to="news/videos", blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_time", "id"]

    def __str__(self):
        return f"{self.news.title} image"
 
