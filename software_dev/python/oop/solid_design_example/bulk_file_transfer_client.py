from abc import ABC
from typing import List


class BulkFileTransferClient(ABC):
    def upload_bulk(self, files: List[bytes]):
        raise NotImplementedError

    def download_bulk(self, targets: List[str]) -> List[bytes]:
        raise NotImplementedError
