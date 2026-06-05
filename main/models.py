from django.db import models
from django.core.exceptions import ValidationError

class Translation(models.Model):
    key = models.CharField(
        max_length=255,
        unique=True
    )

    en = models.TextField(blank=True, null=True)
    ru = models.TextField(blank=True, null=True)
    uz = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.key
    
    
    
class Contact(models.Model):

    title_uz=models.CharField(max_length=255)
    title_ru=models.CharField(max_length=255)
    title_en=models.CharField(max_length=255)

    address_uz=models.TextField()
    address_ru=models.TextField()
    address_en=models.TextField()

    phone=models.CharField(max_length=100)
    email=models.EmailField()

    def save(self,*args,**kwargs):
        self.pk=1
        super().save(*args,**kwargs)

    def delete(self,*args,**kwargs):
        pass

    def get_title(self,lang):
        return getattr(self,f"title_{lang}",self.title_uz)

    def get_address(self,lang):
        return getattr(self,f"address_{lang}",self.address_uz)

    def __str__(self):
        return self.title_uz
    
    
class Advantage(models.Model):

    image=models.ImageField(upload_to="advantages/")

    title_uz=models.CharField(max_length=255)
    title_ru=models.CharField(max_length=255)
    title_en=models.CharField(max_length=255)

    description_uz=models.TextField()
    description_ru=models.TextField()
    description_en=models.TextField()

    created_at=models.DateTimeField(auto_now_add=True)

    def get_title(self,lang):
        return getattr(self,f"title_{lang}",self.title_uz)

    def get_description(self,lang):
        return getattr(self,f"description_{lang}",self.description_uz)

    def __str__(self):
        return self.title_uz

    class Meta:
        ordering=["-created_at"]
        
        
class Statistics(models.Model):
    years_of_experience=models.PositiveIntegerField()
    experience_image_icon=models.ImageField(upload_to="statistics/")
    experience_title_uz=models.CharField(max_length=255)
    experience_title_ru=models.CharField(max_length=255)
    experience_title_en=models.CharField(max_length=255)

    count_projects_done=models.PositiveIntegerField()
    projects_done_image_icon=models.ImageField(upload_to="statistics/")
    projects_done_title_uz=models.CharField(max_length=255)
    projects_done_title_ru=models.CharField(max_length=255)
    projects_done_title_en=models.CharField(max_length=255)

    in_process_count=models.PositiveIntegerField()
    in_process_image_icon=models.ImageField(upload_to="statistics/")
    in_process_title_uz=models.CharField(max_length=255)
    in_process_title_ru=models.CharField(max_length=255)
    in_process_title_en=models.CharField(max_length=255)

    our_partnership_count=models.PositiveIntegerField()
    our_partnership_image_icon=models.ImageField(upload_to="statistics/")
    our_partnership_title_uz=models.CharField(max_length=255)
    our_partnership_title_ru=models.CharField(max_length=255)
    our_partnership_title_en=models.CharField(max_length=255)

    home_page_bg_icon=models.ImageField(upload_to="statistics/bg/")
    company_video_bg_image=models.ImageField(upload_to="statistics/video_bg/")
    
    company_video=models.FileField(upload_to="statistics/videos/")

    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="Statistics"
        verbose_name_plural="Statistics"

    def __str__(self):
        return "Statistics"
    
    
class Partner(models.Model):
    image = models.ImageField(upload_to="partners/")
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "Bizning sheriklar"
        verbose_name_plural = "Bizning sheriklar"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
    
    
    



class News(models.Model):

    title_uz=models.CharField(
        max_length=255,
        verbose_name="Sarlavha (UZ)"
    )
    title_ru=models.CharField(
        max_length=255,
        verbose_name="Sarlavha (RU)"
    )

    title_en=models.CharField(
        max_length=255,
        verbose_name="Sarlavha (EN)"
    )

    text_uz=models.TextField(
        verbose_name="Matn (UZ)"
    )

    text_ru=models.TextField(
        verbose_name="Matn (RU)"
    )

    text_en=models.TextField(
        verbose_name="Matn (EN)"
    )

    news_date=models.DateField(
        verbose_name="Yangilik sanasi"
    )

    social_link=models.URLField(
        blank=True,
        null=True,
        verbose_name="Ijtimoiy tarmoq havolasi"
    )

    created_at=models.DateTimeField(
        auto_now_add=True,
        verbose_name="Yaratilgan vaqt"
    )
    

    class Meta:

        ordering=["-news_date"]

        verbose_name="Yangilik"
        verbose_name_plural="Yangiliklar"

    def get_title(self,lang):
        return getattr(
            self,
            f"title_{lang}",
            self.title_uz
        )

    def get_text(self,lang):
        return getattr(
            self,
            f"text_{lang}",
            self.text_uz
        )

    def first_image(self):
        first=self.images.first()
        return first.image.url if first else "/media/news/default/default_news.png"

    def images_count(self):
        return self.images.count()

    def __str__(self):
        return self.title_uz




