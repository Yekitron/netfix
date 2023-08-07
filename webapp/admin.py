from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Movies


@admin.register(Movies)
class update(ImportExportModelAdmin):
    pass
