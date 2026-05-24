from django.contrib import admin
from .models import Translation,Contact,Advantage,Statistics


@admin.register(Translation)
class TranslationAdmin(admin.ModelAdmin):

    list_display = (
        "key",
        "short_uz",
        "short_ru",
        "short_en",
    )

    search_fields = (
        "key",
        "uz",
        "ru",
        "en",
    )

    ordering = ("key",)

    list_per_page = 50

    fieldsets = (
        (
            "Translation",
            {
                "fields": (
                    "key",
                    "uz",
                    "ru",
                    "en",
                )
            },
        ),
    )

    def short_uz(self, obj):
        return obj.uz[:50] if obj.uz else ""

    def short_ru(self, obj):
        return obj.ru[:50] if obj.ru else ""

    def short_en(self, obj):
        return obj.en[:50] if obj.en else ""

    short_uz.short_description = "UZ"
    short_ru.short_description = "RU"
    short_en.short_description = "EN"
    
    
    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    fields=(
        "title_uz",
        "title_ru",
        "title_en",
        "address_uz",
        "address_ru",
        "address_en",
        "phone",
        "email",
    )

    def has_add_permission(self,request):
        return not Contact.objects.exists()
    
    
@admin.register(Advantage)
class AdvantageAdmin(admin.ModelAdmin):

    list_display=("title_uz","created_at")

    fields=(
        "image",

        "title_uz",
        "title_ru",
        "title_en",

        "description_uz",
        "description_ru",
        "description_en",
    )

    def has_add_permission(self,request):
        return Advantage.objects.count()<6
    
    
    
@admin.register(Statistics)
class StatisticsAdmin(admin.ModelAdmin):
    list_display=[
        "years_of_experience",
        "count_projects_done",
        "in_process_count",
        "our_partnership_count"
    ]

    readonly_fields=["created_at"]

    fieldsets=(
        ("Experience",{
            "fields":(
                "years_of_experience",
                "experience_image_icon",
                "experience_title_uz",
                "experience_title_ru",
                "experience_title_en",
            )
        }),

        ("Projects Done",{
            "fields":(
                "count_projects_done",
                "projects_done_image_icon",
                "projects_done_title_uz",
                "projects_done_title_ru",
                "projects_done_title_en",
            )
        }),

        ("In Process",{
            "fields":(
                "in_process_count",
                "in_process_image_icon",
                "in_process_title_uz",
                "in_process_title_ru",
                "in_process_title_en",
            )
        }),

        ("Our Partnership",{
            "fields":(
                "our_partnership_count",
                "our_partnership_image_icon",
                "our_partnership_title_uz",
                "our_partnership_title_ru",
                "our_partnership_title_en",
            )
        }),

        ("Home Page",{
            "fields":(
                "home_page_bg_icon",
            )
        }),

        ("Company Video",{
            "fields":(
                "company_video_bg_image",
                "company_video",
            )
        }),
            )

    def has_add_permission(self,request):
        return not Statistics.objects.exists()