import os
from datetime import date
from os.path import basename
from zipfile import ZipFile


def zip_packer():
    with ZipFile("out/Spacker-{}.zip".format(date.today()), "w") as zipObj:
        for folderName, filenames in os.walk(".cache"):
            for filename in filenames:
                filePath = os.path.join(folderName, filename)
                zipObj.write(filePath, basename(filePath))
