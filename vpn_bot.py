import telebot
import subprocess

# Reemplaza 'TU_TOKEN_AQUI' por el token proporcionado por BotFather
TOKEN = 'TU_TOKEN_AQUI'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'ayuda'])
def send_welcome(message):
    texto = ("🛡️ **Guardián VPN Activado** 🛡️\n\n"
             "Soy tu consola remota. Comandos disponibles:\n"
             "📡 /estado - Muestra el tráfico y los clientes conectados a WireGuard.\n"
             "🖥️ /recursos - Muestra el consumo de RAM y espacio de almacenamiento.")
    bot.reply_to(message, texto, parse_mode='Markdown')

@bot.message_handler(commands=['estado'])
def estado_vpn(message):
    try:
        # Ejecutamos el comando de WireGuard de forma nativa
        resultado = subprocess.check_output(['sudo', 'wg', 'show'], text=True)
        
        if not resultado.strip():
            bot.reply_to(message, "⚠️ La interfaz de WireGuard parece estar inactiva.")
            return

        # Enviamos la salida formateada como bloque de código para mantener la estructura
        respuesta = f"🔒 **Monitor de WireGuard:**\n\n```text\n{resultado}\n```"
        bot.reply_to(message, respuesta, parse_mode='Markdown')
        
    except Exception as e:
        bot.reply_to(message, f"❌ Error al consultar la VPN: {e}")

@bot.message_handler(commands=['recursos'])
def estado_servidor(message):
    try:
        # Consultamos la RAM libre y el espacio en disco raíz
        ram = subprocess.check_output(['free', '-h'], text=True)
        disco = subprocess.check_output(['df', '-h', '/'], text=True)
        
        respuesta = f"🖥️ **Estado del Servidor:**\n\n**RAM:**\n```text\n{ram}```\n**Disco:**\n```text\n{disco}```"
        bot.reply_to(message, respuesta, parse_mode='Markdown')
        
    except Exception as e:
        bot.reply_to(message, f"❌ Error al consultar recursos: {e}")

bot.infinity_polling()