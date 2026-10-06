from django.urls import path
from . import views

app_name = "faculty"

urlpatterns = [
    path("", views.home, name="home"),
    path("programs/", views.program_list, name="program_list"),
    path("programs/<int:pk>/", views.program_detail, name="program_detail"),
    path("departments/", views.department_list, name="department_list"),
    path("departments/<int:pk>/", views.department_detail,
         name="department_detail"),
    path("research/", views.research_list, name="research_list"),
    path("partners/", views.partner_list, name="partner_list"),
    path("students/", views.organization_list, name="organization_list"),
]