import json
from os import mkdir, path
from shutil import rmtree
from urllib.error import HTTPError

from requests import get


def download_latest():
    try:
        if path.exists(".cache") == True:
            rmtree(".cache")
        elif path.exists(".cache") == False:
            mkdir(".cache")
        try:
            req = get(
                "https://api.github.com/repos/Atmosphere-NX/Atmosphere/releases"
            ).json()

        except HTTPError:
            print(HTTPError)

        rmtree(".cache")
    except Exception as err:
        print(err)
