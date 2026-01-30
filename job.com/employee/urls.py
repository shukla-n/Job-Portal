from django.urls import path
from .views import *

urlpatterns = [
    path("employee/home/", employee_home, name="employee_home"),
    path("employee/profile/", employee_profile, name="employee_profile"),
    path("employee/profile/edit/", employee_profile_edit, name="employee_profile_edit"),
    path("employee/profile/add/exp/", add_experiences, name="add_experiences"),
    path("employee/profile/add/edu/", add_educations, name="add_educations"),
    path("employee/profile/add/pro/", add_project, name="add_project"),
    path("employee/profile/add/skl/", add_skill, name="add_skill"),
    path("employee/job/<int:id>/details/", job_details, name="job_details"),
    path("employee/job/<int:id>/apply/", apply_sts, name="apply_sts"),
    path("employee/applied/jobs/", employee_appliedjob, name="employee_appliedjob"),
]
