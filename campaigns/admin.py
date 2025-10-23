from django.contrib import admin
from .models import EmailTemplate, Campaign


@admin.register(EmailTemplate)
class EmailTemplateAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'created_by', 'created_at']
    list_filter = ['created_at', 'created_by']
    search_fields = ['name', 'subject']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ['name', 'template', 'status', 'created_by', 'created_at']
    list_filter = ['status', 'created_at', 'created_by']
    search_fields = ['name', 'template__name']
    readonly_fields = ['created_at', 'updated_at']