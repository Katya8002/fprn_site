from django.contrib import admin
from .models import (
    Department, Person, Program, ResearchUnit,
    Partner, NewsItem, StudentOrganization, HomePage,
)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "head")


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("full_name", "position", "degree", "office", "phone", "department")
    list_filter = ("department",)
    search_fields = ("full_name",)


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ("name", "specialty_code", "coordinator_name", "department")
    list_filter = ("department",)


@admin.register(ResearchUnit)
class ResearchUnitAdmin(admin.ModelAdmin):
    list_display = ("name", "unit_type", "head")


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ("name", "country")
    filter_horizontal = ("departments",)


@admin.register(NewsItem)
class NewsItemAdmin(admin.ModelAdmin):
    list_display = ("title", "published_at")


@admin.register(StudentOrganization)
class StudentOrganizationAdmin(admin.ModelAdmin):
    list_display = ("name", "url")


@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not HomePage.objects.exists()