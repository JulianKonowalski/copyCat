import os
from getArgs import getArgs
from copyFiles import copyFiles

def main():
    directory, destination = getArgs()
    if os.path.exists(directory):
        copyFiles(directory, destination)