class NewsImage(models.Model):
    news=models.ForeignKey(
        News,
        on_delete=models.CASCADE,
        related_name="images"
    )
    image=models.ImageField(
        upload_to="news/images/%Y/%m/%d/",
        default="news/default/default_news.png",
        verbose_name="Rasm"
    )

    class Meta:

        verbose_name="Yangilik rasmi"
        verbose_name_plural="Yangilik rasmlari"


    def __str__(self):
        return f"{self.news_id}-{self.id}"
    
    



def validate_file_size(file):

    if file.size>10*1024*1024:
        raise ValidationError("Fayl hajmi 10MB dan oshmasligi kerak.")


class ShareholderMeeting(models.Model):

    title_uz=models.CharField(max_length=255,verbose_name="Sarlavha (UZ)")
    title_ru=models.CharField(max_length=255,verbose_name="Sarlavha (RU)")
    title_en=models.CharField(max_length=255,verbose_name="Sarlavha (EN)")

    description_uz=models.TextField(blank=True,null=True,verbose_name="Tavsif (UZ)")
    description_ru=models.TextField(blank=True,null=True,verbose_name="Tavsif (RU)")
    description_en=models.TextField(blank=True,null=True,verbose_name="Tavsif (EN)")

    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name="Aksiyadorlar yig‘ilishi"
        verbose_name_plural="Aksiyadorlar yig‘ilishlari"

    def save(self,*args,**kwargs):

        self.pk=1

        super().save(*args,**kwargs)

    def delete(self,*args,**kwargs):
        pass

    def __str__(self):
        return self.title_uz


class ShareholderMeetingFile(models.Model):

    meeting=models.ForeignKey(
        ShareholderMeeting,
        on_delete=models.CASCADE,
        related_name="files"
    )

    title_uz=models.TextField(verbose_name="Fayl nomi (UZ)")
    title_ru=models.TextField(verbose_name="Fayl nomi (RU)")
    title_en=models.TextField(verbose_name="Fayl nomi (EN)")
    
    
    file=models.FileField(
        upload_to="shareholder_meetings/%Y/%m/%d/",
        validators=[validate_file_size],
        verbose_name="Fayl"
    )

    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name="Yig‘ilish fayli"
        verbose_name_plural="Yig‘ilish fayllari"

        ordering=["id"]

    def __str__(self):
        return f"{self.meeting_id}-{self.id}"
    
    
    
    
class DevelopmentStrategy(models.Model):

    title_uz=models.CharField(max_length=255,verbose_name="Sarlavha (UZ)")
    title_ru=models.CharField(max_length=255,verbose_name="Sarlavha (RU)")
    title_en=models.CharField(max_length=255,verbose_name="Sarlavha (EN)")

    description_uz=models.TextField(blank=True,null=True,verbose_name="Tavsif (UZ)")
    description_ru=models.TextField(blank=True,null=True,verbose_name="Tavsif (RU)")
    description_en=models.TextField(blank=True,null=True,verbose_name="Tavsif (EN)")

    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name="Rivojlanish strategiyasi"
        verbose_name_plural="Rivojlanish strategiyasi"

    def save(self,*args,**kwargs):

        self.pk=1

        super().save(*args,**kwargs)

    def delete(self,*args,**kwargs):
        pass

    def __str__(self):
        return self.title_uz


class DevelopmentStrategyFile(models.Model):

    strategy=models.ForeignKey(
        DevelopmentStrategy,
        on_delete=models.CASCADE,
        related_name="files"
    )

    title_uz=models.TextField(verbose_name="Fayl nomi (UZ)")
    title_ru=models.TextField(verbose_name="Fayl nomi (RU)")
    title_en=models.TextField(verbose_name="Fayl nomi (EN)")

    file=models.FileField(
        upload_to="development_strategy/%Y/%m/%d/",
        validators=[validate_file_size],
        verbose_name="Fayl"
    )

    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name="Strategiya fayli"
        verbose_name_plural="Strategiya fayllari"

        ordering=["id"]

    def __str__(self):
        return f"{self.strategy_id}-{self.id}"
    
    
    
