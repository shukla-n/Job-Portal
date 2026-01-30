from django.shortcuts import render, redirect
from .models import CompanyProfile, JobPost
from account.models import Company, Employee
from employee.models import ApplyJob
from django.http import HttpResponse
from .decorators import company_login_required


# Create your views here.

@company_login_required
def company_home(request):
    comp = request.user
   
    
    edit_pro = CompanyProfile.objects.filter(
        rel_comp=comp,
    )
    post = JobPost.objects.filter(rel_comp_job=comp)
    note = ApplyJob.objects.filter(company_relation = comp).order_by('id').reverse()
    lennote = note.filter(selected = 'Waiting for Review')
    legth = len(lennote)
    context = {
        "comp": comp,
        "edit_pro": edit_pro,
        "post": post,
        'note' : note,
        'legth' : legth
       
    } 
    return render(request, "company/company_home.html", context)


    

@company_login_required
def company_profile(request):
    comp = request.user
    edit_pro = CompanyProfile.objects.filter(rel_comp=comp).first()
    note = ApplyJob.objects.filter(company_relation = comp).order_by('id').reverse()
    lennote = note.filter(selected = 'Waiting for Review')
    legth = len(lennote)
    context = {
        "comp": comp,
        "edit_pro": edit_pro,
        'note' : note,
        'legth' : legth
        } 
    return render(request, "company/company_profile.html", context)
    

@company_login_required
def company_profile_edit(request):
    comp = request.user
    note = ApplyJob.objects.filter(company_relation = comp).order_by('id').reverse()
    lennote = note.filter(selected = 'Waiting for Review')
    legth = len(lennote)
    profile = CompanyProfile.objects.filter(
        rel_comp = comp
    ).first()
    
    if request.method == "POST":
        company_name = request.POST.get("company_name")
        slogan = request.POST.get("slogan")
        company_logo = request.FILES.get("company_logo")
        cover_image = request.FILES.get("cover_image")
        about_disc = request.POST.get("about_disc")
        about_img = request.FILES.get("about_img")
        outh_title = request.POST.get("outh_title")
        outh_disc = request.POST.get("outh_disc")
        outh_img = request.FILES.get("outh_img")
        location = request.POST.get("location")
        if not profile :
            CompanyProfile.objects.create(
                company_name=company_name,
                company_logo=company_logo,
                company_prf_bg=cover_image,
                company_slogam=slogan,
                company_location=location,
                about_us_img=about_img,
                about_us_discpt=about_disc,
                outher_det_title=outh_title,
                outher_det_image=outh_img,
                outher_det_discription=outh_disc,
                rel_comp=comp,
            )
            return redirect("company_profile")
        
        elif profile :
            profile.company_name=company_name
            if company_logo:
                profile.company_logo=company_logo
            if cover_image:
                profile.company_prf_bg=cover_image
            profile.company_slogam=slogan
            profile.company_location=location
            if about_img:
                profile.about_us_img=about_img
            profile.about_us_discpt=about_disc
            profile.outher_det_title=outh_title
            if outh_img:
                profile.outher_det_image=outh_img
            profile.outher_det_discription=outh_disc
            profile.rel_comp=comp
            profile.save()
            return redirect("company_profile")
    context={
        'profile':profile,
        'note' : note,
        'legth': legth
    }  
    return render(request, "company/company_profile_edit.html",context)

    
        

@company_login_required
def post_job(request):
    user = request.user
    comp = CompanyProfile.objects.filter(rel_comp=user).first()
    note = ApplyJob.objects.filter(company_relation = user).order_by('id').reverse()
    lennote = note.filter(selected = 'Waiting for Review')
    legth = len(lennote)
    if request.method == "POST":
        jobtitle = request.POST.get("jobtitle")
        location = request.POST.get("location")
        lastdate = request.POST.get("lastdate")
        jobtype = request.POST.get("jobtype")
        vacancy = request.POST.get("vacancy")
        price = request.POST.get("price")
        category = request.POST.get("category")
        job_discription = request.POST.get("job_discription")
        short_discription = request.POST.get("short_discription")
        required = request.POST.get("required")
        education = request.POST.get("education")
        status = request.POST.get("status")
        if status:
            JobPost.objects.create(
                jobtitle=jobtitle,
                location=location,
                jobtype=jobtype,
                last_date=lastdate,
                vacancy=vacancy,
                price_range=price,
                category = category,
                job_discription=job_discription,
                short_discription=short_discription,
                required=required,
                education=education,
                status=True,
                rel_comp_job=user,
                rel_comp_comp=comp,
            )
           
            return redirect("company_home")
        else:
            JobPost.objects.create(
                jobtitle=jobtitle,
                location=location,
                jobtype=jobtype,
                last_date=lastdate,
                vacancy=vacancy,
                price_range=price,
                category = category,
                job_discription=job_discription,
                short_discription=short_discription,
                required=required,
                education=education,
                status=False,
                rel_comp_job=user,
                rel_comp_comp=comp,
            )
           
            return redirect("company_home")
    context = {
        'note' : note,
        'legth' : legth
    }
    return render(request, "company/job_post.html",context)
    

@company_login_required
def job_status(request, id):
    post = JobPost.objects.get(id=id)
    post.status = not post.status
    post.save()
      
    return redirect("details_job", post.id)
  
    

@company_login_required
def details_job(request, id):
    post = JobPost.objects.get(id=id)
    comp = request.user
    note = ApplyJob.objects.filter(company_relation = comp).order_by('id').reverse()
    lennote = note.filter(selected = 'Waiting for Review')
    legth = len(lennote)
    apl = ApplyJob.objects.filter(rel_post=post)
    context = {
        "post": post,
        "apl": apl,
        'note' : note,
        'legth' : legth
    }
    return render(request,"company/job-detail.html",context)
    

@company_login_required
def applied_employee_profile(request, id):
    comp =request.user
    note = ApplyJob.objects.filter(company_relation = comp).order_by('id').reverse()
    lennote = note.filter(selected = 'Waiting for Review')
    legth = len(lennote)
    apl = ApplyJob.objects.get(id=id)
    if request.method == "POST":
        sel = request.POST.get("select")
        apl.selected = sel
        apl.save()

        return redirect("applied_employee_profile", apl.id)
    context = {
        'note' : note,
        'legth' : legth,
        "apl": apl,
        "exp": apl.rel_profile.addexperience_set.all(),
        "skl": apl.rel_profile.addskill_set.all(),
        "edu": apl.rel_profile.addeducations_set.all(),
        "pro": apl.rel_profile.addproject_set.all(),
        # 'profile' : apl.rel_profile.profileedit.all(),
    }  
    return render(request, "company/applied_user_profile.html", context)
    


def status_change(request, id):
    application = ApplyJob.objects.get(id=id)
    if request.method == 'POST':
        status = request.POST.get(f'status_{id}')
        application.selected = status
        application.save()
        return redirect('details_job', application.rel_post.id)
        
