from .models import News, Category, FooterBlock


def latest_news(request):
    latest_news = News.published.all().order_by("-publish_time")[:10]
    categories = Category.objects.all()
    footer_blocks = {fb.key: fb for fb in FooterBlock.objects.all()}
    desired_order = ["Jamiyat", "Jarayon", "Faoliyat", "Iqtisodiyot", "Tibbiyot", "Turizm", "Oila", "Biznes"]
    # Map by canonical (Latin) name for ordering, but return category objects so name is translated
    name_to_cat = {getattr(c, "name_uz", c.name): c for c in categories}
    nav_categories = [name_to_cat[n] for n in desired_order if n in name_to_cat]
    # append any other categories not in desired list
    for c in categories:
        base_name = getattr(c, "name_uz", c.name)
        if base_name not in desired_order:
            nav_categories.append(c)

    context = {
        'latest_news': latest_news,
        "categories":categories,
        "footer_blocks": footer_blocks,
        "nav_categories": nav_categories,
    }

    return context
