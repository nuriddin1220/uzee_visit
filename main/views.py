from django.shortcuts import render,redirect,get_object_or_404
from .models import (Contact,
                     Advantage,
                     Statistics,
                     News,
                     ShareholderMeeting,
                     DevelopmentStrategy,
                     InternalDocument,
                     BusinessPlan,
                     Dividend,
                     Report,
                     Charter,
                     EmissionProspectus,
                     AuditReport,
                     ImportantFact,
                     ComplyExplain,
                     AffiliatedPerson,
                     ManagementTeam,
                     Vacancy,
                     ResumeTemplate,
                     SupervisoryBoardMember,
                     OrganizationStructure,
                     AboutCompany,
                     Project,
                     Activity)
from django.core.paginator import Paginator
from django.db.models import Count

def root_redirect(request):
    browser_lang = request.META.get(
        "HTTP_ACCEPT_LANGUAGE",
        ""
    ).lower()
    if browser_lang.startswith("ru"):
        lang = "ru"
    elif browser_lang.startswith("en"):
        lang = "en"
    else:
        lang = "uz"

    return redirect(f"/{lang}/")




def home(request,lang=None):

    advantages=Advantage.objects.all()

    lang=request.CURRENT_LANG
    
    advantages=[{
        "image":i.image,
        "title":getattr(i,f"title_{lang}"),
        "description":getattr(i,f"description_{lang}")
    } for i in Advantage.objects.all()]



    news_list=[{
        "id":i.id,
        "title":getattr(i,f"title_{lang}"),
        "text":getattr(i,f"text_{lang}"),
        "first_image":i.first_image(),
        "images_count":i.images_count(),
        "social_link":i.social_link,
        "news_date":i.news_date
    } for i in News.objects.all()[:3]]

    s=Statistics.objects.first()

    statistics={
        "years_of_experience":s.years_of_experience,
        "experience_image_icon":s.experience_image_icon,
        "experience_title":getattr(s,f"experience_title_{lang}"),

        "count_projects_done":s.count_projects_done,
        "projects_done_image_icon":s.projects_done_image_icon,
        "projects_done_title":getattr(s,f"projects_done_title_{lang}"),

        "in_process_count":s.in_process_count,
        "in_process_image_icon":s.in_process_image_icon,
        "in_process_title":getattr(s,f"in_process_title_{lang}"),

        "our_partnership_count":s.our_partnership_count,
        "our_partnership_image_icon":s.our_partnership_image_icon,
        "our_partnership_title":getattr(s,f"our_partnership_title_{lang}"),

        "home_page_bg_icon":s.home_page_bg_icon,

        "company_video_bg_image":s.company_video_bg_image,
        "company_video":s.company_video
    }



    return render(request,"index.html",{"advantages":advantages,"statistics":statistics,"news_list":news_list})



def contact(request,lang=None):

    c=Contact.objects.first()

    return render(request,"contact.html",{
        "contact":c,
        "title":c.get_title(request.CURRENT_LANG) if c else "",
        "address":c.get_address(request.CURRENT_LANG) if c else "",
    })
    
    
def news_detail(request,lang,id):

    lang=request.CURRENT_LANG
    n=get_object_or_404(News,id=id)
    news={
        "id":n.id,
        "title":getattr(n,f"title_{lang}"),
        "text":getattr(n,f"text_{lang}"),
        "social_link":n.social_link,
        "news_date":n.news_date,
        "images":[i.image for i in n.images.all()],
        "images_count":n.images.count()
    }

    latest_news=[{
        "id":i.id,
        "title":getattr(i,f"title_{lang}"),
        "news_date":i.news_date
    } for i in News.objects.exclude(id=id)[:5]]

    return render(request,"news_detail.html",{
        "news":news,
        "latest_news":latest_news
    })
    
    
def news_list(request,lang=None):

    lang=request.CURRENT_LANG

    page_obj=Paginator(
        News.objects.prefetch_related("images").only(
            "id",
            "title_uz","title_ru","title_en",
            "text_uz","text_ru","text_en",
            "social_link",
            "news_date"
        ),
        6
    ).get_page(request.GET.get("page"))

    news_list=[{
        "id":i.id,
        "title":getattr(i,f"title_{lang}"),
        "text":getattr(i,f"text_{lang}"),
        "first_image":i.first_image(),
        "social_link":i.social_link,
        "news_date":i.news_date
    } for i in page_obj]

    return render(request,"news.html",{
        "news_list":news_list,
        "page_obj":page_obj
    })
    
    


