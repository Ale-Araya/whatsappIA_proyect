# Bot Automatizado de WhatsApp

Este repositorio contiene el código de un bot automatizado que utiliza WhatsApp para responder mensajes. Utiliza OCR para leer el contenido de la pantalla y pyautogui para simular interacciones del usuario.

## Funcionalidades
- **Ajuste de Pixel**: Calcula la relación entre los píxeles de la pantalla y la captura de imagen para interacciones precisas.
- **Abrir WhatsApp**: Inicia automáticamente la aplicación de WhatsApp.
- **Enviar Respuesta**: Envía respuestas automatizadas a los mensajes recibidos.
- **Buscar Respuesta**: Genera respuestas utilizando búsquedas en línea y ChatGPT.
- **Buscar Nuevo Mensaje**: Detecta y reacciona a nuevos mensajes en WhatsApp.

## Requisitos
- Python 3.x
- Bibliotecas: pyautogui, pytesseract, PIL, etc.

## Configuración
Asegúrese de configurar las rutas de las imágenes y los comandos específicos del sistema operativo antes de ejecutar el bot.

## Uso
Para utilizar el bot, ejecute `main.py` y permita que interactúe con su sesión de WhatsApp abierta en una instancia de escritorio.

**Nota:** Este bot está diseñado para demostraciones y propósitos educativos. No se recomienda su uso para spam o actividades no autorizadas en WhatsApp.
