from django.contrib import admin
from .models import Translation,Contact,Advantage,Statistics,Partner
from .models import News,NewsImage
from .models import ShareholderMeeting,ShareholderMeetingFile
from .models import DevelopmentStrategy,DevelopmentStrategyFile
from .models import InternalDocumentFile,InternalDocument
from .models import BusinessPlanFile,BusinessPlan
from .models import DividendFile,Dividend
from .models import ReportFile,Report
from .models import CharterFile,Charter
from .models import EmissionProspectusFile,EmissionProspectus
from .models import AuditReportFile,AuditReport
from .models import ImportantFactFile,ImportantFact
from .models import ComplyExplainFile,ComplyExplain
from .models import AffiliatedPersonFile,AffiliatedPerson
from .models import ManagementTeam
from .models import ResumeTemplate
from .models import Vacancy
from .models import SupervisoryBoardMember
from .models import OrganizationStructureFile,OrganizationStructure
from .models import AboutCompanyChronology,AboutCompany
from .models import ProjectImage,Project
from .models import Activity


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
    
    




@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "title",
        "created_at"
    )

    search_fields = (
        "title",
    )
    



class NewsImageInline(admin.TabularInline):

    model=NewsImage
    extra=1


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):

    list_display=(
        "id",
        "title_uz",
        "news_date",
        "created_at"
    )

    list_filter=(
        "news_date",
    )

    search_fields=(
        "title_uz",
        "title_ru",
        "title_en"
    )

    date_hierarchy="news_date"

    inlines=[
        NewsImageInline
    ]
    
    






class ShareholderMeetingFileInline(admin.TabularInline):

    model=ShareholderMeetingFile
    extra=1


@admin.register(ShareholderMeeting)
class ShareholderMeetingAdmin(admin.ModelAdmin):

    list_display=(
        "id",
        "title_uz",
        "created_at"
    )

    search_fields=(
        "title_uz",
        "title_ru",
        "title_en"
    )

    inlines=[
        ShareholderMeetingFileInline
    ]

    def has_add_permission(self,request):

        return not ShareholderMeeting.objects.exists()
    
    
    
class DevelopmentStrategyFileInline(admin.TabularInline):

    model=DevelopmentStrategyFile
    extra=1


@admin.register(DevelopmentStrategy)
class DevelopmentStrategyAdmin(admin.ModelAdmin):

    list_display=(
        "id",
        "title_uz",
        "created_at"
    )

    search_fields=(
        "title_uz",
        "title_ru",
        "title_en"
    )

    inlines=[
        DevelopmentStrategyFileInline
    ]

    def has_add_permission(self,request):

        return not DevelopmentStrategy.objects.exists()

    def has_delete_permission(self,request,obj=None):

        return False
    
    
    
class InternalDocumentFileInline(admin.TabularInline):

    model=InternalDocumentFile
    extra=1


@admin.register(InternalDocument)
class InternalDocumentAdmin(admin.ModelAdmin):

    list_display=(
        "id",
        "title_uz",
        "created_at"
    )

    search_fields=(
        "title_uz",
        "title_ru",
        "title_en"
    )

    inlines=[
        InternalDocumentFileInline
    ]

    def has_add_permission(self,request):

        return not InternalDocument.objects.exists()

    def has_delete_permission(self,request,obj=None):

        return False
    
    

class BusinessPlanFileInline(admin.TabularInline):

    model=BusinessPlanFile
    extra=1


@admin.register(BusinessPlan)
class BusinessPlanAdmin(admin.ModelAdmin):

    list_display=(
        "id",
        "title_uz",
        "created_at"
    )

    search_fields=(
        "title_uz",
        "title_ru",
        "title_en"
    )

    inlines=[
        BusinessPlanFileInline
    ]

    def has_add_permission(self,request):

        return not BusinessPlan.objects.exists()

    def has_delete_permission(self,request,obj=None):

        return False
    
    
class DividendFileInline(admin.TabularInline):

    model=DividendFile
    extra=1


@admin.register(Dividend)
class DividendAdmin(admin.ModelAdmin):

    list_display=(
        "id",
        "title_uz",
        "created_at"
    )

    search_fields=(
        "title_uz",
        "title_ru",
        "title_en"
    )

    inlines=[
        DividendFileInline
    ]

    def has_add_permission(self,request):

        return not Dividend.objects.exists()

    def has_delete_permission(self,request,obj=None):

        return False
    
    
class ReportFileInline(admin.TabularInline):

    model=ReportFile
    extra=1


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):

    list_display=(
        "id",
        "title_uz",
        "created_at"
    )

    search_fields=(
        "title_uz",
        "title_ru",
        "title_en"
    )

    inlines=[
        ReportFileInline
    ]

    def has_add_permission(self,request):

        return not Report.objects.exists()

    def has_delete_permission(self,request,obj=None):

        return False
    
    
class CharterFileInline(admin.TabularInline):

    model=CharterFile
    extra=1


@admin.register(Charter)
class CharterAdmin(admin.ModelAdmin):

    list_display=(
        "id",
        "title_uz",
        "created_at"
    )

    search_fields=(
        "title_uz",
        "title_ru",
        "title_en"
    )

    inlines=[
        CharterFileInline
    ]

    def has_add_permission(self,request):

        return not Charter.objects.exists()

    def has_delete_permission(self,request,obj=None):

        return False
    
    
class EmissionProspectusFileInline(admin.TabularInline):

    model=EmissionProspectusFile
    extra=1


