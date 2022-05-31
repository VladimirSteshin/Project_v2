import requests
from tqdm import tqdm


class YAUpload:
    def __init__(self, token: str, version):
        self.version = version
        self.host = f'https://cloud-api.yandex.net:443/{self.version}/disk/resources'
        self.token = token
        self.path = 'Photo'
        self.headers = None
        self.folder_link = None
        self.folder_params = None

    def get_headers(self):
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def get_folder_params(self):
        self.folder_params = {
            'overwrite': True,
            'path': 'Photo'
        }

    def ya_folder(self):
        url = self.host
        search = requests.get(url, headers=self.headers, params=self.folder_params)
        if search.status_code == 404:
            requests.put(url, headers=self.headers, params=self.folder_params)
        else:
            pass

    def ya_upload(self, links):
        url = f'{self.host}/upload'
        for key, value in tqdm(links.items()):
            requests.post(url, headers=self.headers, params={'path': f'Photo/{key}', 'url': value[0]})
        print('Photos uploaded')
