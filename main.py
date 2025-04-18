from extract_products import get_all_product_urls
from select_urls import load_historial, select_urls_para_enviar, reset_historial
from indexing_api import notify_url, guardar_en_historial

def main():
    print("📦 Extrayendo productos...")
    todas = get_all_product_urls()

    print("🗂️ Cargando historial...")
    historial = load_historial()

    print("🎯 Seleccionando URLs para enviar...")
    urls = select_urls_para_enviar(todas, historial)

    if not urls:
        print("🔁 Historial completo, reiniciando...")
        reset_historial()
        historial = set()
        urls = select_urls_para_enviar(todas, historial)

    print(f"🚀 Enviando {len(urls)} URLs a Google...")
    nuevas = []
    for url in urls:
        if notify_url(url):
            nuevas.append(url)

    print("💾 Actualizando historial...")
    guardar_en_historial(nuevas)

    resumen = f"""
✅ Proceso completado

🔢 Total URLs enviadas hoy: {len(nuevas)}

🔗 URLs:
""" + "\n".join(nuevas)

    with open("resumen.txt", "w", encoding="utf-8") as f:
        f.write(resumen.strip())

    print("📧 Resumen generado para el correo.")

if __name__ == "__main__":
    main()
