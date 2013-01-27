#!/usr/bin/env python2.7

from sys import argv
import subprocess, os, re, time
from subprocess import Popen, PIPE
from os.path import join, getsize

from conf import vals

class Metadata(object):         # inherite from object class(I think its convention :P)
   """
   Extracts metadata from input *video* file.
   Takes only one argument: filename.

   Returns: duration(HH:MM:SS.mSec), fps, resolution[width,height],
   bitrate(Kb/s), and frequency(Hz) 
   """  

   RE_ERROR = 1                   # regExp error

   def __init__(self,filename):
      """construtor.takes input as as argument."""      
      p = subprocess.Popen(['avconv','-i', filename,'-f','metadata'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
      output, error = p.communicate()#[0]
      try:
         # avconv returns info as error msg
         lines = error.splitlines()
         if lines:
            self.lines=lines            
         else:
            print "variable line is EMPTY"
      except:
         print "enable to read variable: error"

   def duration(self):
      """returns duration in: HH:MM:SS.mili-Sec"""
      for line in self.lines:
         try:
            duration = re.search(r'Duration.*?,',line)
            if duration:
               t = re.search(r'\d\d:\d\d:\d\d.\d\d',duration.group())
               return time.strptime(t.group(),"%H:%M:%S.%f")   # HH:MM:SS.milliseconds
         except:
            return RE_ERROR
         
   def fps(self):
      """returns fps in frames/sec"""
      for line in self.lines:
         try:
            frame_per_sec = re.search(r'\d fps',line)
            if frame_per_sec:
               return int(frame_per_sec.group().split()[0])
         except:
            return RE_ERROR

   def resolution(self):
      """returns height[0], width[1] in px"""
      for line in self.lines:
         try:
            resolution = re.search(r'\d\d\d?x\d\d\d*',line)
            if resolution:
               width = resolution.group().split("x")[0]
               height = resolution.group().split("x")[1]
               return int(width),int(height)
         except:
            return RE_ERROR
         
   def frequency(self):
      """returns frequency in Hz"""
      for line in self.lines:
         try:
            freq = re.search(r'\d* Hz',line)
            if freq:
               return int(freq.group().split()[0])
         except:
            return RE_ERROR

   def bitrate(self):
      """returns bitrate in Kb/s"""
      for line in self.lines:
         try:
            bitrate = re.search(r'bitrate: \d*',line)
            if bitrate:
               return int(bitrate.group().split()[1]) # 1st element of split(), 0th element is string
         except:
            return RE_ERROR

class MetaVideo(Metadata):
   """inherit Metadata to use for video"""
   def __init__(self,filename):
      """access __init__ method of Metadata class"""
      super(MetaVideo, self).__init__(filename)
      """access RE_ERROR attrib of Metadata class"""
      super(MetaVideo, self).RE_ERROR
      #filename = filename
      
      """
      class DerivedClass(Base):
          def some_method(self):
              super(DerivedClass, self).meth()
      """

def validate():
   """test value w.r.t to values provided in conf.py"""
   if dict['Duration'] > vals.duration:
      print "ERROR: duration"
   else:
      print "OK: duration"
   
   if int(dict['Frame/sec']) > vals.fps:
      print "ERROR: fps"
   else:
      print "OK: fps"

   if int(dict['BitRate']) > vals.bitrate:
      print "ERROR: bitrate"
   else:
      print "OK: bitrate"
      
   if int(dict['Freq']) > vals.freq:
      print "ERROR: freq"
   else:
      print "OK: freq"

   # print dict['Width'],dict['Height']
   # print vals.width, vals.height
   if dict['Width'] > vals.width and dict['Height'] > vals.height:
      print "ERROR: w.h"
   else:
      print "OK: w.h"

   
if __name__=='__main__':

   if len(argv) != 2:
      print ("usage: %s filename" % argv[0])
      exit(1)

   list=[]
   for files in os.listdir(argv[1]):
      # print files
      filepath = os.path.join(argv[1], files) # join paths with file
      extn = os.path.splitext(files)[1].strip('.') # strip file extn
      # print extn
      # extract only files and match known extensions
      if os.path.isfile(filepath) and extn in vals.extensions:
         list.append(filepath)

   for l in list:
      print l

      # create obj for class MetaVideo
      stvid = MetaVideo(l)
      dict={}
      dict['Duration']=stvid.duration()
      dict['BitRate']=stvid.bitrate()
      dict['Freq']=stvid.frequency()
      dict['Width'],dict['Height']=stvid.resolution()
      dict['Frame/sec']=stvid.fps()
      dict['Name']=l

      print dict

      validate()
# print vals.bitrate
# print vals.fps
# print vals.freq
# print vals.duration
# print vals.height
# print vals.width


"""       

path="/home/sachin/"
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

----------------------



list = []
for files in os.listdir('.'):
    list.append(files.strip())
print list

-------------------

def videoName(lines):
   for line in lines:
      try:
         vName = re.search(r'from \'.*',line) # from 'tamil.ogv':
         if vName:
            print vName.group().split("'")[1]
            #return vName.group().split()[1] # 1st element of split(), 0th element is string
      except:
         return RE_ERROR   

--------------------

try:
   infile = open('error.txt','rb')
   lines = infile.readlines()
   if lines:
      print "hello"
      for line in lines:
         print line
   else:
      print ":("
except:
   print "enable to read file"

out.close()
err.close()
"""

"""
with open('error.txt') as my_file:
   # I already have file open at this point.. now what?
   my_file.seek(0) #ensure you're at the start of the file..
   first_char = my_file.read(1) #get the first character
   if not first_char:
      print "file is empty" #first character is the empty string..
   else:
      my_file.seek(0) #first character wasn't empty, return to start of file.
         #use file now
------------------------------

def readFile(fileHandle, dictName):

     line = fileHandle.readline()
     dictName = {}
     keycounter = 1

     while line:
         key = str(keycounter)
         dictName[key] = line
         keycounter = keycounter + 1
         line = fileHandle.readline()

     return dictName 
"""

"""
while True:
    out = p.stderr.read(1)
    if out == '' and p.poll() != None:
        break
    if out != '':
        sys.stdout.write(out)
        sys.stdout.flush()
        
--------------------------------------
emailAddress = 'sean@example.com'
title = 'My Email Title'
subject = 'This is the subject of my email'

p1 = subprocess.Popen(['echo', subject], stdout=subprocess.PIPE) #Set up the echo command and direct the output to a pipe
p2 = subprocess.Popen(['mail', '-s' ,title, emailAddress], stdin=p1.stdout #send p1's output to p2
p1.stdout.close() #make sure we close the output so p2 doesn't hang waiting for more input
output = p2.communicate()[0] #run our commands)

"""
