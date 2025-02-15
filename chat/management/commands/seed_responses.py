from django.core.management import BaseCommand
from chat.models import ChatResponse

RESPONSES = [
       {
        "content": "Here's an analysis of the latest F1 race performance metrics.",
        "category": "racing",
        "has_artifact": True,
        "artifact_type": "markdown",
        "artifact_content": """# Race Analysis
- Top Speed: 340 km/h
- Fastest Lap: 1:24.634
- Tire Strategy: Medium → Hard → Soft"""
    },
]


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for response in RESPONSES:
            ChatResponse.objects.create(**response)