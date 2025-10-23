from django.core.management.base import BaseCommand
from campaigns.models import Campaign
from recipients.models import RecipientContact
from tracking.models import TrackingLink

class Command(BaseCommand):
    def add_arguments(self,parser):
        parser.add_argument("--campaign",required=True)
        parser.add_argument("--landing-slug",default="mock-password-reset")
    def handle(self,*a,**o):
        camp=Campaign.objects.get(name=o["campaign"])
        base=f"http://127.0.0.1:8000/learn/{o['landing_slug']}/"
        c=0
        for rc in RecipientContact.objects.all():
            _,new=TrackingLink.objects.get_or_create(campaign=camp,recipient=rc,defaults={"target_url":base})
            if new:c+=1
        self.stdout.write(self.style.SUCCESS(f"Tracking links: {c}"))