def shareholders_meeting(request,lang=None):

    lang=request.CURRENT_LANG

    meeting=ShareholderMeeting.objects.prefetch_related("files").first()
    
    if meeting:

        meeting.title=getattr(
            meeting,
            f"title_{lang}"
        )
        meeting.description=getattr(
            meeting,
            f"description_{lang}"
        )

    page_obj=Paginator(
        meeting.files.all() if meeting else [],
        9
    ).get_page(request.GET.get("page"))

    files=[{
        "id":i.id,
        "title":getattr(i,f"title_{lang}"),
        "file":i.file
    } for i in page_obj]

    return render(request,"shareholders_meeting.html",{
        "meeting":meeting,
        "files":files,
        "page_obj":page_obj
    })
    
    
def development_strategy(request,lang=None):

    lang=request.CURRENT_LANG
    strategy=DevelopmentStrategy.objects.prefetch_related("files").first()
    if strategy:

        strategy.title=getattr(strategy,f"title_{lang}")
        strategy.description=getattr(strategy,f"description_{lang}")

    page_obj=Paginator(
        strategy.files.all() if strategy else [],
        9
    ).get_page(request.GET.get("page"))

    files=[{
        "id":i.id,
        "title":getattr(i,f"title_{lang}"),
        "file":i.file
    } for i in page_obj]

    return render(request,"development_strategy.html",{
        "strategy":strategy,
        "files":files,
        "page_obj":page_obj
    })
    
    
def internal_documents(request,lang=None):

    lang=request.CURRENT_LANG

    document=InternalDocument.objects.prefetch_related("files").first()

    if document:

        document.title=getattr(document,f"title_{lang}")
        document.description=getattr(document,f"description_{lang}")

    page_obj=Paginator(
        document.files.all() if document else [],
        9
    ).get_page(request.GET.get("page"))

    files=[{
        "id":i.id,
        "title":getattr(i,f"title_{lang}"),
        "file":i.file
    } for i in page_obj]

    return render(request,"internal_documents.html",{
        "document":document,
        "files":files,
        "page_obj":page_obj
    })
    
    
    
def business_plan(request,lang=None):

    lang=request.CURRENT_LANG

    plan=BusinessPlan.objects.prefetch_related("files").first()

    if plan:

        plan.title=getattr(plan,f"title_{lang}")
        plan.description=getattr(plan,f"description_{lang}")

    page_obj=Paginator(
        plan.files.all() if plan else [],
        9
    ).get_page(request.GET.get("page"))

    files=[{
        "id":i.id,
        "title":getattr(i,f"title_{lang}"),
        "file":i.file
    } for i in page_obj]

    return render(request,"business_plan.html",{
        "plan":plan,
        "files":files,
        "page_obj":page_obj
    })
    
    
def dividends(request,lang=None):

    lang=request.CURRENT_LANG

    dividend=Dividend.objects.prefetch_related("files").first()

    if dividend:

        dividend.title=getattr(dividend,f"title_{lang}")
        dividend.description=getattr(dividend,f"description_{lang}")

    page_obj=Paginator(
        dividend.files.all() if dividend else [],
        9
    ).get_page(request.GET.get("page"))

    files=[{
        "id":i.id,
        "title":getattr(i,f"title_{lang}"),
        "file":i.file
    } for i in page_obj]

    return render(request,"dividends.html",{
        "dividend":dividend,
        "files":files,
        "page_obj":page_obj
    })
    
def reports(request,lang=None):

    lang=request.CURRENT_LANG

    report=Report.objects.prefetch_related("files").first()

    if report:

        report.title=getattr(report,f"title_{lang}")
        report.description=getattr(report,f"description_{lang}")

    page_obj=Paginator(
        report.files.all() if report else [],
        9
    ).get_page(request.GET.get("page"))

    files=[{
        "id":i.id,
        "title":getattr(i,f"title_{lang}"),
        "file":i.file
    } for i in page_obj]

    return render(request,"reports.html",{
        "report":report,
        "files":files,
        "page_obj":page_obj
    })
    
