import requests
import json
from datetime import datetime

def obtener_datos():
    print("Iniciando extracción de datos...")
    
    # 1. API CoinGecko: Obtener Bitcoin y Ethereum en USD
    url_crypto = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
    resp_crypto = requests.get(url_crypto)
    datos_crypto = resp_crypto.json()
    
    btc_usd = datos_crypto["bitcoin"]["usd"]
    eth_usd = datos_crypto["ethereum"]["usd"]
    
    # 2. API Exchange Rate: Obtener cotización USD a ARS (Pesos Argentinos)
    url_fiat = "https://open.er-api.com/v6/latest/USD"
    resp_fiat = requests.get(url_fiat)
    datos_fiat = resp_fiat.json()
    
    usd_ars = datos_fiat["rates"]["ARS"]
    
    # 3. Transformación / Procesamiento de datos
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    registro_completo = {
        "timestamp": timestamp,
        "fiat_rates": {
            "USD_ARS": round(usd_ars, 2)
        },
        "crypto_rates_usd": {
            "bitcoin": btc_usd,
            "ethereum": eth_usd
        },
        "crypto_rates_ars": {
            "bitcoin": round(btc_usd * usd_ars, 2),
            "ethereum": round(eth_usd * usd_ars, 2)
        }
    }
    
    return registro_completo

if __name__ == "__main__":
    reporte = obtener_datos()
    print("\n--- REPORTE CONSOLIDADO ---")
    print(json.dumps(reporte, indent=4, ensure_ascii=False))

# Guardar en archivo local
    with open("market_history.json", "a") as f:
        f.write(json.dumps(reporte, ensure_ascii=False) + "\n")
    print("\n¡Registro guardado en market_history.json!")