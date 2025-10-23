from django.contrib import admin
from .models import RecipientList, RecipientContact


@admin.register(RecipientList)
class RecipientListAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'created_at']
    list_filter = ['created_at', 'owner']
    search_fields = ['name']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(RecipientContact)
class RecipientContactAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name', 'department', 'recipient_list']
    list_filter = ['department', 'recipient_list', 'created_at']
    search_fields = ['email', 'first_name', 'last_name']
    readonly_fields = ['created_at', 'updated_at']