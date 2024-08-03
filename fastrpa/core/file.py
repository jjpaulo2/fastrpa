import os

from mimetypes import guess_extension
from requests import Response
from tempfile import mkstemp

from fastrpa.types import WebDriver
from fastrpa.utils import get_session


class File:
    def __init__(self, webdriver: WebDriver) -> None:
        self.webdriver = webdriver

    def get_extension(self, response: Response) -> str:
        content_type = response.headers['Content-Type']
        mime_type, *_ = content_type.split(';')
        if extension := guess_extension(mime_type):
            return extension
        raise ValueError('The response does not have a Content-Type header!')

    def get_hash(self, response: Response) -> str:
        return str(abs(hash(response.content)))

    def download_file(self, url: str, path: str | None = None) -> str:
        response = get_session(self.webdriver).get(url)
        file_suffix = self.get_hash(response) + self.get_extension(response)

        if path is None:
            _, path = mkstemp(file_suffix)

        elif '.' not in path:
            path = os.path.join(path, file_suffix)

        with open(path, 'wb') as file:
            file.write(response.content)

        return path

    def download_file_to_cwd(self, url: str) -> str:
        return self.download_file(url, os.getcwd())

    def get_path(self, path: str) -> str:
        if os.path.isfile(path):
            return path
        return self.download_file(path)
