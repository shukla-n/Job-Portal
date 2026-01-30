from django.urls import path
from .views import *

urlpatterns = [
    path("company/home/", company_home, name="company_home"),
    path("company/profile/", company_profile, name="company_profile"),
    path("company/profile/edit/", company_profile_edit, name="company_profile_edit"),
    path("company/post/job/", post_job, name="post_job"),
    path("company/job/<int:id>/details/", details_job, name="details_job"),
    path("company/job/<int:id>/status/", job_status, name="job_status"),
    path( "company/applied/<int:id>/user/", applied_employee_profile, name="applied_employee_profile"),
    path('emp/<int:id>/', status_change, name='empl_status_change')
]
 