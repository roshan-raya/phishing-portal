from django.contrib import admin
from django.urls import path, include
from tracking import views as tracking_views

urlpatterns = [
    path('', include(('tracking.urls','tracking'),namespace='tracking')),
    path('learn/<slug:slug>/', tracking_views.landing_view, name='learn'),
    path("admin/", admin.site.urls),
    path("", include("dashboard.urls")),
    path("auth/", include("accounts.urls")),
]
