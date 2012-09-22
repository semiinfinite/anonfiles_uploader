import os

for dirname, dirnames, filenames in os.walk('roms'):
#    for subdirname in dirnames:
#        print os.path.join(dirname, subdirname)
    for filename in filenames:
        print os.path.join(dirname, filename)
