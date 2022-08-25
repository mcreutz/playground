"""
Implemented the example from:
https://dev.to/ezzy1337/a-pythonic-guide-to-solid-design-principles-4c8i
"""

from ftp_client import FTPClient
from ftps_client import FTPSClient
from sftp_client import SFTPClient
from s3_client import S3Client
from scp_client import SCPClient
from file_transfer_processor import FileTransferProcessor

if __name__ == '__main__':
    ftp = FTPClient('ftp.host.com', 8800)
    sftp = FTPSClient('sftp.host.com', 22, 'ftps_user', 'P@ssw0rd1!')
    ftps = SFTPClient('ftps.host.com', 990, 'ftps_user', 'P@ssw0rd1!')
    s3 = S3Client('ftp.host.com', 8800)
    scp = SCPClient('ftp.host.com', 8800)

    transferrer = FileTransferProcessor()
    for client in [ftp, sftp, ftps, s3, scp]:
        transferrer.exchange(client, b'Hello', 'greeting.txt')
