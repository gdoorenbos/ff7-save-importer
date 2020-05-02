import pickle
import os.path
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from ff7_gen_cksum import calc_cksum, _save_filename
from ff7_get_user_id import get_user_id, _ff7_steam_dir

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive.file']

FOLDER_NAME = 'My FF7 Save Data'

def get_drive_service():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build('drive', 'v3', credentials=creds)

def get_folder(drive_service):
    # first, see if the folder already exists
    page_token = None
    while True:
        response = drive_service.files().list(q="mimeType='application/vnd.google-apps.folder' and trashed=false",
                                              spaces='drive',
                                              fields='nextPageToken, files(id, name)',
                                              pageToken=page_token).execute()

        for file in response.get('files', []):
            if file.get('name') == FOLDER_NAME:
                return file

        page_token = response.get('nextPageToken', None)
        if not page_token:
            break;

    # if we get here, the folder does not exist. Create it.
    folder_metadata = {
        'name': FOLDER_NAME,
        'mimeType': 'application/vnd.google-apps.folder'
    }
    return drive_service.files().create(body=folder_metadata, fields='id, name').execute()

def upload_save_file(drive_service, folder):
    # build path to local save file
    local_save = _ff7_steam_dir + "/user_" + get_user_id() + "/" + _save_filename
    
    # Don't overwrite the save file - just keep uploading duplicates
    # This will preserve playthrough history
    file_metadata = {
        'name': _save_filename,
        'parents': [folder.get('id')]
    }
    media = MediaFileUpload(local_save)
    return drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()

def main():
    drive_service = get_drive_service()
    
    folder = get_folder(drive_service)
    print('Folder ID: %s' % folder.get('id'))
    
    file = upload_save_file(drive_service, folder)
    print('file id: %s' % file.get('id'))

if __name__ == '__main__':
    main()