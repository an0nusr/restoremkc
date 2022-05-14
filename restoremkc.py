from urllib.request import urlopen, urlretrieve
from pathlib import Path
from zipfile import ZipFile
import re
from fixlinks import processFiles


BASE_URL = "https://web.archive.org/web/20050206222836/"
_ARCHIVE_URL = "https://web.archive.org/web/20050206222836/http://swatkats.org/download/index.html"


LINKS = [
  ("http://swatkats.org/download/BlackNetZIP-index-main.zip", "BlackNetZIP-index-main.zip"),
  ("http://swatkats.org/download/BlackNetZIP-images.zip", "BlackNetZIP-images.zip"),
  ("http://swatkats.org/download/BlackNetZIP-index-clean.zip", "BlackNetZIP-index-clean.zip"),
  ("http://swatkats.org/download/BlackNetZIP-index-adult.zip", "BlackNetZIP-index-adult.zip"),
  ("http://swatkats.org/download/BlackNetZIP-index-complete.zip", "BlackNetZIP-index-complete.zip"),
  ("http://swatkats.org/download/BlackNetZIP-S00.zip", "BlackNetZIP-S00.zip"),
  ("http://swatkats.org/download/BlackNetZIP-S01.zip", "BlackNetZIP-S01.zip"),
  ("http://swatkats.org/download/BlackNetZIP-S02.zip", "BlackNetZIP-S02.zip"),
  ("http://swatkats.org/download/BlackNetZIP-S03.zip", "BlackNetZIP-S03.zip"),
  ("http://swatkats.org/download/BlackNetZIP-S04.zip", "BlackNetZIP-S04.zip"),
  ("http://swatkats.org/download/BlackNetZIP-S05.zip", "BlackNetZIP-S05.zip"),
  ("http://swatkats.org/download/BlackNetZIP-S06.zip", "BlackNetZIP-S06.zip")
]

def downloadArchive(downloadPath = "./zips"):
    Path(downloadPath).mkdir(exist_ok=True)

    for link, file in LINKS:
        print(f"Downloading {file}")

        # this is a two-step process. We have to open the link from archive.org,
        # then grab the src of the iframe on the next page.
        archiveHtml = urlopen(BASE_URL + link).read().decode('utf-8')

        # parse the iframe from the response
        m = re.search(r'<iframe id="playback" src="(.*?.zip)"', archiveHtml)
        archiveLink = m.group(1) #type:ignore

        urlretrieve(archiveLink, Path(downloadPath) / file)


def unzipArchive(downloadPath = "./zips", target = "./mkcblacknet"):
    targetPath = Path(target)
    targetPath.mkdir(exist_ok=True)

    zipPaths = Path(downloadPath).glob("*.zip")
    for zipPath in zipPaths:
        print(f"Unzipping file {zipPath} into {targetPath}")
        with ZipFile(zipPath) as zip:
            zip.extractall(targetPath)

def fixLinks(target = "./mkcblacknet"):
    targetPath = Path(target)
    htmlFiles = targetPath.glob("**/*.html")
    processFiles(htmlFiles)

def main():
    ZIP_TMP_DIR = "zips"
    TARGET_DIR = "mkcblacknet"

    print("Downloading MKC Blacknet archives from Archive.org...\n")
    
    downloadArchive(ZIP_TMP_DIR)

    print(f"\nExtracting downloaded files to {TARGET_DIR}\n")

    unzipArchive(ZIP_TMP_DIR, TARGET_DIR)

    print(f"\nFixing links so the archive can be used locally...\n")
    fixLinks(TARGET_DIR)

    print("\n\nWork complete - you should now be able to browse MKCBlacknet on your machine!\n")
    print(f"Type 'cd {TARGET_DIR}' in your terminal to switch to the download directory, then")
    print(f"run 'python -m http.server' to run a local web server to browse it!")

if __name__ == '__main__':
    main()

