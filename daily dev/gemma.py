from google import genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

client = genai.Client( api_key =  os.getenv("GOOGLE_AI_STUDIO_KEY"))
response = client.models.generate_content(
    model = "gemma-3-27b-it", contents = "Explain Transformers to me like I am a beginner developer"
)

print(response.text)