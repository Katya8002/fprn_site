from django.shortcuts import render, get_object_or_404
from .models import (
    Department, Person, Program, ResearchUnit,
    Partner, NewsItem, StudentOrganization, HomePage,
)


def home(request):
    return render(request, "faculty/home.html", {
        "page": HomePage.objects.first(),
        "leadership": Person.objects.filter(is_leadership=True).order_by("id"),
        "news": NewsItem.objects.order_by("-published_at")[:3],
    })


def program_list(request):
    return render(request, "faculty/program_list.html", {
        "programs": Program.objects.select_related("department"),
    })


def program_detail(request, pk):
    program = get_object_or_404(
        Program.objects.select_related("department"), pk=pk)
    return render(request, "faculty/program_detail.html",
                  {"program": program})


def department_list(request):
    return render(request, "faculty/department_list.html", {
        "departments": Department.objects.prefetch_related("programs"),
    })


def department_detail(request, pk):
    department = get_object_or_404(Department, pk=pk)
    return render(request, "faculty/department_detail.html", {
        "department": department,
        "teachers": department.people.all(),
        "programs": department.programs.all(),
    })


def research_list(request):
    return render(request, "faculty/research_list.html", {
        "units": ResearchUnit.objects.select_related("head"),
    })


def partner_list(request):
    return render(request, "faculty/partner_list.html", {
        "partners": Partner.objects.prefetch_related("departments"),
    })


def organization_list(request):
    return render(request, "faculty/organization_list.html", {
        "organizations": StudentOrganization.objects.all(),
    })