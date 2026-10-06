from django.contrib import admin
from .models import ExchangeProgram


@admin.register(ExchangeProgram)
class ExchangeProgramAdmin(admin.ModelAdmin):
    list_display = ("university", "country", "languages", "seats",
                    "seats_is_maximum", "deadline", "status")
    list_filter = ("country",)

    @admin.display(boolean=True, description="Прийом триває")
    def status(self, obj):
        return obj.is_open