from bs4 import BeautifulSoup
from cli_args_system import Args
import requests
import wget
import os
import sys


mediaTypes = []
args = Args()
list_of_flags = args.args()
for flag in list_of_flags:
    if flag == "--images" or "-img":
        mediaTypes.append("img")
    if flag == "--videos" or "-video":
        mediaTypes.append("video")
if len(mediaTypes) == 0:
    mediaTypes.append("img")
    mediaTypes.append("video")
mediaTypes = list(set(mediaTypes))

urls = []

try:
    file = open('input.txt', 'r')
    for line in file.readlines():
        formattedLine = line.strip().lstrip().rstrip()
        if len(formattedLine) != 0:
            urls.append(formattedLine)
except:
    sys.exit("\n Error reading input.txt")


if len(urls) != 0:
    for url in urls:
        page = requests.get(url)

        soup = BeautifulSoup(page.text, "html.parser")
        allMedia = soup.findAll(mediaTypes)

        if len(allMedia) == 0:
            print("\n There is no media in " + url)
            continue

        try:
            sourceLinks = []

            for media in allMedia:
                link = "https://telegra.ph" + media["src"]
                sourceLinks.append(link)

            parentDir = os.path.join(os.getcwd(), "downloads")
            folderName = url.split("telegra.ph/")[-1]
            folderDir = os.path.join(parentDir, folderName)

            if not os.path.exists(folderDir):
                os.makedirs(folderDir)

            for link in sourceLinks:
                file_name = wget.download(link, folderDir)

            print("\n Sucessfully downloaded all media of " + url)

        except:
            print("\n wget failed to download")

    sys.exit("\n The program downloaded everything that could be possible")

else:
    sys.exit("\n The list of urls is empty")
