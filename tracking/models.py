import uuid
from django.db import models
from campaigns.models import Campaign
from recipients.models import RecipientContact

class TrackingLink(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name="tracking_links")
    recipient = models.ForeignKey(RecipientContact, on_delete=models.CASCADE, related_name="tracking_links")
    token = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True)
    target_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ("campaign", "recipient")
    def __str__(self): return f"{self.campaign.name} -> {self.recipient.email}"

class TrackingEvent(models.Model):
    OPEN="OPEN"; CLICK="CLICK"; REPORT="REPORT"; LANDING_VIEW="LANDING_VIEW"
    TYPE_CHOICES=[(OPEN,"Open"),(CLICK,"Click"),(REPORT,"Report"),(LANDING_VIEW,"Landing View")]
    campaign=models.ForeignKey(Campaign,on_delete=models.CASCADE,related_name="events")
    recipient=models.ForeignKey(RecipientContact,on_delete=models.CASCADE,related_name="events")
    link=models.ForeignKey(TrackingLink,null=True,blank=True,on_delete=models.SET_NULL,related_name="events")
    type=models.CharField(max_length=20,choices=TYPE_CHOICES)
    ip_addr=models.GenericIPAddressField(null=True,blank=True)
    user_agent=models.TextField(blank=True)
    path=models.CharField(max_length=512,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    meta=models.JSONField(default=dict,blank=True)
    def __str__(self): return f"{self.type} {self.recipient.email} {self.created_at:%Y-%m-%d %H:%M}"
