import requests
import os
import datetime
import json
import configparser


class VKDownload:

    def __init__(self):
        config = configparser.ConfigParser()
        config.read("settings.ini")
        self.token = config["VK"]["token"]
        self.version = config["VK"]["version"]
        self.host = "https://api.vk.com/method/"
        self.id = None
        self.download_tools = None
        self.json = None
        self.screen_name = None
        self.photo_count = None

    def get_id(self):
        self.id = str(input("Enter your nickname or ID: "))
        if self.id.isdigit():
            url = f'{self.host}users.get'
            response = requests.get(url, params={"access_token": self.token, "v": self.version,
                                                 'user_ids': self.id})
            if not response.json()['response']:
                print('Wrong ID! Try again')
                self.get_id()
        else:
            url = f'{self.host}utils.resolveScreenName'
            response = requests.get(url, params={"access_token": self.token, "v": self.version,
                                                 "screen_name": self.id})
            if not response.json()['response']:
                print('Wrong nickname! Try again')
                self.get_id()
            else:
                self.id = response.json()['response']['object_id']

    def get_photo_count(self):
        self.photo_count = str(input("Enter how many photos you wish to upload: "))
        if self.photo_count.isdigit():
            pass
        else:
            print('Use only digits!')
            self.get_photo_count()

    def get_params(self):
        return {
            "access_token": self.token,
            "v": self.version,
            "owner_id": self.id,
            "album_id": "profile",
            "rev": "1",
            "photo_sizes": "1",
            "extended": "1",
            "count": self.photo_count
        }

    def get_photo_list(self):
        url = f"{self.host}photos.get"
        params = self.get_params()
        response = requests.get(url, params=params).json()
        self.json = response

    def get_download_tools(self):
        download_tools = {}
        for item in self.json["response"]["items"]:
            name = str(item["likes"]["count"])
            date = str(datetime.datetime.fromtimestamp(item["date"]).strftime("%B %d, %Y %I_%M_%S"))
            largest_type = ""
            url = ""
            pixels = 0
            for size in item["sizes"]:
                multiply = int(size["height"]) * int(size["width"])
                if multiply > pixels:
                    pixels = multiply
                    largest_type = size["type"]
                    url = size["url"]
            if name in download_tools.keys():
                download_tools[name + " " + date] = [url, largest_type]
            else:
                download_tools[name] = [url, largest_type]
        self.download_tools = download_tools

    def log(self):
        log = []
        for key, value in self.download_tools.items():
            session = {"file_name": key + ".jpg", "size": value[1]}
            log.append(session)
        path = os.getcwd()
        with open(path + "\\" + "log.json", "w") as here:
            json.dump(log, here, indent=1)
