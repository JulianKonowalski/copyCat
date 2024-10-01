import os
from getArgs import getArgs
from copyFiles import copyFiles

def __start__(directory, destination):
    print('Copying files...')
    copyFiles(directory, destination)
    print('Done!')

def main():
    directory, destination = getArgs()
    if not os.path.exists(directory):
        print('No such base directory')
        return
    __start__(directory, destination)
    return