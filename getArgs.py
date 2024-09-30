import argparse

def getArgs():
    parser = argparse.ArgumentParser(
        prog='copyCat',
        description='copying files from a folder to a new destination'
    )
    parser.add_argument('directory')
    parser.add_argument('destination')
    args = parser.parse_args()
    return (args.directory, args.destination)