class InternalDocument(models.Model):

    title_uz=models.CharField(max_length=255,verbose_name="Sarlavha (UZ)")
    title_ru=models.CharField(max_length=255,verbose_name="Sarlavha (RU)")
    title_en=models.CharField(max_length=255,verbose_name="Sarlavha (EN)")

    description_uz=models.TextField(blank=True,null=True,verbose_name="Tavsif (UZ)")
    description_ru=models.TextField(blank=True,null=True,verbose_name="Tavsif (RU)")
    description_en=models.TextField(blank=True,null=True,verbose_name="Tavsif (EN)")

    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name="Ichki hujjatlar"
        verbose_name_plural="Ichki hujjatlar"

    def save(self,*args,**kwargs):

        self.pk=1

        super().save(*args,**kwargs)

    def delete(self,*args,**kwargs):
        pass

    def __str__(self):
        return self.title_uz


class InternalDocumentFile(models.Model):

    document=models.ForeignKey(
        InternalDocument,
        on_delete=models.CASCADE,
        related_name="files"
    )

    title_uz=models.TextField(verbose_name="Fayl nomi (UZ)")
    title_ru=models.TextField(verbose_name="Fayl nomi (RU)")
    title_en=models.TextField(verbose_name="Fayl nomi (EN)")

    file=models.FileField(
        upload_to="internal_documents/%Y/%m/%d/",
        validators=[validate_file_size],
        verbose_name="Fayl"
    )

    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name="Ichki hujjat fayli"
        verbose_name_plural="Ichki hujjat fayllari"

        ordering=["id"]

    def __str__(self):
        return f"{self.document_id}-{self.id}"
    
    


class BusinessPlan(models.Model):

    title_uz=models.CharField(max_length=255,verbose_name="Sarlavha (UZ)")
    title_ru=models.CharField(max_length=255,verbose_name="Sarlavha (RU)")
    title_en=models.CharField(max_length=255,verbose_name="Sarlavha (EN)")

    description_uz=models.TextField(blank=True,null=True,verbose_name="Tavsif (UZ)")
    description_ru=models.TextField(blank=True,null=True,verbose_name="Tavsif (RU)")
    description_en=models.TextField(blank=True,null=True,verbose_name="Tavsif (EN)")

    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name="Biznes-reja"
        verbose_name_plural="Biznes-reja"

    def save(self,*args,**kwargs):

        self.pk=1

        super().save(*args,**kwargs)

    def delete(self,*args,**kwargs):
        pass

    def __str__(self):
        return self.title_uz


class BusinessPlanFile(models.Model):

    plan=models.ForeignKey(
        BusinessPlan,
        on_delete=models.CASCADE,
        related_name="files"
    )

    title_uz=models.TextField(verbose_name="Fayl nomi (UZ)")
    title_ru=models.TextField(verbose_name="Fayl nomi (RU)")
    title_en=models.TextField(verbose_name="Fayl nomi (EN)")

    file=models.FileField(
        upload_to="business_plan/%Y/%m/%d/",
        validators=[validate_file_size],
        verbose_name="Fayl"
    )

    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name="Biznes-reja fayli"
        verbose_name_plural="Biznes-reja fayllari"

        ordering=["id"]

    def __str__(self):
        return f"{self.plan_id}-{self.id}"
    
    
class Dividend(models.Model):

    title_uz=models.CharField(max_length=255,verbose_name="Sarlavha (UZ)")
    title_ru=models.CharField(max_length=255,verbose_name="Sarlavha (RU)")
    title_en=models.CharField(max_length=255,verbose_name="Sarlavha (EN)")

    description_uz=models.TextField(blank=True,null=True,verbose_name="Tavsif (UZ)")
    description_ru=models.TextField(blank=True,null=True,verbose_name="Tavsif (RU)")
    description_en=models.TextField(blank=True,null=True,verbose_name="Tavsif (EN)")

    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name="Dividendlar"
        verbose_name_plural="Dividendlar"

    def save(self,*args,**kwargs):

        self.pk=1

        super().save(*args,**kwargs)

    def delete(self,*args,**kwargs):
        pass

    def __str__(self):
        return self.title_uz


