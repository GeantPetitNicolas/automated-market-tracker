# 📈 Automated Market Tracker & ETL Pipeline

Un pipeline de datos automatizado construido en Python que extrae, transforma y consolida diariamente métricas financieras clave de criptomonedas y divisas locales.

## 🛠️ Tecnologías utilizadas

* **Lenguaje:** Python 3.10
* **APIs:** CoinGecko API (Criptomonedas) & ExchangeRate-API (Fiat / ARS)
* **Automatización & Cloud:** GitHub Actions (CI/CD Scheduled Workflows)
* **Formato de datos:** JSON (Historización continua)

## ⚙️ Arquitectura del Pipeline

1. **Extraction (E):** Se realiza una consulta HTTP asíncrona a las APIs de mercado para obtener cotizaciones en tiempo real de Bitcoin, Ethereum y el tipo de cambio USD/ARS.
2. **Transformation (T):** El script calcula automáticamente los valores de las criptomonedas convertidos a moneda local (ARS) y normaliza la estructura con una marca temporal (ISO Timestamp).
3. **Loading (L):** El registro consolidado se añade de forma continua al archivo histórico `market_history.json`.
4. **Orchestration:** Un runner de GitHub Actions ejecuta este flujo de forma automatizada cada 24 horas (o bajo demanda vía `workflow_dispatch`).

## 🚀 Ejecución Local

1. Clonar el repositorio:
   ```bash
   git clone [https://github.com/GeantPetitNicolas/automated-market-tracker.git](https://github.com/GeantPetitNicolas/automated-market-tracker.git)