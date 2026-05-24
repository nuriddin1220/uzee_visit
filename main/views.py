from django.shortcuts import render
from django.shortcuts import redirect
from .models import Contact,Advantage,Statistics


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



    return render(request,"index.html",{"advantages":advantages,"statistics":statistics})



def contact(request,lang=None):

    c=Contact.objects.first()

    return render(request,"contact.html",{
        "contact":c,
        "title":c.get_title(request.CURRENT_LANG) if c else "",
        "address":c.get_address(request.CURRENT_LANG) if c else "",
    })