import argparse
import os

def getArgs():
    parser = argparse.ArgumentParser(
        prog='copyCat',
        description='copying files from a folder to a new destination'
    )
    parser.add_argument('directory')
    parser.add_argument('destination')
    args = parser.parse_args()
    directory = os.path.abspath(args.directory)
    destination = os.path.abspath(args.destination)
    return (directory, destination)