class DividendFile(models.Model):

    dividend=models.ForeignKey(
        Dividend,
        on_delete=models.CASCADE,
        related_name="files"
    )

    title_uz = models.TextField(verbose_name="Fayl nomi (UZ)")
    title_ru = models.TextField(verbose_name="Fayl nomi (RU)")
    title_en = models.TextField(verbose_name="Fayl nomi (EN)")

    file=models.FileField(
        upload_to="dividends/%Y/%m/%d/",
        validators=[validate_file_size],
        verbose_name="Fayl"
    )

    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name="Dividend fayli"
        verbose_name_plural="Dividend fayllari"

        ordering=["id"]

    def __str__(self):
        return f"{self.dividend_id}-{self.id}"
    
    
class Report(models.Model):

    title_uz=models.CharField(max_length=255,verbose_name="Sarlavha (UZ)")
    title_ru=models.CharField(max_length=255,verbose_name="Sarlavha (RU)")
    title_en=models.CharField(max_length=255,verbose_name="Sarlavha (EN)")

    description_uz=models.TextField(blank=True,null=True,verbose_name="Tavsif (UZ)")
    description_ru=models.TextField(blank=True,null=True,verbose_name="Tavsif (RU)")
    description_en=models.TextField(blank=True,null=True,verbose_name="Tavsif (EN)")

    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name="Hisobotlar"
        verbose_name_plural="Hisobotlar"

    def save(self,*args,**kwargs):

        self.pk=1

        super().save(*args,**kwargs)

    def delete(self,*args,**kwargs):
        pass

    def __str__(self):
        return self.title_uz


class ReportFile(models.Model):

    report=models.ForeignKey(
        Report,
        on_delete=models.CASCADE,
        related_name="files"
    )

    title_uz=models.TextField(verbose_name="Fayl nomi (UZ)")
    title_ru=models.TextField(verbose_name="Fayl nomi (RU)")
    title_en=models.TextField(verbose_name="Fayl nomi (EN)")

    file=models.FileField(
        upload_to="reports/%Y/%m/%d/",
        validators=[validate_file_size],
        verbose_name="Fayl"
    )

    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name="Hisobot fayli"
        verbose_name_plural="Hisobot fayllari"

        ordering=["id"]

    def __str__(self):
        return f"{self.report_id}-{self.id}"
    
    
class Charter(models.Model):

    title_uz=models.CharField(max_length=255,verbose_name="Sarlavha (UZ)")
    title_ru=models.CharField(max_length=255,verbose_name="Sarlavha (RU)")
    title_en=models.CharField(max_length=255,verbose_name="Sarlavha (EN)")

    description_uz=models.TextField(blank=True,null=True,verbose_name="Tavsif (UZ)")
    description_ru=models.TextField(blank=True,null=True,verbose_name="Tavsif (RU)")
    description_en=models.TextField(blank=True,null=True,verbose_name="Tavsif (EN)")

    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name="Ustav"
        verbose_name_plural="Ustav"

    def save(self,*args,**kwargs):

        self.pk=1

        super().save(*args,**kwargs)

    def delete(self,*args,**kwargs):
        pass

    def __str__(self):
        return self.title_uz


class CharterFile(models.Model):

    charter=models.ForeignKey(
        Charter,
        on_delete=models.CASCADE,
        related_name="files"
    )

    title_uz=models.TextField(verbose_name="Fayl nomi (UZ)")
    title_ru=models.TextField(verbose_name="Fayl nomi (RU)")
    title_en=models.TextField(verbose_name="Fayl nomi (EN)")

    file=models.FileField(
        upload_to="charter/%Y/%m/%d/",
        validators=[validate_file_size],
        verbose_name="Fayl"
    )

    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name="Ustav fayli"
        verbose_name_plural="Ustav fayllari"

        ordering=["id"]

    def __str__(self):
        return f"{self.charter_id}-{self.id}"
    
    
