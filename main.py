import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# WhatsApp Cloud API configuration
WHATSAPP_TOKEN = os.getenv('WHATSAPP_TOKEN')
WHATSAPP_PHONE_ID = os.getenv('WHATSAPP_PHONE_ID')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json(silent=True) or {}
    message = data.get('message', '')
    reply = f"Echo: {message}"
    return jsonify({'reply': reply})


@app.route('/whatsapp', methods=['POST'])
def send_whatsapp():
    """Send a WhatsApp message using the Cloud API."""
    if not WHATSAPP_TOKEN or not WHATSAPP_PHONE_ID:
        return jsonify({'error': 'WhatsApp API not configured'}), 500

    data = request.get_json(silent=True) or {}
    to = data.get('to')
    text = data.get('message', '')
    if not to or not text:
        return jsonify({'error': 'Missing "to" or "message" field'}), 400

    url = f"https://graph.facebook.com/v18.0/{WHATSAPP_PHONE_ID}/messages"
    headers = {
        'Authorization': f'Bearer {WHATSAPP_TOKEN}',
        'Content-Type': 'application/json',
    }
    payload = {
        'messaging_product': 'whatsapp',
        'to': to,
        'type': 'text',
        'text': {
            'preview_url': False,
            'body': text,
        },
    }

    resp = requests.post(url, json=payload, headers=headers)
    if resp.status_code != 200:
        return jsonify({'error': 'Failed to send message', 'details': resp.text}), 500

    return jsonify({'status': 'sent'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
