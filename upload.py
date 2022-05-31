import requests
import os
from tqdm import tqdm


class YAUpload:
    def __init__(self, token: str, version):
        self.path = os.getcwd()
        self.version = version
        self.host = f'https://cloud-api.yandex.net:443/{self.version}/disk/resources'
        self.token = token
        self.headers = None
        self.folder_link = None
        self.params = None

    def get_headers(self):
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def get_params(self):
        self.params = {
            'overwrite': True,
            'path': 'Photo'
        }

    def ya_folder(self):
        url = self.host
        search = requests.get(url, headers=self.headers, params=self.params)
        if search.status_code == 404:
            requests.put(url, headers=self.headers, params=self.params)

        else:
            pass

    def ya_upload(self):
        pass
