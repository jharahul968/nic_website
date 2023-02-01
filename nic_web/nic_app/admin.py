from django.contrib import admin

# Register your models here.

from django.contrib import admin

from nic_app.models import Instrument


@admin.register(Instrument)
class InstrumentAdmin(admin.ModelAdmin):
    pass
