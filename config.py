import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "21796677")

API_HASH = os.environ.get("API_HASH", "bae470bd3dd2707adce4c659d82545d0")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

FORCE_SUB = os.environ.get("FORCE_SUB", "heart_botz") 

DB_NAME = os.environ.get("DB_NAME","rename")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://rename:OToSKUK8UlmMA6P0@cluster0.3gj0t.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]

PORT = os.environ.get("PORT", "8080")
