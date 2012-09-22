# Anonfiles Uploader #
## Overview ##
File uploader that takes a directory as an argument, and uploads all zip files in the subdirectories to anonfiles.com

## Usage ##
`python anonupload.py dir_to_upload`

## Uploader Output ##
When you first run anonupload.py a new file is created named newlyUploadedFiles.csv. This fill will include all the files in the directory you selected that have been uploaded to anonfiles.com

The lines in newlyUploadedFiles.csv will be appended to previouslyUploadedFiles.csv. This file will be used to check if the files have been uploaded before. If the file was previously uploaded, the link for that file on anonfiles.com is checked to make sure that it is still alive and available for download. If the link is not alive then it is flagged to be reuploaded.