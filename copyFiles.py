import os

BUFFERSIZE = 1024

def __makeDir__(dir):
    while True:
        try:
            os.mkdir(dir)
            break
        except FileNotFoundError:
            parentDir = os.path.join(dir, os.pardir)
            __makeDir__(parentDir)

def __copyFile__(filePath, destination):
    filename = os.path.basename(filePath)
    rfile = open(filePath, 'rb')
    wfile = open(os.path.join(destination, filename), 'wb')
    buffer = rfile.read(BUFFERSIZE)
    while buffer:
        wfile.write(buffer)
        buffer = rfile.read(BUFFERSIZE)
    rfile.close()
    wfile.close()

def copyFiles(directory, destination):
    if not os.path.exists(destination):
        __makeDir__(destination)
    for path in os.listdir(directory):
        fullPath = os.path.join(directory, path)
        if os.path.isdir(fullPath):
            subDestination = os.path.join(destination, path)
            os.mkdir(subDestination)
            copyFiles(fullPath, subDestination)
            continue
        __copyFile__(fullPath, destination)