def charter(request,lang=None):

    lang=request.CURRENT_LANG

    charter=Charter.objects.prefetch_related("files").first()

    if charter:

        charter.title=getattr(charter,f"title_{lang}")
        charter.description=getattr(charter,f"description_{lang}")

    page_obj=Paginator(
        charter.files.all() if charter else [],
        9
    ).get_page(request.GET.get("page"))

    files=[{
        "id":i.id,
        "title":getattr(i,f"title_{lang}"),
        "file":i.file
    } for i in page_obj]

    return render(request,"charter.html",{
        "charter":charter,
        "files":files,
        "page_obj":page_obj
    })
    


def emission_prospectus(request,lang=None):

    lang=request.CURRENT_LANG

    prospectus=EmissionProspectus.objects.prefetch_related("files").first()

    if prospectus:

        prospectus.title=getattr(prospectus,f"title_{lang}")
        prospectus.description=getattr(prospectus,f"description_{lang}")

    page_obj=Paginator(
        prospectus.files.all() if prospectus else [],
        9
    ).get_page(request.GET.get("page"))

    files=[{
        "id":i.id,
        "title":getattr(i,f"title_{lang}"),
        "file":i.file
    } for i in page_obj]

    return render(request,"emission_prospectus.html",{
        "prospectus":prospectus,
        "files":files,
        "page_obj":page_obj
    })
    
    
def audit_report(request,lang=None):

    lang=request.CURRENT_LANG

    report=AuditReport.objects.prefetch_related("files").first()

    if report:

        report.title=getattr(report,f"title_{lang}")
        report.description=getattr(report,f"description_{lang}")

    page_obj=Paginator(
        report.files.all() if report else [],
        9
    ).get_page(request.GET.get("page"))

    files=[{
        "id":i.id,
        "title":getattr(i,f"title_{lang}"),
        "file":i.file
    } for i in page_obj]

    return render(request,"audit_report.html",{
        "report":report,
        "files":files,
        "page_obj":page_obj
    })
    
    
def important_facts(request,lang=None):

    lang=request.CURRENT_LANG

    fact=ImportantFact.objects.prefetch_related("files").first()

    if fact:

        fact.title=getattr(fact,f"title_{lang}")
        fact.description=getattr(fact,f"description_{lang}")

    page_obj=Paginator(
        fact.files.all() if fact else [],
        9
    ).get_page(request.GET.get("page"))

    files=[{
        "id":i.id,
        "title":getattr(i,f"title_{lang}"),
        "file":i.file
    } for i in page_obj]

    return render(request,"important_facts.html",{
        "fact":fact,
        "files":files,
        "page_obj":page_obj
    })
    
    
def comply_explain(request,lang=None):

    lang=request.CURRENT_LANG

    comply=ComplyExplain.objects.prefetch_related("files").first()

    if comply:

        comply.title=getattr(comply,f"title_{lang}")
        comply.description=getattr(comply,f"description_{lang}")

    page_obj=Paginator(
        comply.files.all() if comply else [],
        9
    ).get_page(request.GET.get("page"))

    files=[{
        "id":i.id,
        "title":getattr(i,f"title_{lang}"),
        "file":i.file
    } for i in page_obj]

    return render(request,"comply_explain.html",{
        "comply":comply,
        "files":files,
        "page_obj":page_obj
    })
    
    
def affiliated_persons(request,lang=None):

    lang=request.CURRENT_LANG

    person=AffiliatedPerson.objects.prefetch_related("files").first()

    if person:

        person.title=getattr(person,f"title_{lang}")
        person.description=getattr(person,f"description_{lang}")

    page_obj=Paginator(
        person.files.all() if person else [],
        9
    ).get_page(request.GET.get("page"))

    files=[{
        "id":i.id,
        "title":getattr(i,f"title_{lang}"),
        "file":i.file
    } for i in page_obj]

    return render(request,"affiliated_persons.html",{
        "person":person,
        "files":files,
        "page_obj":page_obj
    })
    
    


def management_team(request,lang=None):

    lang=request.CURRENT_LANG

    staff=[{
        "id":i.id,
        "full_name":getattr(i,f"full_name_{lang}"),
        "position":getattr(i,f"position_{lang}"),
        "reception_days":getattr(i,f"reception_days_{lang}"),
        "phone_number":i.phone_number,
        "biography":getattr(i,f"biography_{lang}"),
        "duty":getattr(i,f"duty_{lang}"),
        "image":i.image,
        "email":i.email,
        "order":i.order
    } for i in ManagementTeam.objects.all()]

    return render(request,"management_team.html",{
        "staff":staff,
        "active_menu":"management",})
    
    
    
