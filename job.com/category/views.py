from django.shortcuts import render
from company.models import JobPost
from django.contrib.auth.decorators import login_required
from employee.decorators import employee_login_required


# Create your views here.
@employee_login_required
def it_field(request):
    post = JobPost.objects.all()
    context={
        'post' : post
    } 
    return render(request,'category/it_field.html',context)
    


@employee_login_required
def customer_service(request):
    post = JobPost.objects.all()
    context={
        'post' : post
    } 
    return render(request,'category/customer_service.html',context)

    


@employee_login_required
def human_resource(request):
    post = JobPost.objects.all()
    context={
        'post' : post
    }
    return render(request,'category/human_resource.html',context)
    


@employee_login_required
def work_from_home(request):
    post = JobPost.objects.all()
    context={
        'post' : post
    }
    return render(request,'category/work_from_home.html',context)
    


@employee_login_required
def mechanical_job(request):
    post = JobPost.objects.all()
    context={
        'post' : post
    }
    return render(request,'category/mechanical_job.html',context)
    


@employee_login_required
def automobile(request):
    post = JobPost.objects.all()
    context={
        'post' : post
    } 
    return render(request,'category/automobile.html',context)


@employee_login_required
def education(request):
    post = JobPost.objects.all()
    context={
        'post' : post
    }
    return render(request,'category/education.html',context)


@employee_login_required
def education(request):
    post = JobPost.objects.all()
    context={
        'post' : post
    } 
    return render(request,'category/education.html',context)



@employee_login_required
def design(request):
    post = JobPost.objects.all()
    context={
        'post' : post
    }
    return render(request,'category/design.html',context)

    