#!/usr/bin/python

import requests
import sys, os
import hashlib

def uploadFile(fileToUpload):
    """Function will upload files passed as paramter to anonfiles.com"""
    url = 'https://anonfiles.com/api?plain'
    f = open('%s' % fileToUpload, 'rb')
    files = {'file': ('%s' % fileToUpload, f)}

    r = requests.post(url, files = files)
    f.close()
    return r.text

def getmd5(filePath, block_size = 8192):
    """Takes file path and does an incremental md5 of the file"""
    md5 = hashlib.md5()
    f = open(filePath)
    while True:
        data = f.read(block_size)
        if not data:
            break
        md5.update(data)
    return md5.hexdigest()

def deleteBadLink(badLine):
    """Deletes bad link from previousUploadedFiles.csv"""
    lines = open('previouslyUploadedFiles.csv').readlines()
    f = open('previouslyUploadedFiles.csv', 'w')
    for line in lines:
        if line != badLine:
            f.write(line)
    f.close()


def filePreviouslyUploaded(filePath, fileHash):
    """Checks if the file has been uploaded before"""
    for line in open(filePath):
        if fileHash in line:
            if linkAlive(line.split(',')[1]):
                return True
            else:
                deleteBadLink(line)
                return False
        return True
    return False

def linkAlive(link):
    """Gets previously uploaded files and verifies that the link is still aliveself."""
    r = requests.get(link)
    if link in r.text:
        return True
    return False

def startProcess():
    """
    Reads first command line argument with folder location with files to upload
    and uploads them to anonfiles. Checks to make sure files have not previously
    been uploaded before trying to upload. This will conserve bandwidth, but
    will require more cpu as the file has to be hashed to check previously uploaded
    data files.
    """
    filesToUpload = []
    for dirname, dirnames, filenames in os.walk(sys.argv[1]):
        for filename in filenames:
            if os.path.splitext(filename)[1] == ".zip":
                filesToUpload.append(os.path.join(dirname, filename))

    outputFile = open('newlyUploadedFiles.csv', 'w')
    for fileToUpload in filesToUpload:
        fileToUploadHash = getmd5(fileToUpload)
        if os.path.exists('previouslyUploadedFiles.csv'):
            if not filePreviouslyUploaded('previouslyUploadedFiles.csv', fileToUploadHash):
                outputFile.write(fileToUpload + "," + uploadFile(fileToUpload) + "," + fileToUploadHash + "\n")
                print "%s uploaded!" % fileToUpload
            else:
                print "%s previously uploaded. Skipped! MD5: %s" % (fileToUpload, fileToUploadHash)
        else:
            outputFile.write(fileToUpload + "," + uploadFile(fileToUpload) + "," + fileToUploadHash + "\n")
            print "%s uploaded!" % fileToUpload
    outputFile.close()

    oldFile = open('previouslyUploadedFiles.csv', 'a')
    newFile = open('newlyUploadedFiles.csv', 'r')
    oldFile.write(newFile.read())
    newFile.close()
    oldFile.close()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        startProcess()
    else:
        print "Usage: python anonfiles.py dir_to_upload"
