from django.contrib import admin
from django.template.defaultfilters import title

from .models import News, Category, Contact, Comment, Advertisement, FooterBlock, AboutPage, FeaturedCategory, ContactInfo, NewsImage
# Register your models here.


class NewsImageInline(admin.TabularInline):
    model = NewsImage
    extra = 1


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'publish_time', 'status']
    list_filter = ['status', 'created_time', 'publish_time']
    prepopulated_fields = {"slug": ('title',)}
    date_hierarchy = 'publish_time'
    search_fields = ['title', 'body']
    ordering = ['status', 'publish_time']
    inlines = [NewsImageInline]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

admin.site.register(Contact)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'body', 'created_time', 'active']
    list_filter = ['active', 'created_time']
    search_fields = ['user', 'body']
    actions = ['disable_comments', 'activate_comments']

    def disable_comments(self, request, queryset):
        queryset.update(active=False)
        
    def activate_comments(self, request, queryset):
        queryset.update(active=True)


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'display_order', 'created_time']
    list_filter = ['is_active']
    search_fields = ['title']
    ordering = ['display_order', '-created_time']


@admin.register(FooterBlock)
class FooterBlockAdmin(admin.ModelAdmin):
    list_display = ['key', 'title', 'updated_time']
    search_fields = ['title', 'description']


@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'updated_time']
    list_filter = ['is_active']
    search_fields = ['title', 'subtitle', 'body']


@admin.register(FeaturedCategory)
class FeaturedCategoryAdmin(admin.ModelAdmin):
    list_display = ['category', 'display_order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['category__name']
    ordering = ['display_order']


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ['title', 'address', 'phone', 'email', 'updated_time']
    search_fields = ['title', 'address', 'phone', 'email']
