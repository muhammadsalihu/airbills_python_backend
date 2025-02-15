from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ChatResponse
import json
import random

# Create your views here.
@csrf_exempt
def chat(request):
    if request.method == 'POST':
        data = json.loads(request.body)  # Parse JSON data from the request
        user_message = data.get('message', '')   # Extract Users message

        response = ChatResponse.objects.order_by('?').first() # Get a random response from DB

        return JsonResponse({
            'response': response.content,
            'artifact': {
                'type': response.artifact_type,
                'content': response.artifact_content
            } if response.has_artifact else None
        })