from sys import argv
import subprocess, os, re, time, fnmatch, glob
from os.path import join, getsize
from metavideo import MetaVideo
from conf import vals           # import reference values

def validate():
   """test value w.r.t to values provided in conf.py"""
   if dict['Duration'] > vals.duration:
      print "ERROR: duration"
      print "Video duration: %s" %(dict['Duration'])
      print "Default duration: %s" %(vals.duration)
   else:
      print "OK: duration"
   
   if dict['Frame/sec'] > vals.fps:
      print "ERROR: fps"
      print "Video frame rate: %d fps" %(dict['Frame/sec'])
      print "Default frame rate: %d fps" %(vals.fps)
   else:
      print "OK: fps"

   if dict['BitRate'] > vals.bitrate:
      print "ERROR: bitrate"
      print "Video bitrate: %d" %(dict['BitRate'])
      print "Default bitrate: %d" %(vals.bitrate)
   else:
      print "OK: bitrate"
      
   if dict['Freq'] > vals.freq:
      print "ERROR: freq"
      print "Video freq: %d Hz" %(dict['Freq'])
      print "Default freq: %d Hz" %(vals.freq)
   else:
      print "OK: freq"

   if dict['Width'] > vals.width and dict['Height'] > vals.height:
      print "ERROR: width & height"
      print "Video Width: %d px" %(dict['Width'])
      print "Default Width: %d px" %(vals.width)
      print ""
      print "Video Height: %d px" %(dict['Height'])
      print "Default Height: %d px" %(vals.height)
   else:
      print "OK: width & height"

   if dict['Size'] > vals.size:
      print "ERROR: size"
      print "Video size: %d M" %(dict['Size'])
      print "Default size: %d M" %(vals.size)
   else:
      print "OK: size"
   

if __name__=='__main__':

   if len(argv) != 2:
      print ("Error: Please provide directory path or a file name")
      print ("Usage: %s <dir_with_video_files>" % argv[0])
      exit(1)

   match = []                   # create a list of filepath
   if os.path.isfile(argv[1]):
      extn = os.path.splitext(argv[1])[1].strip('.') # strip out extension
      if extn in vals.extensions:                     # filter out selected extensions
         match.append(os.path.join(argv[1]))   # append it to a list
   else:     
      for root, dirnames, filenames in os.walk(argv[1]):
         for filename in fnmatch.filter(filenames, '*'): # match everything
            extn = os.path.splitext(filename)[1].strip('.') # strip out extension
            if extn in vals.extensions:                     # filter out selected extensions
               match.append(os.path.join(root, filename))   # append it to a list
            else:
               print "ERROR: Extension NOT supported"
               print "Please add extension in conf.py"

   for l in match:              # sort out filepath
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
      #print dict
      validate()


