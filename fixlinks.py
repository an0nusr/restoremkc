from pathlib import Path
import re
from typing import Generator, List

SERVER_ROOT = "/"

def processFiles(files: Generator[Path, None, None]):
    for f in files:
        print(f"Reading file: {f}")
        html = f.read_text()

        #print("Old links:")
        #for i in findLinks(html): print(i)

        html = fixLinkCase(html)
        html = fixQuotes(html)
        html = fixIndexLinks(html)
        html = makeRelativeLinks(html)

        #print("New links:")
        #for i in findLinks(html): print(i)

        #Path("test.html").write_text(html)
        f.write_text(html)

def fixLinkCase(html: str):
    html = re.sub(r" HREF=", r" href=", html)
    html = re.sub(r" BACKGROUND=", r" background=", html)
    return re.sub(r" SRC=", r" src=", html)

def findLinks(html: str):
    return re.findall(r"(src|href|background)=(\"?[^ >\"]+\"?)", html, re.IGNORECASE)

def fixQuotes(html: str):
    # fix links that don't have quote marks
    return re.sub(r"(src|href|background)=([^ >\"]+)", r'\1="\2"', html)

def fixIndexLinks(html: str):
    # don't link to index.html pages, as it breaks relative page links.
    # instead link to the folder - the browser will keep the link and the trailing slash
    # will fix the relative link issue.
    return re.sub(r"(href)=(.*?)/index\.html", r"href=\2/", html)

def makeRelativeLinks(html: str):
    # don't use mkcblacknet.org - use the server root
    replace_str = r'\1="' + SERVER_ROOT + r'\3"'
    
    # fix links and images
    return re.sub(r"(src|href|background)=\"(.*?)mkcblacknet\.org/(.*?)\"", replace_str, html)

def main():
    files = Path(".").glob("**/*.html")
    processFiles(files)

if __name__ == '__main__':
    main()