from pip._vendor import requests

from pprint import pprint

class YaUploader:
    def __init__(self, token: str):
        self.token = token
    
    def get_headers(self):
        return {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}

    def _get_upload_link(self, disk_file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload(self, file_path: str):
        response_link = self._get_upload_link(file_path)
        href = response_link.get("href", "")
        response = requests.put(href, data=open(file_path, 'rb'))


if __name__ == '__main__':
    path_to_file = 'task_2.2.txt'
    token = 
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)