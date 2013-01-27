#!/usr/bin/env python2.7

from sys import argv
import subprocess, os, re, time, fnmatch
from subprocess import Popen, PIPE
from os.path import join, getsize

from conf import vals           # import reference values
RE_ERROR = 1                  # regExp error

class Metadata(object):         # inherite from object class(I think its convention :P)
   """
   Extracts metadata from input *video* file.
   Takes only one argument: filename

   Returns: duration(HH:MM:SS.mSec), fps, resolution[width,height],
   bitrate(Kb/s), frequency(Hz) and size(MB)
   """  
   RE_ERROR = 1                  # regExp error
   def __init__(self,filename):
      """construtor: takes input as as argument."""      
      p = subprocess.Popen(['avconv','-i', filename,'-f','metadata'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
      output, error = p.communicate()#[0]
      self.filename=filename
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

   def size(self):
      """return size in MB"""
      return float(os.path.getsize(self.filename)/1048576)
      

class MetaVideo(Metadata):
   """
   inherit Metadata to use for video

   class DerivedClass(Base):
       def some_method(self):
           super(DerivedClass, self).meth()
              
   """

   def __init__(self,filename):
      """access __init__ method of Metadata class"""
      super(MetaVideo, self).__init__(filename)
      """access RE_ERROR attrib of Metadata class"""
      super(MetaVideo, self).RE_ERROR
      

def validate():
   """test value w.r.t to values provided in conf.py"""
   if dict['Duration'] > vals.duration:
      print "ERROR: duration"
   else:
      print "OK: duration"
   
   if dict['Frame/sec'] > vals.fps:
      print "ERROR: fps"
   else:
      print "OK: fps"

   if dict['BitRate'] > vals.bitrate:
      print "ERROR: bitrate"
   else:
      print "OK: bitrate"
      
   if dict['Freq'] > vals.freq:
      print "ERROR: freq"
   else:
      print "OK: freq"

   if dict['Width'] > vals.width and dict['Height'] > vals.height:
      print "ERROR: w.h"
   else:
      print "OK: w.h"

   if dict['Size'] > vals.size:
      print "ERROR: size"
   else:
      print "OK: size"
   


if __name__=='__main__':

   if len(argv) != 2:
      print ("Usage: %s <dir_with_video_files>" % argv[0])
      exit(1)

   match = []                   # create a list of filepath
   for root, dirnames, filenames in os.walk(argv[1]):
      for filename in fnmatch.filter(filenames, '*'): # match everything
         extn = os.path.splitext(filename)[1].strip('.') # strip out extension
         if extn in vals.extensions:                     # filter out selected extensions
            match.append(os.path.join(root, filename))   # append it to a list
   for l in match:              # sort out filepath
      # create obj for class MetaVideo
      stvid = MetaVideo(l)      
      dict={}                   
      dict['Duration']=stvid.duration()
      dict['BitRate']=stvid.bitrate()
      dict['Freq']=stvid.frequency()
      dict['Width'],dict['Height']=stvid.resolution()
      dict['Frame/sec']=stvid.fps()
      dict['Name']=l
      dict['Size']=stvid.size()
      print "\n"+ l + "\n--------------------"
      validate()

