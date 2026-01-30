from django.urls import path
from .views import *

urlpatterns = [
    path('itfiled/',it_field,name="it_field"),
    path('customerservice/',customer_service,name="customer_service"),
    path('humanresource/',human_resource,name="human_resource"),
    path('workfromhome/',work_from_home,name="work_from_home"),
    path('mechanicaljob/',mechanical_job,name="mechanical_job"),
    path('automobile/',automobile,name="automobile"),
    path('education/',education,name="education"),
    path('design/',design,name="design"),
]