from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = 'service_account.json'
FOLDER_ID = '1DXD9LhPTfVNHAAdgrLHq8YSEc4wsa0-f'
FILE_PATH = 'xlsx_data/16-12-2025.xlsx'

creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

service = build('drive', 'v3', credentials=creds)

file_metadata = {
    'name': 'test.jpg',
    'parents': [FOLDER_ID]
}

media = MediaFileUpload(
    FILE_PATH,
    mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
)

file = service.files().create(
    body=file_metadata,
    media_body=media,
    fields='id',
    supportsAllDrives=True
).execute()

print("Uploaded:", file['id'])
