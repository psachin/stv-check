from meta import Metadata, time

class MetaVideo(Metadata):
   """
   inherit Metadata to use for video
   """
   def __init__(self, filename):
      """access __init__ method of Metadata class"""
      super(MetaVideo, self).__init__(filename)
      
   def duration(self):
      """returns duration in formatted text"""
      self.vid_duration=super(MetaVideo, self).duration
      return time.strftime('%H:%M:%S', self.vid_duration())
      

