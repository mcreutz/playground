from file_transfer_client import FileTransferClient
# import FTPDriver


class S3Client(FileTransferClient):
    def __init__(self, host, port):
        self._client = FTPDriver(host, port)

    def upload(self, file: bytes):
        self._client.upload(file)

    def download(self, target: str) -> bytes:
        return self._client.download(target)
