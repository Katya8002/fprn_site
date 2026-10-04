from django.shortcuts import render
from .models import ExchangeProgram


def exchange_list(request):
    programs = ExchangeProgram.objects.order_by("deadline")
    return render(request, "exchange/exchange_list.html",
                  {"programs": programs})