class EmissionProspectus(models.Model):

    title_uz=models.CharField(max_length=255,verbose_name="Sarlavha (UZ)")
    title_ru=models.CharField(max_length=255,verbose_name="Sarlavha (RU)")
    title_en=models.CharField(max_length=255,verbose_name="Sarlavha (EN)")

    description_uz=models.TextField(blank=True,null=True,verbose_name="Tavsif (UZ)")
    description_ru=models.TextField(blank=True,null=True,verbose_name="Tavsif (RU)")
    description_en=models.TextField(blank=True,null=True,verbose_name="Tavsif (EN)")

    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name="Emissiya prospekti"
        verbose_name_plural="Emissiya prospekti"

    def save(self,*args,**kwargs):

        self.pk=1

        super().save(*args,**kwargs)

    def delete(self,*args,**kwargs):
        pass

    def __str__(self):
        return self.title_uz


class EmissionProspectusFile(models.Model):

    prospectus=models.ForeignKey(
        EmissionProspectus,
        on_delete=models.CASCADE,
        related_name="files"
    )

    title_uz=models.TextField(verbose_name="Fayl nomi (UZ)")
    title_ru=models.TextField(verbose_name="Fayl nomi (RU)")
    title_en=models.TextField(verbose_name="Fayl nomi (EN)")

    file=models.FileField(
        upload_to="emission_prospectus/%Y/%m/%d/",
        validators=[validate_file_size],
        verbose_name="Fayl"
    )

    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name="Emissiya prospekti fayli"
        verbose_name_plural="Emissiya prospekti fayllari"

        ordering=["id"]

    def __str__(self):
        return f"{self.prospectus_id}-{self.id}"
    
    
class AuditReport(models.Model):

    title_uz=models.CharField(max_length=255,verbose_name="Sarlavha (UZ)")
    title_ru=models.CharField(max_length=255,verbose_name="Sarlavha (RU)")
    title_en=models.CharField(max_length=255,verbose_name="Sarlavha (EN)")

    description_uz=models.TextField(blank=True,null=True,verbose_name="Tavsif (UZ)")
    description_ru=models.TextField(blank=True,null=True,verbose_name="Tavsif (RU)")
    description_en=models.TextField(blank=True,null=True,verbose_name="Tavsif (EN)")

    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name="Auditorlik hisoboti"
        verbose_name_plural="Auditorlik hisoboti"

    def save(self,*args,**kwargs):

        self.pk=1

        super().save(*args,**kwargs)

    def delete(self,*args,**kwargs):
        pass

    def __str__(self):
        return self.title_uz


class AuditReportFile(models.Model):

    report=models.ForeignKey(
        AuditReport,
        on_delete=models.CASCADE,
        related_name="files"
    )

    title_uz=models.TextField(verbose_name="Fayl nomi (UZ)")
    title_ru=models.TextField(verbose_name="Fayl nomi (RU)")
    title_en=models.TextField(verbose_name="Fayl nomi (EN)")

    file=models.FileField(
        upload_to="audit_reports/%Y/%m/%d/",
        validators=[validate_file_size],
        verbose_name="Fayl"
    )

    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name="Auditorlik hisoboti fayli"
        verbose_name_plural="Auditorlik hisoboti fayllari"

        ordering=["id"]

    def __str__(self):
        return f"{self.report_id}-{self.id}"
    
    
class ImportantFact(models.Model):

    title_uz=models.CharField(max_length=255,verbose_name="Sarlavha (UZ)")
    title_ru=models.CharField(max_length=255,verbose_name="Sarlavha (RU)")
    title_en=models.CharField(max_length=255,verbose_name="Sarlavha (EN)")

    description_uz=models.TextField(blank=True,null=True,verbose_name="Tavsif (UZ)")
    description_ru=models.TextField(blank=True,null=True,verbose_name="Tavsif (RU)")
    description_en=models.TextField(blank=True,null=True,verbose_name="Tavsif (EN)")

    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name="Muhim faktlar"
        verbose_name_plural="Muhim faktlar"

    def save(self,*args,**kwargs):

        self.pk=1

        super().save(*args,**kwargs)

    def delete(self,*args,**kwargs):
        pass

    def __str__(self):
        return self.title_uz


class ImportantFactFile(models.Model):

    fact=models.ForeignKey(
        ImportantFact,
        on_delete=models.CASCADE,
        related_name="files"
    )

    title_uz=models.TextField(verbose_name="Fayl nomi (UZ)")
    title_ru=models.TextField(verbose_name="Fayl nomi (RU)")
    title_en=models.TextField(verbose_name="Fayl nomi (EN)")

    file=models.FileField(
        upload_to="important_facts/%Y/%m/%d/",
        validators=[validate_file_size],
        verbose_name="Fayl"
    )

    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name="Muhim fakt fayli"
        verbose_name_plural="Muhim fakt fayllari"

        ordering=["id"]

    def __str__(self):
        return f"{self.fact_id}-{self.id}"
    
    


