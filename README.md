# Anonfiles Uploader #
## Overview: ##
File uploader that takes a directory as an argument, and uploads all zip files in the subdirectories to anonfiles.com

## Prerequisites: ##
`pip install -r requirements.txt`

## Usage: ##
`python anonupload.py dir_to_upload`

## Uploader Output: ##
When you first run anonupload.py a new file is created named newlyUploadedFiles.csv. This fill will include all the files in the directory you selected that have been uploaded to anonfiles.com

The lines in newlyUploadedFiles.csv will be appended to previouslyUploadedFiles.csv. This file will be used to check if the files have been uploaded before. If the file was previously uploaded, the link for that file on anonfiles.com is checked to make sure that it is still alive and available for download. If the link is not alive then it is flagged to be reuploaded.

## TODO: ##
- Move from standard CSV output to SQLite
- Optimize link removal on bad links

## LICENSE ##

Copyright (c) 2012, Michael Mitchell  
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

Redistributions of source code must retain the above copyright notice,
this list of conditions and the following disclaimer.
Redistributions in binary form must reproduce the above copyright
notice, this list of conditions and the following disclaimer in the
documentation and/or other materials provided with the distribution.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED
TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
