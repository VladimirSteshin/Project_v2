from download import VKDownload
from upload import YAUpload

vk_id = input("Enter your nickname or ID: ")
photo_count = str(input("Enter how much photos you wish to upload: "))

if __name__ == "__main__":
    download = VKDownload(vk_id, photo_count)
    download.get_photo_list()
    download.get_download_tools()
    download.log()
    upload = YAUpload()
    upload.get_headers()
    upload.get_folder_params()
    upload.ya_folder()
    upload.ya_upload(download.download_tools)
