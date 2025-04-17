import os
import json
import csv
from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession

# 🟢 Leer el contenido JSON desde la variable de entorno
credentials_json_str = os.environ['GOOGLE_CREDENTIALS_JSON']
credentials_info = json.loads(credentials_json_str)

SCOPES = ["https://www.googleapis.com/auth/indexing"]
credentials = service_account.Credentials.from_service_account_info(credentials_info, scopes=SCOPES)
authed_session = AuthorizedSession(credentials)

# ✅ Enviar una URL
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

# 💾 Guardar en historial CSV
def guardar_en_historial(urls, csv_file="enviados_a_google.csv"):
    with open(csv_file, "a", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        for url in urls:
            writer.writerow([url])

