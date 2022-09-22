from typing import List
from file_transfer_client import FileTransferClient
from bulk_file_transfer_client import BulkFileTransferClient
# import FTPSDriver


class SFTPClient(FileTransferClient, BulkFileTransferClient):
    def __init__(self, host, port, username, password):
        self._client = FTPSDriver(host, port, user=username, password=password)

    def upload(self, file: bytes):
        self._client.upload(file)

    def download(self, target: str) -> bytes:
        return self._client.download(target)

    def upload_bulk(self, files: List[bytes]):
        for file in files:
            self.upload(file)

    def download_bulk(self, targets: List[str]) -> List[bytes]:
        files = []
        for target in targets:
            files.append(self.download(target))
        return files