class ComplyExplain(models.Model):

    title_uz=models.CharField(max_length=255,verbose_name="Sarlavha (UZ)")
    title_ru=models.CharField(max_length=255,verbose_name="Sarlavha (RU)")
    title_en=models.CharField(max_length=255,verbose_name="Sarlavha (EN)")

    description_uz=models.TextField(blank=True,null=True,verbose_name="Tavsif (UZ)")
    description_ru=models.TextField(blank=True,null=True,verbose_name="Tavsif (RU)")
    description_en=models.TextField(blank=True,null=True,verbose_name="Tavsif (EN)")

    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name="Comply or Explain"
        verbose_name_plural="Comply or Explain"

    def save(self,*args,**kwargs):

        self.pk=1

        super().save(*args,**kwargs)

    def delete(self,*args,**kwargs):
        pass

    def __str__(self):
        return self.title_uz


class ComplyExplainFile(models.Model):

    comply=models.ForeignKey(
        ComplyExplain,
        on_delete=models.CASCADE,
        related_name="files"
    )

    title_uz=models.TextField(verbose_name="Fayl nomi (UZ)")
    title_ru=models.TextField(verbose_name="Fayl nomi (RU)")
    title_en=models.TextField(verbose_name="Fayl nomi (EN)")

    file=models.FileField(
        upload_to="comply_explain/%Y/%m/%d/",
        validators=[validate_file_size],
        verbose_name="Fayl"
    )

    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name="Rioya qil yoki tushuntir fayli"
        verbose_name_plural="Rioya qil yoki tushuntir fayllari"

        ordering=["id"]

    def __str__(self):
        return f"{self.comply_id}-{self.id}"
    
    
    
class AffiliatedPerson(models.Model):

    title_uz=models.CharField(max_length=255,verbose_name="Sarlavha (UZ)")
    title_ru=models.CharField(max_length=255,verbose_name="Sarlavha (RU)")
    title_en=models.CharField(max_length=255,verbose_name="Sarlavha (EN)")

    description_uz=models.TextField(blank=True,null=True,verbose_name="Tavsif (UZ)")
    description_ru=models.TextField(blank=True,null=True,verbose_name="Tavsif (RU)")
    description_en=models.TextField(blank=True,null=True,verbose_name="Tavsif (EN)")

    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name="Affillangan shaxslar"
        verbose_name_plural="Affillangan shaxslar"

    def save(self,*args,**kwargs):

        self.pk=1

        super().save(*args,**kwargs)

    def delete(self,*args,**kwargs):
        pass

    def __str__(self):
        return self.title_uz


class AffiliatedPersonFile(models.Model):

    person=models.ForeignKey(
        AffiliatedPerson,
        on_delete=models.CASCADE,
        related_name="files"
    )

    title_uz=models.TextField(verbose_name="Fayl nomi (UZ)")
    title_ru=models.TextField(verbose_name="Fayl nomi (RU)")
    title_en=models.TextField(verbose_name="Fayl nomi (EN)")

    file=models.FileField(
        upload_to="affiliated_persons/%Y/%m/%d/",
        validators=[validate_file_size],
        verbose_name="Fayl"
    )

    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name="Affillangan shaxs fayli"
        verbose_name_plural="Affillangan shaxs fayllari"

        ordering=["id"]

    def __str__(self):
        return f"{self.person_id}-{self.id}"
    
    
    
