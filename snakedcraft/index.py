# REEEEEEEEE
import os
import time
import wget
import touch
root = os.path.dirname(os.path.realpath(__file__))
cache = os.path.dirname(os.path.realpath(__file__)) + '\cache'
jars = cache + '\jars'
conf = cache + '\conf'
utils = root + '\\utils'\

# Self updating!
import urllib.request

path = os.path.dirname(__file__)

with urllib.request.urlopen("https://example.com/latest.zip") as upd:
    with open(path, "wb+") as f:
        f.write(upd.read())

# Set up for downloads
from pathlib import Path

path_to_file = '.made'
path = Path('.made')

if path.is_file():
    pass
else:
    print('Setting up!')
    os.chdir(root)
    os.mkdir('./utils')
    touch.touch(".made")
    minecraft_dir = "./craft"
    os.mkdir(minecraft_dir)
    os.mkdir('./cache')
    os.chdir(cache)
    os.mkdir('./jars')
    os.mkdir('./conf')
    os.chdir(conf)
    os.mkdir('purpur-16-5')
    print('Downloading Server')
    os.chdir(jars)
    wget.download(url="https://ghcdn.rawgit.org/mcfan4256/cdn1/main/snakedcraft/craft/purpur-16-5.jar")
    print("")
    print('Done!')
    os.chdir(root)
    print("")
    print('Downloading Configs!')
    os.chdir(conf + '\purpur-16-5')
    wget.download(url='https://ghcdn.rawgit.org/mcfan4256/cdn1/main/snakedcraft/conf/bukkit.yml')
    print("")
    wget.download(url='https://ghcdn.rawgit.org/mcfan4256/cdn1/main/snakedcraft/conf/paper.yml')
    print("")
    wget.download(url='https://ghcdn.rawgit.org/mcfan4256/cdn1/main/snakedcraft/conf/purpur.yml')
    print("")
    wget.download(url='https://ghcdn.rawgit.org/mcfan4256/cdn1/main/snakedcraft/conf/server.properties')
    print("")
    wget.download(url='https://ghcdn.rawgit.org/mcfan4256/cdn1/main/snakedcraft/conf/spigot.yml')
    print("")
    wget.download(url='https://ghcdn.rawgit.org/mcfan4256/cdn1/main/snakedcraft/conf/tuinity.yml')
    print("")
    print('Done!')
    print('')
    os.chdir(utils)
    print('Downloading Utilities!')
    print('')
    wget.download(url='https://ghcdn.rawgit.org/mcfan4256/cdn1/main/snakedcraft/utils/portforward.jar')
    print('')
    print('Done!')
    os.chdir(root)
