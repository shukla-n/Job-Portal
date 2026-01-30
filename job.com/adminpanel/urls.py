from django.urls import path
from .views import *

urlpatterns = [
    path('siteadmin/home/',admin_homepage,name="admin_homepage"),
    path('siteadmin/employees/',admin_employees_details,name="admin_employees_details"),
    path('siteadmin/companies/',admin_companies_details,name="admin_companies_details"),
    
    path('siteadmin/companie/<int:id>/delete/',delete_account_company,name="delete_account_company"),
    path('siteadmin/employee/<int:id>/delete/',delete_account_employee,name="delete_account_employee"),
    
    path('siteadmin/companies/permissions/',login_permissions,name="login_permissions"),
    path('siteadmin/<int:id>/permissions/done/',permission_done,name="permission_done"),
    
    path('siteadmin/<int:id>/permissions/sts/',approve_sts,name="approve_sts"),
]
