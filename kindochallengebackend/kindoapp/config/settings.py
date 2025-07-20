import os

from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Loading the env variables as settings variables
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")
SMTP_HOST = os.getenv("SMTP_HOST", "email-smtp.us-east-1.amazonaws.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
DB_USERNAME=os.getenv("DB_USERNAME")
DB_PASSWORD=os.getenv("DB_PASSWORD")
DB_HOST=os.getenv("DB_HOST", "localhost")
DB_PORT=int(os.getenv("DB_PORT", 5432))