class ManagementTeam(models.Model):

    full_name_uz=models.CharField(max_length=255,verbose_name="F.I.Sh. (UZ)")
    full_name_ru=models.CharField(max_length=255,verbose_name="Ф.И.О. (RU)")
    full_name_en=models.CharField(max_length=255,verbose_name="Full Name (EN)")

    position_uz=models.CharField(max_length=255,verbose_name="Lavozim (UZ)")
    position_ru=models.CharField(max_length=255,verbose_name="Должность (RU)")
    position_en=models.CharField(max_length=255,verbose_name="Position (EN)")

    reception_days_uz=models.CharField(max_length=255,verbose_name="Qabul kunlari (UZ)")
    reception_days_ru=models.CharField(max_length=255,verbose_name="Приемные дни (RU)")
    reception_days_en=models.CharField(max_length=255,verbose_name="Reception Days (EN)")

    phone_number=models.CharField(max_length=100,verbose_name="Telefon")

    biography_uz=models.TextField(blank=True,null=True,verbose_name="Tarjimai hol (UZ)")
    biography_ru=models.TextField(blank=True,null=True,verbose_name="Биография (RU)")
    biography_en=models.TextField(blank=True,null=True,verbose_name="Biography (EN)")

    duty_uz=models.TextField(blank=True,null=True,verbose_name="Vazifalari (UZ)")
    duty_ru=models.TextField(blank=True,null=True,verbose_name="Обязанности (RU)")
    duty_en=models.TextField(blank=True,null=True,verbose_name="Duties (EN)")

    image=models.ImageField(
        upload_to="management_team/%Y/%m/%d/",
        default="management_team/default/default.png",
        verbose_name="Rasm"
    )
    
    email=models.EmailField(
        blank=True,
        null=True,
        verbose_name="Elektron pochta"
    )

    order=models.PositiveIntegerField(
        default=0,
        verbose_name="Tartib raqami"
    )

    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name="Rahbariyat a'zosi"
        verbose_name_plural="Rahbariyat"
        ordering=["order"]

    def __str__(self):

        return self.full_name_uz
    
    
    

class Vacancy(models.Model):

    title_uz=models.CharField(max_length=255,verbose_name="Lavozim nomi (UZ)")
    title_ru=models.CharField(max_length=255,verbose_name="Название вакансии (RU)")
    title_en=models.CharField(max_length=255,verbose_name="Vacancy Title (EN)")

    description_uz=models.TextField(verbose_name="Tavsif (UZ)")
    description_ru=models.TextField(verbose_name="Описание (RU)")
    description_en=models.TextField(verbose_name="Description (EN)")

    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name="Vakansiya"
        verbose_name_plural="Vakansiyalar"

        ordering=["-id"]

    def __str__(self):

        return self.title_uz
    
    
class ResumeTemplate(models.Model):

    file=models.FileField(
        upload_to="resume_templates/%Y/%m/%d/",
        validators=[validate_file_size],
        verbose_name="Rezyume namunasi"
    )

    updated_at=models.DateTimeField(auto_now=True)

    class Meta:

        verbose_name="Rezyume namunasi"
        verbose_name_plural="Rezyume namunasi"

    def save(self,*args,**kwargs):

        self.pk=1

        super().save(*args,**kwargs)

    def delete(self,*args,**kwargs):
        pass

    def __str__(self):

        return "Resume namunasi"
    
    
class SupervisoryBoardMember(models.Model):
    full_name_uz=models.CharField(
        max_length=255,
        verbose_name="F.I.Sh. (UZ)"
    )
    full_name_ru=models.CharField(
        max_length=255,
        verbose_name="Ф.И.О. (RU)"
    )
    full_name_en=models.CharField(
        max_length=255,
        verbose_name="Full Name (EN)"
    )
    position_uz=models.CharField(
        max_length=255,
        verbose_name="Lavozimi (UZ)"
    )
    position_ru=models.CharField(
        max_length=255,
        verbose_name="Должность (RU)"
    )
    position_en=models.CharField(
        max_length=255,
        verbose_name="Position (EN)"
    )
    is_auditor=models.BooleanField(
        default=False,
        verbose_name="Auditor"
    )
    order=models.PositiveIntegerField(
        default=0,
        verbose_name="Tartib"
    )
    created_at=models.DateTimeField(
        auto_now_add=True
    )
    class Meta:
        verbose_name="Kuzatuv kengashi a'zosi"
        verbose_name_plural="Kuzatuv kengashi a'zolari"
        ordering=["order"]

    def __str__(self):
        return self.full_name_uz
    
    
    
