from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_GET, require_POST
from .models import TrackingLink, TrackingEvent
from landing.models import LandingPage

_PIXEL=bytes.fromhex("89504E470D0A1A0A0000000D49484452000000010000000108060000001F15C4890000000A49444154789C636000000200010005FE02FEA7B2DE0000000049454E44AE426082")

def _log(event_type,link,request):
    TrackingEvent.objects.create(
        campaign=link.campaign,recipient=link.recipient,link=link,type=event_type,
        ip_addr=request.META.get("REMOTE_ADDR"),user_agent=request.META.get("HTTP_USER_AGENT",""),path=request.path)

@require_GET
def open_pixel(request,token):
    link=get_object_or_404(TrackingLink,token=token)
    _log("OPEN",link,request)
    r=HttpResponse(_PIXEL,content_type="image/png")
    r["Cache-Control"]="no-store"
    return r

@require_GET
def click_redirect(request,token):
    link=get_object_or_404(TrackingLink,token=token)
    _log("CLICK",link,request)
    return HttpResponseRedirect(f"{link.target_url}?t={link.token}")

@require_POST
def report_phish(request,token):
    link=get_object_or_404(TrackingLink,token=token)
    _log("REPORT",link,request)
    return HttpResponse("Thanks for reporting!",content_type="text/plain")

@require_GET
def landing_view(request,slug):
    page=get_object_or_404(LandingPage,slug=slug,is_active=True)
    t=request.GET.get("t")
    if t:
        try:_log("LANDING_VIEW",TrackingLink.objects.get(token=t),request)
        except TrackingLink.DoesNotExist:pass
    return render(request,"landing/learn.html",{"page":page})
