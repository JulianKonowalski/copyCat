import os
from getArgs import getArgs
from copyFiles import copyFiles

def main():
    directory, destination = getArgs()
    if not os.path.exists(directory):
        print('No such base directory')
        return
    copyFiles(directory, destination)