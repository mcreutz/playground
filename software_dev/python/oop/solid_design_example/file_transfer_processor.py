from file_transfer_client import FileTransferClient


class FileTransferProcessor():
    def exchange(self, client: FileTransferClient, to_upload: bytes, to_download: str) -> bytes:
        client.upload(to_upload)
        return client.download(to_download)
