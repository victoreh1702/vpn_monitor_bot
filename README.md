# Guardián VPN - Server & Network Monitor 🛡️📡

Un bot de Telegram ultraligero desarrollado en Python para monitorizar en tiempo real el estado de una red VPN WireGuard y los recursos de hardware en servidores Linux. Diseñado específicamente para funcionar con un consumo imperceptible en entornos cloud, como las instancias Always Free de Oracle Cloud.

## 🚀 Características Principales

*   **Monitorización de WireGuard:** Lectura directa del estado de la interfaz `wg0`. Muestra al instante los clientes conectados (peers), IPs asignadas, tiempos de conexión (handshakes) y tráfico de red consumido.
*   **Control de Hardware:** Consulta instantánea de la memoria RAM disponible (incluyendo buffers y swap) y la partición de almacenamiento del disco duro.
*   **Ejecución Nativa en Linux:** Utiliza el módulo `subprocess` de Python para ejecutar comandos nativos del sistema operativo (`wg show`, `free -h`, `df -h`) y capturar su salida, actuando como una terminal remota segura desde Telegram.
*   **Aislamiento de Procesos:** Corre de forma independiente en segundo plano sin interferir con el tráfico de la VPN ni con otros bots alojados en la misma máquina.

## 🛠 Stack Tecnológico

*   **Lenguaje:** Python 3
*   **Librerías Core:** `pyTelegramBotAPI` (Telebot), `subprocess`
*   **Infraestructura:** Linux/Ubuntu (Oracle Cloud Infrastructure - OCI)
*   **Redes:** Protocolo WireGuard

## 📋 Comandos Disponibles

| Comando | Descripción |
| :--- | :--- |
| `/start` o `/ayuda` | Muestra el panel principal y la lista de comandos. |
| `/estado` | Imprime el registro de WireGuard con los dispositivos enlazados y su consumo de datos. |
| `/recursos` | Despliega el uso actual de memoria RAM y el espacio libre en el disco del servidor. |

## ⚙️ Despliegue en Servidor

Para levantar el servicio desde cero en un entorno Linux/Ubuntu mediante conexión SSH:

1. **Crear el entorno virtual e instalar dependencias:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install pyTelegramBotAPI
   ```

2. **Configuración del Script:**
   Crea el archivo `vpn_bot.py`, pega el código fuente del proyecto y sustituye la variable `TOKEN` por el token de acceso proporcionado por BotFather.

3. **Ejecución persistente (Nohup):**
   Lanza el proceso en segundo plano para poder desconectarte del servidor sin interrumpir el bot:
   ```bash
   nohup python vpn_bot.py &
   ```
   *Una vez ejecutado, el bot quedará a la escucha en Telegram las 24 horas del día.*