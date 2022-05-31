from download import VKDownload
from upload import YAUpload

vk_id = "552934290"

if __name__ == "__main__":
    download = VKDownload(vk_id)
    print(download.token)
    download.get_photo_list()
    download.get_download_tools()
    download.log()
    upload = YAUpload()
    upload.get_headers()
    upload.get_folder_params()
    upload.ya_folder()
    upload.ya_upload(download.download_tools)