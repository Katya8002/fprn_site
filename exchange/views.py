from django.shortcuts import render
from .models import ExchangeProgram


def exchange_list(request):
    programs = ExchangeProgram.objects.order_by("deadline")
    selected = request.GET.get("country", "")
    if selected:
        programs = programs.filter(country=selected)
    countries = (
        ExchangeProgram.objects.exclude(country="")
        .order_by("country")
        .values_list("country", flat=True)
        .distinct()
    )
    return render(request, "exchange/exchange_list.html", {
        "programs": programs,
        "countries": countries,
        "selected": selected,
    })