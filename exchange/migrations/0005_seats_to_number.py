import re

from django.db import migrations, models


def parse_seats(raw):
    match = re.search(r"\d+", raw)
    if not match:
        raise ValueError(f"Не вдалося розпізнати кількість місць: {raw!r}")
    number = int(match.group())
    is_maximum = raw.strip().lower().startswith("до")
    return number, is_maximum


def forwards(apps, schema_editor):
    ExchangeProgram = apps.get_model("exchange", "ExchangeProgram")
    for program in ExchangeProgram.objects.all():
        number, is_maximum = parse_seats(program.seats)
        program.seats_number = number
        program.seats_is_maximum = is_maximum
        program.save(update_fields=["seats_number", "seats_is_maximum"])


def backwards(apps, schema_editor):
    ExchangeProgram = apps.get_model("exchange", "ExchangeProgram")
    for program in ExchangeProgram.objects.all():
        text = str(program.seats_number)
        if program.seats_is_maximum:
            text = f"до {text}"
        program.seats = text
        program.save(update_fields=["seats"])


class Migration(migrations.Migration):

    dependencies = [
        ("exchange", "0004_split_university_country"),
    ]

    operations = [
        migrations.AddField(
            model_name="exchangeprogram",
            name="seats_number",
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name="exchangeprogram",
            name="seats_is_maximum",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="exchangeprogram",
            name="seats",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.RunPython(forwards, backwards),
        migrations.RemoveField(
            model_name="exchangeprogram",
            name="seats",
        ),
        migrations.RenameField(
            model_name="exchangeprogram",
            old_name="seats_number",
            new_name="seats",
        ),
        migrations.AlterField(
            model_name="exchangeprogram",
            name="seats",
            field=models.PositiveIntegerField(),
        ),
    ]