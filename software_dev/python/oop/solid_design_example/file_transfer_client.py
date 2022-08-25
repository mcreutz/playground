from abc import ABC


class FileTransferClient(ABC):
    def upload(self, file: bytes):
        raise NotImplementedError

    def download(self, target: str) -> bytes:
        raise NotImplementedError

    # def cd(self, target_dir):
    #     raise NotImplementedError