@admin.register(EmissionProspectus)
class EmissionProspectusAdmin(admin.ModelAdmin):

    list_display=(
        "id",
        "title_uz",
        "created_at"
    )

    search_fields=(
        "title_uz",
        "title_ru",
        "title_en"
    )

    inlines=[
        EmissionProspectusFileInline
    ]

    def has_add_permission(self,request):

        return not EmissionProspectus.objects.exists()

    def has_delete_permission(self,request,obj=None):

        return False
    
    
class AuditReportFileInline(admin.TabularInline):

    model=AuditReportFile
    extra=1


@admin.register(AuditReport)
class AuditReportAdmin(admin.ModelAdmin):

    list_display=(
        "id",
        "title_uz",
        "created_at"
    )

    search_fields=(
        "title_uz",
        "title_ru",
        "title_en"
    )

    inlines=[
        AuditReportFileInline
    ]

    def has_add_permission(self,request):

        return not AuditReport.objects.exists()

    def has_delete_permission(self,request,obj=None):

        return False
    
    
class ImportantFactFileInline(admin.TabularInline):

    model=ImportantFactFile
    extra=1


@admin.register(ImportantFact)
class ImportantFactAdmin(admin.ModelAdmin):

    list_display=(
        "id",
        "title_uz",
        "created_at"
    )

    search_fields=(
        "title_uz",
        "title_ru",
        "title_en"
    )

    inlines=[
        ImportantFactFileInline
    ]

    def has_add_permission(self,request):

        return not ImportantFact.objects.exists()

    def has_delete_permission(self,request,obj=None):

        return False
    
    
class ComplyExplainFileInline(admin.TabularInline):

    model=ComplyExplainFile
    extra=1


@admin.register(ComplyExplain)
class ComplyExplainAdmin(admin.ModelAdmin):

    list_display=(
        "id",
        "title_uz",
        "created_at"
    )

    search_fields=(
        "title_uz",
        "title_ru",
        "title_en"
    )

    inlines=[
        ComplyExplainFileInline
    ]

    def has_add_permission(self,request):

        return not ComplyExplain.objects.exists()

    def has_delete_permission(self,request,obj=None):

        return False
    
    
class AffiliatedPersonFileInline(admin.TabularInline):

    model=AffiliatedPersonFile
    extra=1


@admin.register(AffiliatedPerson)
class AffiliatedPersonAdmin(admin.ModelAdmin):

    list_display=(
        "id",
        "title_uz",
        "created_at"
    )

    search_fields=(
        "title_uz",
        "title_ru",
        "title_en"
    )

    inlines=[
        AffiliatedPersonFileInline
    ]

    def has_add_permission(self,request):

        return not AffiliatedPerson.objects.exists()

    def has_delete_permission(self,request,obj=None):

        return False
    
    
@admin.register(ManagementTeam)
class ManagementTeamAdmin(admin.ModelAdmin):

    list_display=(
        "id",
        "full_name_uz",
        "position_uz",
        "phone_number",
        "order"
    )

    list_editable=(
        "order",
    )

    search_fields=(
        "full_name_uz",
        "full_name_ru",
        "full_name_en",
        "position_uz",
        "position_ru",
        "position_en"
    )

    ordering=("order",)
    
    
@admin.register(ResumeTemplate)
class ResumeTemplateAdmin(admin.ModelAdmin):

    list_display=(
        "id",
        "updated_at"
    )

    def has_add_permission(self,request):

        return not ResumeTemplate.objects.exists()

    def has_delete_permission(self,request,obj=None):

        return False
    
    
@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):

    list_display=(
        "id",
        "title_uz",
        "created_at"
    )

    search_fields=(
        "title_uz",
        "title_ru",
        "title_en"
    )

    ordering=(
        "-id",
    )
    
    
@admin.register(SupervisoryBoardMember)
class SupervisoryBoardMemberAdmin(admin.ModelAdmin):

    list_display=(
        "order",
        "full_name_uz",
        "position_uz",
        "is_auditor"
    )

    list_filter=(
        "is_auditor",
    )

    search_fields=(
        "full_name_uz",
        "full_name_ru",
        "full_name_en",
        "position_uz",
        "position_ru",
        "position_en"
    )

    ordering=(
        "order",
    )
    
class OrganizationStructureFileInline(admin.TabularInline):

    model=OrganizationStructureFile
    extra=1


@admin.register(OrganizationStructure)
class OrganizationStructureAdmin(admin.ModelAdmin):

    list_display=(
        "id",
        "title_uz",
        "created_at"
    )

    search_fields=(
        "title_uz",
        "title_ru",
        "title_en"
    )

    inlines=[
        OrganizationStructureFileInline
    ]

    def has_add_permission(self,request):

        return not OrganizationStructure.objects.exists()

    def has_delete_permission(self,request,obj=None):

        return False
    
    
class AboutCompanyChronologyInline(admin.TabularInline):

    model=AboutCompanyChronology
    extra=1


@admin.register(AboutCompany)
class AboutCompanyAdmin(admin.ModelAdmin):

    list_display=(
        "id",
        "title_uz",
        "created_at"
    )

    inlines=[
        AboutCompanyChronologyInline
    ]

    def has_add_permission(self,request):

        return not AboutCompany.objects.exists()

    def has_delete_permission(self,request,obj=None):

        return False
    
    
class ProjectImageInline(admin.TabularInline):

    model=ProjectImage
    extra=1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display=(
        "id",
        "title_uz",
        "period",
        "created_at"
    )

    search_fields=(
        "title_uz",
        "title_ru",
        "title_en"
    )

    list_filter=(
        "created_at",
    )

    readonly_fields=(
        "created_at",
    )

    inlines=[
        ProjectImageInline
    ]
    
    
@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "title_uz",
        "created_at"
    )

    search_fields = (
        "title_uz",
        "title_ru",
        "title_en"
    )