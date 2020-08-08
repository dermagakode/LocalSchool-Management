from django.contrib import admin
from .models import TeachingMaterials, Attachments

class AttachmentsStack(admin.TabularInline):
    model = Attachments
    extra = 0

class TeachingMaterialsAdmin(admin.ModelAdmin):
    list_display = (
        'school',
        'grade',
        'subject',
        'topic'
    )

    inlines = (
        AttachmentsStack,
    )

admin.site.register(TeachingMaterials, TeachingMaterialsAdmin)
