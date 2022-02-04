from __future__ import print_function
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.http import MediaIoBaseUpload
import googleapiclient.errors
from  tqdm  import  tqdm
import requests
import os.path
import time
import io
from settings import SCOPES


class GoogleDrive:
    """
    Класс GoogleDrive - используется для работы с Google.Drive.

    Основное применение - работа с файлами на Google.Drive.

    Methods
    -------
        get_files_google_drive():
            возвращает список файлов на Google.Drive.

        create_directory_google_drive(name: str):
            создаёт папку на Google.Drive.

        download_files_google_drive(folder_id: str, list_name: list):
            загружает файл по url на Google.Drive.

        delete_files_google_drive(fileId: str):
            удаляет файл на Google.Drive.

    """

    def __init__(self):

        creds = None

        # Файл token.json хранит токены доступа и обновления пользователя,
        # он создается автоматически, когда поток авторизации завершается.
        if os.path.exists('classes/token.json'):
            creds = Credentials.from_authorized_user_file('classes/token.json', SCOPES)

        # Если нет доступных (действительных) учетных данных, позвольте пользователю войти в систему.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'classes/credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)

            # Сохранение учетных данных для следующего запуска.
            with open('classes/token.json', 'w', encoding='utf-8') as token:
                token.write(creds.to_json())

        # Сервис, который будет использовать 3ю версию REST API Google.Drive,
        # отправляя запросы из-под учетных данных credentials.
        self.service = build('drive', 'v3', credentials=creds)

    def get_files_google_drive(self):
        """
        Метод получения списка файлов на Google.Drive.

        pageSize: int
            количество результатов выдачи

        fields: дополнительные поля

            nextPageToken: str
                токен следующей страницы, если все результаты не помещаются в один ответ.

            files()
                параметр, указывающий, что нужно возвращать список файлов,
                где в скобках указан список полей для файлов, которые нужно показывать в результатах выдачи.

                В данном случае указаны поля для файлов:
                id - идентификатор файла,
                name - имя файла,
                mimeType - тип файла,
                parents — ID папки, в которой расположен файл/подпапка,
                createdTime — дата создания файла/папки.

                Со всеми возможными полями можно ознакомиться в документации:
                https://developers.google.com/drive/api/v3/reference/files

        pageToken: str
            токен страницы с результатом запроса.

        В качестве возврата (return) метод использует список res_list с информацией о файлах на Google.Drive.

        Ссылка на официальную документацию: https://developers.google.com/drive/api/v3/reference/files/get

        """

        # Вызов API Drive v3
        results = self.service.files().list(pageSize=10,
                                       fields="nextPageToken, files(id, name, mimeType, parents, createdTime)").execute()
        nextPageToken = results.get('nextPageToken')

        while nextPageToken:
            nextPage = self.service.files().list(pageSize=10,
                                            fields="nextPageToken, files(id, name, mimeType, parents, createdTime)",
                                            pageToken=nextPageToken).execute()
            nextPageToken = nextPage.get('nextPageToken')
            results['files'] = results['files'] + nextPage['files']

        res_list = results.get('files')
        return res_list

    def create_directory_google_drive(self, name):
        """
        Метод создания папки на Google.Drive.

        Parameters
        ----------
        name: str
            имя создаваемой папки.

        Результатом работы функции является создание новой директории на Google.Drive.

        Ссылка на официальную документацию: https://developers.google.com/drive/api/v3/folder

        """

        file_metadata = {
            'name': name,
            'mimeType': 'application/vnd.google-apps.folder'
        }
        file = self.service.files().create(body=file_metadata,
                                      fields='id').execute()

        print()
        print('Создание папки прошло успешно')
        print()
        print('Идентификатор папки: %s' % file.get('id'))

    def download_files_google_drive(self, folder_id, list_name):
        """
        Метод загрузки файлов на Google.Drive.

        Parameters
        ----------
        folder_id: str
            идентификатор папки

        list_name: list
            список с информацией о загружаемых файлах.

        Exceptions
        ----------
        googleapiclient.errors.HttpError - HTTP data was invalid or unexpected

        Результатом работы функции является загрузка файлов на Google.Drive.

        Ссылка на официальную документацию: https://developers.google.com/drive/api/v3/manage-uploads

        """

        try:
            print()
            for info in tqdm(list_name, desc='Идёт загрузка файлов на Google.Drive, пожалуйста, подождите ...', unit='S'):
                time.sleep(1)
                response = requests.get(info['url'])

                if response.status_code >= 200 and response.status_code < 300:
                    file_content = io.BytesIO(response.content)
                    file_metadata = {'name': f"{info['file_name']}", 'parents': [folder_id]}
                    media = MediaIoBaseUpload(file_content, mimetype='image/jpeg')
                    self.service.files().create(body=file_metadata, media_body=media, fields='id').execute()

            print()
            print('Данные успешно загружены.')

        except googleapiclient.errors.HttpError as error:
            print(f"\nРабота метода была прервана ошибкой.\n"
                  f"Происходит обработка данных об ошибке, пожалуйста, подождите...\n"
                  f"{error}"
                  f"Программа продолжает работу в штатном режиме.\n"
                  f"Вам необходимо снова получить информацию о фотографиях пользователя (пользователей) Вконтакте и повторить попытку.")

    def delete_files_google_drive(self, fileId):
        """
        Метод удаления файлов на Google.Drive.

        Parameters
        ----------
        fileId: str
            идентификатор файла.

        Результатом работы функции является удаление файла на Google.Drive.

        Ссылка на официальную документацию: https://developers.google.com/drive/api/v3/reference/files/delete

        """

        self.service.files().delete(fileId=fileId).execute()