class OrganizationStructure(models.Model):

    title_uz=models.CharField(max_length=255,verbose_name="Sarlavha (UZ)")
    title_ru=models.CharField(max_length=255,verbose_name="Sarlavha (RU)")
    title_en=models.CharField(max_length=255,verbose_name="Sarlavha (EN)")

    description_uz=models.TextField(blank=True,null=True,verbose_name="Tavsif (UZ)")
    description_ru=models.TextField(blank=True,null=True,verbose_name="Tavsif (RU)")
    description_en=models.TextField(blank=True,null=True,verbose_name="Tavsif (EN)")

    image=models.ImageField(
        upload_to="organization_structure/%Y/%m/%d/",
        verbose_name="Tuzilma rasmi"
    )

    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name="Tashkiliy tuzilma"
        verbose_name_plural="Tashkiliy tuzilma"

    def save(self,*args,**kwargs):

        self.pk=1

        super().save(*args,**kwargs)

    def delete(self,*args,**kwargs):
        pass

    def __str__(self):

        return self.title_uz
    
class OrganizationStructureFile(models.Model):

    structure=models.ForeignKey(
        OrganizationStructure,
        on_delete=models.CASCADE,
        related_name="files"
    )

    title_uz=models.TextField(verbose_name="Fayl nomi (UZ)")
    title_ru=models.TextField(verbose_name="Fayl nomi (RU)")
    title_en=models.TextField(verbose_name="Fayl nomi (EN)")

    file=models.FileField(
        upload_to="organization_structure/%Y/%m/%d/",
        validators=[validate_file_size],
        verbose_name="Fayl"
    )

    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name="Tuzilma fayli"
        verbose_name_plural="Tuzilma fayllari"

        ordering=["id"]

    def __str__(self):

        return f"{self.structure_id}-{self.id}"
    
    
class AboutCompany(models.Model):

    title_uz=models.CharField(max_length=255,verbose_name="Sarlavha (UZ)")
    title_ru=models.CharField(max_length=255,verbose_name="Sarlavha (RU)")
    title_en=models.CharField(max_length=255,verbose_name="Sarlavha (EN)")

    about_content_uz=models.TextField(verbose_name="Matn (UZ)")
    about_content_ru=models.TextField(verbose_name="Matn (RU)")
    about_content_en=models.TextField(verbose_name="Matn (EN)")

    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name="Jamiyat haqida"
        verbose_name_plural="Jamiyat haqida"

    def save(self,*args,**kwargs):

        self.pk=1

        super().save(*args,**kwargs)

    def delete(self,*args,**kwargs):
        pass

    def __str__(self):

        return self.title_uz
    
    
class AboutCompanyChronology(models.Model):

    about=models.ForeignKey(
        AboutCompany,
        on_delete=models.CASCADE,
        related_name="chronologies"
    )

    year=models.PositiveIntegerField(
        verbose_name="Yil"
    )

    description_uz=models.TextField(
        verbose_name="Tavsif (UZ)"
    )

    description_ru=models.TextField(
        verbose_name="Tavsif (RU)"
    )

    description_en=models.TextField(
        verbose_name="Tavsif (EN)"
    )

    class Meta:

        verbose_name="Tarixiy voqea"
        verbose_name_plural="Tarixiy voqealar"

        ordering=["year"]

    def __str__(self):

        return str(self.year)
    
    
class Project(models.Model):

    title_uz=models.TextField()
    title_ru=models.TextField()
    title_en=models.TextField()

    description_uz=models.TextField()
    description_ru=models.TextField()
    description_en=models.TextField()
    
    period=models.CharField(
        max_length=100,
        verbose_name="Amalga oshirish davri"
    )

    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name="Loyiha"
        verbose_name_plural="Loyihalar"
        ordering=["-created_at"]

    def __str__(self):
        return self.title_uz

    def first_image(self):
        image=self.images.first()
        return image.image.url if image else None
    
    def images_count(self):
        return self.images.count()
    
    
class ProjectImage(models.Model):

    project=models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="images"
    )

    image=models.ImageField(
        upload_to="projects/"
    )

    class Meta:

        verbose_name="Loyiha rasmi"
        verbose_name_plural="Loyiha rasmlari"

    def __str__(self):

        return f"Image #{self.pk}"
    
    
    
class Activity(models.Model):
    title_uz = models.CharField(
        max_length=255
    )
    title_ru = models.CharField(
        max_length=255
    )
    title_en = models.CharField(
        max_length=255
    )
    description_uz = models.TextField()
    description_ru = models.TextField()
    description_en = models.TextField()

    image = models.ImageField(
        upload_to="activities/%Y/%m/%d/"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    class Meta:
        verbose_name = "Faoliyat"
        verbose_name_plural = "Faoliyatlar"
        ordering = ["created_at"]

    def __str__(self):
        return self.title_uz