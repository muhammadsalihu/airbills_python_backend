from supabase import create_client
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch Supabase URL and key from environment variables
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")

# Check if the necessary environment variables are loaded
if not supabase_url or not supabase_key:
    raise ValueError("Supabase URL or key is missing. Please check your .env file.")

# Initialize Supabase Client
supabase = create_client(supabase_url, supabase_key)

# Now you can use the 'supabase' client to interact with your Supabase instance
