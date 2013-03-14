import subprocess, os, re, time, fnmatch
from subprocess import Popen, PIPE

class Metadata(object):        
   """
   Extracts metadata from input *video* file.
   Takes only one argument: filename

   Returns: duration(HH:MM:SS), fps, resolution[width,height],
   bitrate(Kb/s), frequency(Hz) and size(MB)
   """  
   def __init__(self,filename):
      """construtor: takes input as as argument."""      
      p = Popen(['avconv','-i', filename,'-f','metadata'],stdout=PIPE,stderr=PIPE)
      # output, error = p.communicate()#[0]
      error = p.communicate()[1] # 'avconv' returns file info as error
      self.filename=filename
      self.RE_ERROR = -1        # regExp error
      try:
         lines = error.splitlines()
         if lines:
            self.lines=lines            
         else:
            print "variable line is EMPTY"
      except:
         print "Enable to read variable: error"

   # def args(self):
   #    """just to export lines"""
   #    self.lines=self.lines     # cant return directly
   #    return self.lines

   def duration(self):
      """returns duration in: HH:MM:SS.mili-Sec"""
      for line in self.lines:
         try:
            duration = re.search(r'Duration.*?,',line)
            if duration:
               t = re.search(r'\d\d:\d\d:\d\d.\d\d',duration.group())
               return time.strptime(t.group(),"%H:%M:%S.%f")   # HH:MM:SS.milliseconds
         except:
            return self.RE_ERROR
         
   def fps(self):
      """returns frames/sec"""
      for line in self.lines:
         try:
            frame_per_sec = re.search(r'\d*.[\d*]* fps',line)
            if frame_per_sec:
               return int(frame_per_sec.group().split()[0])
         except:
            return self.RE_ERROR

   def resolution(self):
      """returns height[0], width[1] in px"""
      for line in self.lines:
         try:
            resolution = re.search(r'\d\d\d*x\d\d\d*',line)
            if resolution:
               width = resolution.group().split("x")[0]
               height = resolution.group().split("x")[1]
               return int(width),int(height)
         except:
            return self.RE_ERROR
         
   def frequency(self):
      """returns frequency in Hz"""
      for line in self.lines:
         try:
            freq = re.search(r'\d* Hz',line)
            if freq:
               return int(freq.group().split()[0])
         except:
            return self.RE_ERROR

   def bitrate(self):
      """returns bitrate in Kb/s"""
      for line in self.lines:
         try:
            bitrate = re.search(r'bitrate: \d*',line)
            if bitrate:
               return int(bitrate.group().split()[1]) # 1st element of split(), 0th element is string
         except:
            return self.RE_ERROR

   def size(self):
      '''Convert a file size to human-readable form.'''
      try:
         file_size = subprocess.Popen(['du','-h', self.filename],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
         output = file_size.communicate()[0]
         return int(output.split()[0].split('M')[0])
      except:
         return self.RE_ERROR
      
