from django.shortcuts import render, redirect
from .models import *
from account.models import *
from company.models import JobPost
from django.http import HttpResponse
from .decorators import employee_login_required


# Create your views here.

@employee_login_required
def employee_home(
    request,
):
    post = JobPost.objects.all()
    category = request.GET.get('category', '')
    jobtitle = request.GET.get('jobtitle', '')
    location = request.GET.get('location', '')
    if category or jobtitle :
        post = post.filter(category__icontains=category)
        post = post.filter(jobtitle__icontains=jobtitle)
    elif location:
        post = post.filter(location__icontains=location)
    context = {"post": post}
     
    return render(request, "employees_pages/emp_home.html", context)

    

@employee_login_required
def job_details(request, id):
    post = JobPost.objects.get(id=id)
    user = request.user
    comp = post.rel_comp_job
    prof = ProfileEdit.objects.filter(rel_profile=user).first()
   
    if request.method == "POST":
        apl = request.POST.get("apply")

        if apl:
            ApplyJob.objects.create(
                apply_status=True, 
                rel_profile=user, 
                rel_post=post, 
                rel_empl_post=prof,
                company_relation = comp
            )

            return redirect("job_details", post.id)
        else:
            ApplyJob.objects.create(
                apply_status=False,
                rel_profile=request.user,
                rel_post=post,
                rel_empl_post=prof,
                company_relation = comp
            )

            return redirect("job_details", post.id)

    apl = ApplyJob.objects.filter(rel_post=post).values_list("rel_profile", flat=True)
    
    context = {"post": post, "apl": apl}
    return render(request, "employees_pages/job_details.html", context)


@employee_login_required
def apply_sts(request, id):
    post = JobPost.objects.get(id=id)
    apl = ApplyJob.objects.filter(rel_post=post).first()
    apl.apply_status = not apl.apply_status
    apl.save()

    return redirect("job_details", post.id)

@employee_login_required
def employee_profile(request):
    emp = request.user

    addskl = AddSkill.objects.filter(rel_skill=emp)
    addexpe = AddExperience.objects.filter(rel_experience=emp)
    addeduc = AddEducations.objects.filter(rel_education=emp)
    addpro = AddProject.objects.filter(rel_project=emp)
    addprof = ProfileEdit.objects.filter(rel_profile=emp).first()

    context = {
        "emp": emp,
        "exp": addexpe,
        "educ": addeduc,
        "pro": addpro,
        "skl": addskl,
        "prof": addprof,
    } 
    return render(request, "employees_pages/emp_profile.html", context)

    

@employee_login_required
def employee_profile_edit(request):
    emp = request.user
    profile = ProfileEdit.objects.filter(
        rel_profile = emp
    ).first()
    
    if not profile:
        
        if request.method == "POST":
            prof_titl = request.POST.get("prof_titl")
            bio = request.POST.get("bio")
            pro_img = request.FILES.get("pro_img")
            pro_cv = request.FILES.get("pro_cv")
            location = request.POST.get("location")
            mob = request.POST.get("mob")
            status = request.POST.get("status")
            gender = request.POST.get("gender")

            ProfileEdit.objects.create(
                profile_title=prof_titl,
                bio=bio,
                profile_img=pro_img,
                resume=pro_cv,
                location=location,
                mobile_no=mob,
                working_sts=status,
                gender=gender,
                rel_profile=emp,
            )
            return redirect("employee_profile")
  
        return render(request, "employees_pages/emp_edit_profile.html")

        
    elif profile:
        
        if request.method == "POST":
            prof_titl = request.POST.get("prof_titl")
            bio = request.POST.get("bio")
            pro_img = request.FILES.get("pro_img")
            pro_cv = request.FILES.get("pro_cv")
            location = request.POST.get("location")
            mob = request.POST.get("mob")
            status = request.POST.get("status")
            gender = request.POST.get("gender")
            
            
            profile.profile_title=prof_titl
            profile.bio=bio
            if pro_img:
                profile.profile_img=pro_img
            if pro_cv:
                profile.resume=pro_cv
            profile.location=location
            profile.mobile_no=mob
            profile.working_sts=status
            profile.gender=gender
            profile.rel_profile=emp
            profile.save()
        
            return redirect("employee_profile")
        context={
            'profile':profile
        }  
        return render(request, "employees_pages/emp_edit_profile.html",context)
    
        
        

@employee_login_required
def add_experiences(request):
    emp = request.user
    if request.method == "POST":
        role = request.POST.get("role")
        name = request.POST.get("name")
        year = request.POST.get("year")
        discri = request.POST.get("discri")

        AddExperience.objects.create(
            job_role=role,
            date=year,
            company_name=name,
            job_dicription=discri,
            rel_experience=emp,
        )
        return redirect("employee_profile")
    return render(request, "employees_pages/emp_profile.html")


    

@employee_login_required
def add_educations(request):
    emp = request.user
    if request.method == "POST":
        name = request.POST.get("name")
        quali = request.POST.get("quali")
        year = request.POST.get("year")
        disc = request.POST.get("disc")

        AddEducations.objects.create(
            school=name,
            qualification=quali,
            date=year,
            shor_dicription=disc,
            rel_education=emp,
        )
        return redirect("employee_profile")
    return render(request, "employees_pages/emp_profile.html")

    

@employee_login_required
def add_project(request):
    emp = request.user
    if request.method == "POST":
        name = request.POST.get("name")
        domine = request.POST.get("domine")
        disc = request.POST.get("disc")

        AddProject.objects.create(
            pro_name=name, domine=domine, shor_dicription=disc, rel_project=emp
        )
        return redirect("employee_profile")
    return render(request, "employees_pages/emp_profile.html")

    

@employee_login_required
def add_skill(request):
    emp = request.user
    if request.method == "POST":
        skill = request.POST.get("skill")
        perc = request.POST.get("percentage")

        AddSkill.objects.create(skill=skill, percentage=perc, rel_skill=emp)
        return redirect(
            "employee_profile",
        ) 
    return render(request, "employees_pages/emp_profile.html")

    

@employee_login_required
def employee_appliedjob(request):
    user = request.user
    apl = ApplyJob.objects.filter(rel_profile=user)

    context = {"apl": apl}  
    return render(request, "employees_pages/applied_jobs.html", context)
 
    






