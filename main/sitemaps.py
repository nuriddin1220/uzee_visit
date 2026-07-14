from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import News

LANGUAGES = ["uz", "ru", "en"]


class StaticSitemap(Sitemap):

    protocol = "https"

    def items(self):
        pages = [
            "home_lang",
            "contact",
            "news_list",
            "shareholders_meeting",
            "development_strategy",
            "internal_documents",
            "business_plan",
            "dividends",
            "reports",
            "charter",
            "emission_prospectus",
            "audit_report",
            "important_facts",
            "comply_explain",
            "affiliated_persons",
            "management_team",
            "vacancies",
            "supervisory_board",
            "organizational_structure",
            "general_information",
            "projects",
            "activity_list",
        ]

        return [
            (lang, page)
            for lang in LANGUAGES
            for page in pages
        ]

    def location(self, item):
        lang, page = item
        return reverse(page, kwargs={"lang": lang})


class NewsSitemap(Sitemap):

    protocol = "https"
    priority = 0.8
    changefreq = "weekly"

    def items(self):
        return [
            (lang, news)
            for lang in LANGUAGES
            for news in News.objects.only("id", "created_at")
        ]

    def location(self, item):
        lang, news = item
        return reverse(
            "news_detail",
            kwargs={
                "lang": lang,
                "id": news.id,
            },
        )

    def lastmod(self, item):
        _, news = item
        return news.created_at