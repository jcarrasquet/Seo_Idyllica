import requests
from requests.auth import HTTPBasicAuth
from config import WC_API_URL, CONSUMER_KEY, CONSUMER_SECRET

def get_all_product_urls():
    auth = HTTPBasicAuth(CONSUMER_KEY, CONSUMER_SECRET)
    page = 1
    urls = []
    while True:
        r = requests.get(WC_API_URL, params={'per_page': 100, 'page': page}, auth=auth)
        if r.status_code != 200:
            print("Error:", r.status_code, r.text)
            break
        data = r.json()
        if not data:
            break
        urls.extend([p['permalink'] for p in data])
        page += 1
    return urls