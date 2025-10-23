from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Count, Q
from campaigns.models import Campaign
from tracking.models import TrackingEvent, TrackingLink

@login_required
def home(request):
    user = request.user

    if hasattr(user, "is_admin") and user.is_admin():
        return render(request, "dashboard/admin_home.html", {})

    if hasattr(user, "is_instructor") and user.is_instructor():
        qs = Campaign.objects.all()
        if not user.is_superuser:
            qs = qs.filter(created_by=user)
        campaigns = qs.order_by("-created_at")

        selected = request.GET.get("campaign")
        if selected:
            campaigns = campaigns.filter(id=selected)

        campaign = campaigns.first()
        metrics, top = None, []

        if campaign:
            total_recipients = TrackingLink.objects.filter(campaign=campaign).count()
            events = TrackingEvent.objects.filter(campaign=campaign)

            # Unique recipient counts for each event type
            unique_open = events.filter(type="OPEN").values("recipient").distinct().count()
            unique_click = events.filter(type="CLICK").values("recipient").distinct().count()
            unique_report = events.filter(type="REPORT").values("recipient").distinct().count()

            # Total raw counts (for display)
            total_open = events.filter(type="OPEN").count()
            total_click = events.filter(type="CLICK").count()
            total_report = events.filter(type="REPORT").count()

            def rate(unique):
                return round((unique / total_recipients) * 100, 1) if total_recipients else 0.0

            metrics = {
                "total_recipients": total_recipients,
                "opens": total_open,
                "clicks": total_click,
                "reports": total_report,
                "open_rate": rate(unique_open),
                "click_rate": rate(unique_click),
                "report_rate": rate(unique_report),
            }

            top = (
                events.values("recipient__email")
                .annotate(
                    opens=Count("id", filter=Q(type="OPEN")),
                    clicks=Count("id", filter=Q(type="CLICK")),
                    reports=Count("id", filter=Q(type="REPORT")),
                    total=Count("id"),
                )
                .order_by("-total")[:10]
            )

        ctx = {
            "campaigns": Campaign.objects.filter(created_by=user)
            if not user.is_superuser
            else Campaign.objects.all(),
            "campaign": campaign,
            "metrics": metrics,
            "top": top,
            "rate_rows": [
                ("Open", metrics["open_rate"] if metrics else 0),
                ("Click", metrics["click_rate"] if metrics else 0),
                ("Report", metrics["report_rate"] if metrics else 0),
            ] if metrics else [],
        }
        return render(request, "dashboard/instructor_home.html", ctx)

    return render(request, "dashboard/recipient_home.html", {})
