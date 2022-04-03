from requests import get

from utils.fetch import download_latest
from utils.zip import zip_packer

if __name__ == "__main__":
    download_latest()
    zip_packer()
    