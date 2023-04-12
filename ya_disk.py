import requests


class Yandex_Disk:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        """Метод создания заголовка"""

        return {
            "Content-Type": "application/json",
            "Authorization": f"OAuth {self.token}",
        }

    def get_file_list(self):
        """Метод получения списка файлов"""

        files_url = "https://cloud-api.yandex.net/v1/disk/resources/files"

        headers = self.get_headers()

        response = requests.get(url=files_url, headers=headers)

        return response.json()

    def _get_upload_link(self, disk_file_path):
        """Метод запроса у яндекса ссылки для выгрузки"""

        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"

        headers = self.get_headers()

        params = {"path": disk_file_path, "overwrite": "true"}

        response = requests.get(url=upload_url, headers=headers, params=params)

        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename=None):
        """Метод выгрузки на яндекс диск"""

        data = self._get_upload_link(disk_file_path=disk_file_path)
        file_url = data.get("href")
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = self.get_headers()
        if filename:
            response = requests.put(file_url, data=open(filename, "rb"))
        else:
            response = requests.put(
                url=url, headers=headers, params={"path": disk_file_path}
            )
        if response.status_code == 201:
            print("Success")
