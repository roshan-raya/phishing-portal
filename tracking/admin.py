from django.contrib import admin
from .models import TrackingLink, TrackingEvent
@admin.register(TrackingLink)
class TLAdmin(admin.ModelAdmin):
    list_display=("token","campaign","recipient","target_url","created_at")
@admin.register(TrackingEvent)
class TEAdmin(admin.ModelAdmin):
    list_display=("type","campaign","recipient","created_at","ip_addr")
