import csv
import os
import random
from config import HISTORIAL_CSV, N_URLS_DIARIAS

def load_historial():
    enviados = set()
    if os.path.exists(HISTORIAL_CSV):
        with open(HISTORIAL_CSV, newline='', encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if row:
                    enviados.add(row[0])
    return enviados

def select_urls_para_enviar(todas_urls, historial):
    pendientes = list(set(todas_urls) - historial)
    return random.sample(pendientes, min(N_URLS_DIARIAS, len(pendientes)))