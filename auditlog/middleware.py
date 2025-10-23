from .models import AuditEntry

class AuditLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        resp = self.get_response(request)

        try:
            AuditEntry.objects.create(
                user=request.user if request.user.is_authenticated else None,
                path=request.path,
                method=request.method,
                ip=(request.META.get("HTTP_X_FORWARDED_FOR","").split(",")[0].strip() or request.META.get("REMOTE_ADDR")),
                user_agent=request.META.get("HTTP_USER_AGENT", ""),
                action="VIEW"
            )
        except Exception:
            pass  # don't break UX due to audit

        return resp
