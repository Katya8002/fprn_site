import re

from django.db import migrations

PAREN = re.compile(r"^(?P<name>.+?)\s*\((?P<country>[^()]+)\)\s*$")
DASH = re.compile(r"^(?P<name>.+?)\s+[-–—]\s+(?P<country>[^-–—]+)$")
COMMA = re.compile(r"^(?P<name>.+),\s*(?P<country>[^,]+)$")


def split_university(value):
    value = value.strip()
    for pattern in (PAREN, DASH, COMMA):
        match = pattern.match(value)
        if match:
            return match.group("name").strip(), match.group("country").strip()
    return value, ""


def forwards(apps, schema_editor):
    ExchangeProgram = apps.get_model("exchange", "ExchangeProgram")
    for program in ExchangeProgram.objects.all():
        name, country = split_university(program.university)
        program.university = name
        program.country = country
        program.save(update_fields=["university", "country"])


def backwards(apps, schema_editor):
    ExchangeProgram = apps.get_model("exchange", "ExchangeProgram")
    for program in ExchangeProgram.objects.all():
        if program.country:
            program.university = f"{program.university}, {program.country}"
            program.country = ""
            program.save(update_fields=["university", "country"])


class Migration(migrations.Migration):

    dependencies = [
        ("exchange", "0003_exchangeprogram_country"),
    ]

    operations = [
        migrations.RunPython(forwards, backwards),
    ]