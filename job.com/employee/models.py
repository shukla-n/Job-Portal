from django.db import models
from account.models import Employee,Company
from company.models import JobPost

# Create your models here.


class AddExperience(models.Model):
    job_role = models.CharField(max_length=50)
    date = models.CharField(max_length=10)
    company_name = models.CharField(max_length=50)
    job_dicription = models.TextField(null=True, blank=True)
    rel_experience = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=True, blank=True
    )


class AddEducations(models.Model):
    school = models.CharField(max_length=50)
    qualification = models.CharField(max_length=50)
    date = models.CharField(max_length=10)
    shor_dicription = models.TextField(null=True, blank=True)
    rel_education = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=True, blank=True
    )


class AddProject(models.Model):
    pro_name = models.CharField(max_length=50)
    domine = models.CharField(max_length=50)
    shor_dicription = models.TextField(null=True, blank=True)
    rel_project = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=True, blank=True
    )


class AddSkill(models.Model):
    skill = models.CharField(max_length=50)
    percentage = models.IntegerField()
    rel_skill = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=True, blank=True
    )


class ProfileEdit(models.Model):
    worksts = (
        ("frsh", "I'm Fresher"),
        ("exp", "I'm Experienced"))

    gender = (("M", "Male"), ("F", "Female"), ("O", "Outher"))

    profile_title = models.CharField(max_length=50,null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    profile_img = models.ImageField(upload_to="profile.image/", null=True, blank=True,default='static\img\pro.png')
    resume = models.FileField(upload_to="resume/", null=True, blank=True)
    location = models.CharField(max_length=50,null=True, blank=True)
    mobile_no = models.CharField(max_length=12,null=True, blank=True)
    working_sts = models.CharField(max_length=50, choices=worksts,null=True, blank=True)
    gender = models.CharField(max_length=50, choices=gender,null=True, blank=True)
    rel_profile = models.OneToOneField(
        Employee, on_delete=models.CASCADE, null=True, blank=True
    )


class ApplyJob(models.Model):
    sel = (
        ("Waiting for Review", "Waiting for Review"),
        ("Your Selected", "Your Selected"),
        ("Rejected", "Rejected"),
    )
    apply_status = models.BooleanField(default=True)
    rel_profile = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=True, blank=True,related_name='applied_jobs'
    )

    rel_post = models.ForeignKey(
        JobPost, on_delete=models.CASCADE, null=True, blank=True
    )
    rel_empl_post = models.ForeignKey(
        ProfileEdit, on_delete=models.CASCADE, null=True, blank=True
    )
    selected = models.CharField(
        max_length=30, choices=sel, default="Waiting for Review"
    )
    company_relation = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='apply_jobs',null=True, blank=True)
   