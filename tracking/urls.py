from django.urls import path
from . import views
app_name="tracking"
urlpatterns=[
  path("t/open/<uuid:token>.png",views.open_pixel,name="open"),
  path("t/click/<uuid:token>/",views.click_redirect,name="click"),
  path("t/report/<uuid:token>/",views.report_phish,name="report"),
]
