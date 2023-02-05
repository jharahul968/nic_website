from django.contrib import admin

# Register your models here.

from django.contrib import admin

from nic_app.models import *


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Ongoing)
class OngoingAdmin(admin.ModelAdmin):
    pass
