import os

BUFFERSIZE = 1024

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
    for path in os.listdir(directory):
        fullPath = os.path.join(directory, path)
        if os.path.isdir(fullPath):
            continue
        __copyFile__(fullPath, destination)