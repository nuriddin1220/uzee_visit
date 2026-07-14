from django.urls import path
from .views import (home,
                    root_redirect,
                    contact,
                    news_detail,
                    news_list,
                    shareholders_meeting,
                    development_strategy,
                    internal_documents,
                    business_plan,
                    dividends,
                    reports,
                    charter,
                    emission_prospectus,
                    audit_report,
                    important_facts,
                    comply_explain,
                    affiliated_persons,
                    management_team,
                    vacancies,
                    supervisory_board,
                    organization_structure,
                    general_information,
                    projects,
                    project_detail,
                    activity_list,
                    robots_txt)

from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticSitemap, NewsSitemap

sitemaps = {
    "static": StaticSitemap,
    "news": NewsSitemap,
}




urlpatterns = [
    path("", root_redirect),
    path("<str:lang>/", home, name="home_lang"),
    path("<str:lang>/contact/", contact, name="contact"),
    path("<str:lang>/news/<int:id>/",news_detail,name="news_detail"),
    path("<str:lang>/news/",news_list,name="news_list"),
    path("<str:lang>/shareholders-meeting/",shareholders_meeting,name="shareholders_meeting"),
    path("<str:lang>/development-strategy/",development_strategy,name="development_strategy"),
    path("<str:lang>/internal-documents/",internal_documents,name="internal_documents"),
    path("<str:lang>/business-plan/",business_plan,name="business_plan"),
    path("<str:lang>/dividends/",dividends,name="dividends"),
    path("<str:lang>/reports/",reports,name="reports"),
    path("<str:lang>/charter/",charter,name="charter"),
    path("<str:lang>/emission-prospectus/",emission_prospectus,name="emission_prospectus"),
    path("<str:lang>/audit-report/",audit_report,name="audit_report"),
    path("<str:lang>/important-facts/",important_facts,name="important_facts"),
    path("<str:lang>/comply-explain/",comply_explain,name="comply_explain"),
    path("<str:lang>/affiliated-persons/",affiliated_persons,name="affiliated_persons"),
    
    path("<str:lang>/management-team/",management_team,name="management_team"),
    path("<str:lang>/vacancies/",vacancies,name="vacancies"),
    path("<str:lang>/supervisory-board/",supervisory_board,name="supervisory_board"),
    path("<str:lang>/organization-structure/",organization_structure,name="organizational_structure"),
    path("<str:lang>/general-information/",general_information,name="general_information"),
    
    path("<str:lang>/projects/",projects,name="projects"),
    path("<str:lang>/projects/<int:id>/",project_detail,name="project_detail"),
    
    path("<str:lang>/activities/",activity_list,name="activity_list"),
    
    path("robots.txt", robots_txt),
    path("robots.txt/", robots_txt),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
    path("sitemap.xml/", sitemap, {"sitemaps": sitemaps}),
]