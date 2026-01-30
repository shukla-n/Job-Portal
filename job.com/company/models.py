from django.db import models
from account.models import Company

# Create your models here.


class CompanyProfile(models.Model):
    company_name = models.CharField(max_length=50,null=True, blank=True)
    company_logo = models.ImageField(upload_to="company/", null=True, blank=True)
    company_prf_bg = models.ImageField(upload_to="company/", null=True, blank=True)
    company_slogam = models.CharField(max_length=50,null=True, blank=True)
    company_location = models.CharField(max_length=50,null=True, blank=True)
    about_us_img = models.ImageField(upload_to="company/", null=True, blank=True)
    about_us_discpt = models.TextField(null=True, blank=True)
    outher_det_title = models.CharField(max_length=50,null=True, blank=True)
    outher_det_image = models.ImageField(upload_to="company/", null=True, blank=True)
    outher_det_discription = models.TextField(null=True, blank=True)
    rel_comp = models.OneToOneField(
        Company, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.company_name


class JobPost(models.Model):
    cate = (
        ('IT FIELD','IT FIELD'),
        ('CUSTOMER SERVICE','CUSTOMER SERVICE'),
        ('HUMAN RESOURCE','HUMAN RESOURCE'),
        ('WORK FROM HOME','WORK FROM HOME'),
        ('MECHANICAL JOBS','MECHANICAL JOBS'),
        ('AUTOMOBILE','AUTOMOBILE'),
        ('TEACHING & EDUCATION','TEACHING & EDUCATION'),
        ('DESIGN & CREATIVE','DESIGN & CREATIVE'),
        
    )
    
    type = (("Full Time", "Full Time"), ("Part Time", "Part Time"))
    jobtitle = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    posttime = models.DateTimeField(auto_now_add=True)
    jobtype = models.CharField(max_length=20, choices=type)
    last_date = models.CharField(max_length=50)
    price_range = models.CharField(max_length=50)
    vacancy = models.IntegerField()
    job_discription = models.TextField()
    short_discription = models.TextField()
    required = models.TextField()
    education = models.TextField()
    status = models.BooleanField(default=True)
    category = models.CharField(max_length=20,choices=cate)

    rel_comp_job = models.ForeignKey(
        Company, on_delete=models.CASCADE, null=True, blank=True
    )
    rel_comp_comp = models.ForeignKey(
        CompanyProfile, on_delete=models.CASCADE, null=True, blank=True
    )
