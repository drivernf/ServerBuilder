import zipfile
import os.path
import pysftp as sftp
import tkinter as tk
from tkinter import filedialog, Text
import GUI

pathToZip = '/'

def main():
    GUI.guiSetup(pathToZip)

# Changes folder of local directory
def changeFolder():
    global pathToZip
    pathToZip = filedialog.askdirectory() + '/'
    GUI.pathToZipTK.set('Local Folder: {}'.format(pathToZip))

# Zips local directory
def zipFolder():
    zf = zipfile.ZipFile(os.path.dirname(os.path.realpath(__file__)) + "/" + os.path.basename(os.path.normpath(pathToZip)) + ".zip", "w")
    for root, dirs, files in os.walk(pathToZip):
        for file in files:
            zf.write(os.path.join(root, file), os.path.join(root[len(pathToZip):], file))

# Transfers local directory to server
def upload():
    try:
        cnopts = sftp.CnOpts()
        cnopts.hostkeys = None
        s = sftp.Connection(host='96.30.199.232', username='root', password='', cnopts=cnopts)
        remotePath = '/root/GameServer/w.zip'
        localPath = 'w.zip'
        print('Removing old build...')
        s.execute('cd ~/GameServer/ && chmod +x delete.sh && ./delete.sh')
        print('Transferring zip...')
        s.put(localPath, remotePath)
        print('Unpacking and executing...')
        print('Done!')
        #s.execute('cd ~/GameServer/ && chmod +x unpack.sh && ./unpack.sh')
        s.close()

    except:
        print ('Upload failed')

if __name__ == '__main__':
    main()