def vacancies(request,lang=None):

    lang=request.CURRENT_LANG

    page_obj=Paginator(
        Vacancy.objects.all(),
        10
    ).get_page(request.GET.get("page"))

    vacancies=[{
        "id":i.id,
        "title":getattr(i,f"title_{lang}"),
        "description":getattr(i,f"description_{lang}")
    } for i in page_obj]
    
    resume_template=ResumeTemplate.objects.first()
    
    return render(
        request,
        "vacancies.html",
        {
            "vacancies":vacancies,
            "page_obj":page_obj,
            "active_menu":"vacancies",
            "resume_template":resume_template
        }
    )
    
    
def supervisory_board(request,lang=None):

    lang=request.CURRENT_LANG

    members=[
        {
            "id":i.id,
            "full_name":getattr(i,f"full_name_{lang}"),
            "position":getattr(i,f"position_{lang}")
        }
        for i in SupervisoryBoardMember.objects.filter(
            is_auditor=False
        )]

    auditors=[
        {
            "id":i.id,
            "full_name":getattr(i,f"full_name_{lang}"),
            "position":getattr(i,f"position_{lang}")
        }
        for i in SupervisoryBoardMember.objects.filter(
            is_auditor=True
        )]

    return render(request,"supervisory_board.html",
        {
            "members":members,
            "auditors":auditors,
            "active_menu":"supervisory_board"
        })
    
    
def organization_structure(request,lang=None):

    lang=request.CURRENT_LANG

    structure=OrganizationStructure.objects.prefetch_related("files").first()

    if structure:

        structure.title=getattr(structure,f"title_{lang}")
        structure.description=getattr(structure,f"description_{lang}")

    files=[{
        "id":i.id,
        "title":getattr(i,f"title_{lang}"),
        "file":i.file
    } for i in structure.files.all()] if structure else []

    return render(request,"organization_structure.html",{
        "structure":structure,
        "files":files,
        "active_menu":"organizational_structure"
    })
    
    
def general_information(request,lang=None):

    lang=request.CURRENT_LANG

    about=AboutCompany.objects.prefetch_related(
        "chronologies"
    ).first()

    if about:

        about.title=getattr(
            about,
            f"title_{lang}"
        )

        about.about_content=getattr(
            about,
            f"about_content_{lang}"
        )

    chronologies=[{
        "year":i.year,
        "description":getattr(
            i,
            f"description_{lang}"
        )
    } for i in about.chronologies.all()] if about else []

    return render(
        request,
        "general_information.html",
        {
            "general_information":about,
            "chronologies":chronologies,
            "active_menu":"general_information"
        }
    )
    
    
    
def projects(request,lang=None):

    lang=request.CURRENT_LANG
    
    page_obj=Paginator(Project.objects.all(),8).get_page(request.GET.get("page"))
    projects=[{
        "id":i.id,
        "title":getattr(i,f"title_{lang}"),
        "period":i.period,
        "first_image":i.first_image()
    } for i in page_obj]

    return render(request,"projects.html",
        {
            "projects":projects,
            "page_obj":page_obj
        })
    
    


def project_detail(request,lang,id):

    lang=request.CURRENT_LANG

    p=get_object_or_404(
        Project.objects.prefetch_related("images"),
        id=id
    )

    project={
        "id":p.id,
        "title":getattr(p,f"title_{lang}"),
        "description":getattr(p,f"description_{lang}"),
        "period":p.period,
        "images":[i.image for i in p.images.all()],
        "images_count":p.images.count()
    }


    return render(request,"project_detail.html",{"project":project,})





def activity_list(request, lang):

    lang = request.CURRENT_LANG

    activities = [{
        "id": i.id,
        "title": getattr(i, f"title_{lang}"),
        "description": getattr(i, f"description_{lang}"),
        "image": i.image.url
    } for i in Activity.objects.all()]

    return render(
        request,
        "activity_list.html",
        {
            "activities": activities
        }
    )
    

from django.http import HttpResponse
def robots_txt(request):
    sitemap_url = request.build_absolute_uri("/sitemap.xml")

    return HttpResponse(
        "\n".join([
            "User-Agent: *",
            "Allow: /",
            "",
            f"Sitemap: {sitemap_url}",
        ]),
        content_type="text/plain",
    )