import json
import csv
from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession
from config import CLAVE_GOOGLE, HISTORIAL_CSV

# 🔐 Autenticación desde variable de entorno
credentials_json_str = os.environ['GOOGLE_CREDENTIALS_JSON']
credentials_info = json.loads(credentials_json_str)
SCOPES = ["https://www.googleapis.com/auth/indexing"]
credentials = service_account.Credentials.from_service_account_file(CLAVE_GOOGLE, scopes=SCOPES)
authed_session = AuthorizedSession(credentials)

def notify_url(url):
    endpoint = "https://indexing.googleapis.com/v3/urlNotifications:publish"
    payload = {
        "url": url,
        "type": "URL_UPDATED"
    }
    response = authed_session.post(endpoint, json=payload)
    if response.status_code == 200:
        print(f"✅ Notificado: {url}")
        return True
    else:
        print(f"❌ Error: {url} — {response.text}")
        return False

def guardar_en_historial(urls):
    with open(HISTORIAL_CSV, "a", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        for url in urls:
            writer.writerow([url])
