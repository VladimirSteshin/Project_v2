from download import VKDownload
from upload import YAUpload

vk_token = ""
vk_version = "5.131"
vk_id = "552934290"

ya_token = ''
ya_version = 'v1'

if __name__ == "__main__":
    download = VKDownload(vk_token, vk_version, vk_id)
    download.get_photo_list()
    download.get_download_tools()
    download.log()
    upload = YAUpload(ya_token, ya_version)
    upload.get_headers()
    upload.get_folder_params()
    upload.ya_folder()
    upload.ya_upload(download.download_tools)
