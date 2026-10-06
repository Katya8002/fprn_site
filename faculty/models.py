from django.db import models
from django.utils import timezone


class Department(models.Model):
    name = models.CharField(max_length=200)
    head = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Person(models.Model):
    full_name = models.CharField(max_length=200)
    position = models.CharField(max_length=200, blank=True)
    degree = models.CharField(max_length=200, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    office = models.CharField(max_length=100, blank=True)
    is_leadership = models.BooleanField(default=False)
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="people",
    )

    def __str__(self):
        return self.full_name


class Program(models.Model):
    name = models.CharField(max_length=200)
    specialty_code = models.CharField(max_length=20, blank=True)
    description = models.TextField(blank=True)
    coordinator_name = models.CharField(max_length=200, blank=True)
    coordinator_contact = models.CharField(max_length=200, blank=True)
    disciplines = models.TextField(
        blank=True, help_text="По одній дисципліні на рядок")
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="programs",
    )

    def __str__(self):
        return self.name


class ResearchUnit(models.Model):
    class UnitType(models.TextChoices):
        CENTER = "center", "Центр"
        LABORATORY = "laboratory", "Лабораторія"

    name = models.CharField(max_length=200)
    unit_type = models.CharField(max_length=20, choices=UnitType.choices)
    head = models.ForeignKey(
        Person,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="led_units",
    )

    def __str__(self):
        return self.name


class Partner(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=100, blank=True)
    departments = models.ManyToManyField(
        Department, related_name="partners", blank=True
    )

    def __str__(self):
        return self.name


class NewsItem(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField(blank=True)
    published_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class StudentOrganization(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.name

class HomePage(models.Model):
    title = models.CharField(
        max_length=200, default="Факультет природничих наук")
    description = models.TextField(blank=True)
    contacts = models.TextField(blank=True)

    def __str__(self):
        return self.title