#!/usr/bin/env python2.7

from datetime import datetime

t = datetime.strptime('30/03/09 16:31:32.123', '%d/%m/%y %H:%M:%S.%f')
n = datetime.now()
#print n-t

import os, os.path

#print os.walk.__doc__
import os,re
from os.path import join, getsize

extensions = ['AVI',
              'avi',
              'ogv',
              'OGV',
              'mp4',
              'MP4',
              'DAT',
              'dat',
              'MKV',
              'mkv',
              'vob',
              'VOB',
              '3gp',
              '3GP',
              'mov',
              'MOV']
list = []

path="/media/My\ Disc"
for files in os.listdir(path):
    # print files
    filepath = os.path.join(path, files) # join paths with file
    extn = os.path.splitext(files)[1].strip('.') # strip file extn
    # print extn
    # extract only files and match known extensions
    if os.path.isfile(filepath) and extn in extensions:
        list.append(filepath)

for l in list:
    print l


#    else:
#        print "error"


    
    
 

            

""""
if os.path.isfile(filepath) and extn in extentions:
print os.path.abspath(filepath)

print os.path.join('/home/sachin/Videos/',files)

os.path.isfile(filepath) and ext 

for files in os.listdir('.'):
    list.append(files.strip())
print list

------------


   print sum([getsize(join(root, name)) for name in files]),
    print "bytes in", len(files), "non-directory files"
    if 'CVS' in dirs:
        dirs.remove('CVS')  # don't visit CVS directories

        fullpath = os.path.join(root, f)
        if os.path.getsize(fullpath) < 200 * 1024:
            os.remove(fullpath)
            
"""""
