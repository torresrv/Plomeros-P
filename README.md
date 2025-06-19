# Plomeros Chatbot

This repository contains a minimal Flask-based chatbot application. The project is configured so it can be deployed to Google Cloud Run using the Google Cloud SDK.

## Requirements

- Python 3.10+
- `gcloud` command line tool
- A Google Cloud project with billing enabled

## Local Development

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the server locally:

```bash
python main.py
```

Send a POST request to `http://localhost:8080/chat` with a JSON body like `{"message": "hola"}` and you will get a simple echo reply.

## WhatsApp Integration

Set the following environment variables to enable sending WhatsApp messages using the [WhatsApp Cloud API](https://developers.facebook.com/docs/whatsapp/cloud-api):

- `WHATSAPP_TOKEN` – your WhatsApp access token
- `WHATSAPP_PHONE_ID` – the phone number ID associated with your Meta app

Run the server and send a POST request to `/whatsapp` with a JSON body:

```json
{
  "to": "<DESTINATION_PHONE_NUMBER>",
  "message": "Hola desde la API"
}
```

If the request succeeds, the server responds with `{"status": "sent"}`.

## Deploy to Google Cloud Run

1. [Install the Google Cloud SDK](https://cloud.google.com/sdk) and authenticate:

```bash
gcloud auth login
gcloud config set project <YOUR_PROJECT_ID>
```

2. Set the environment variable `GCLOUD_PROJECT` to your project ID (optionally `SERVICE_NAME` and `GCLOUD_REGION`):

```bash
export GCLOUD_PROJECT=<YOUR_PROJECT_ID>
```

3. Run the deployment script:

```bash
python deploy_gcloud.py
```

The script builds the container image and deploys it to Cloud Run. When deployment is complete, `gcloud` will output the service URL where your chatbot is available.
