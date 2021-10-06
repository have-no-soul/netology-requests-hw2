import requests

main_api_url = 'https://cloud-api.yandex.net'
upload_endpoint = '/v1/disk/resources/upload'

path_to_file = 'files-to-upload/BumazhnySamoletik.gif'

TOKEN = ''


class YaUploader:
    def __init__(self, token):
        self.token = token

    def upload(self, path_to_file):
        file_name = path_to_file.split('/')[-1]

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
        params = {'path': file_name, 'overwrite': 'true'}

        get_upload_url = main_api_url + upload_endpoint

        response_url = requests.get(url=get_upload_url, headers=headers, params=params)

        href = response_url.json().get('href')
        response = requests.put(url=href, data=path_to_file)
        response.raise_for_status()
        if response.status_code == 201:
            print("Upload Success!")


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    token = TOKEN
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
