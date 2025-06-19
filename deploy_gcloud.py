import os
import subprocess
import sys

PROJECT_ID = os.getenv('GCLOUD_PROJECT')
SERVICE_NAME = os.getenv('SERVICE_NAME', 'plomeros-chat-bot')
REGION = os.getenv('GCLOUD_REGION', 'us-central1')


def run(cmd):
    print('Running:', cmd)
    subprocess.check_call(cmd, shell=True)


def deploy():
    run(f'gcloud builds submit --project {PROJECT_ID}')
    run(
        f'gcloud run deploy {SERVICE_NAME} --project {PROJECT_ID} '
        f'--region {REGION} --platform managed --source . '
        '--allow-unauthenticated'
    )


if __name__ == '__main__':
    if not PROJECT_ID:
        print('Please set the GCLOUD_PROJECT environment variable')
        sys.exit(1)
    deploy()
