from django.db import models


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