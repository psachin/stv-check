#!/usr/bin/env python2.7

from meta import Metadata

class MetaAudio(Metadata):
   """
   inherit Metadata to use for audio
   """
   def __init__(self, filename):
      """access __init__ method of Metadata class"""
      super(MetaAudio, self).__init__(filename)
      self.lines=super(MetaAudio, self).args()

   def type(self):
      """
      type of audio: mp3, ogg, wav, etc
      """
      for line in self.lines:
         try:
            formatt = re.search(r',?*, from',line)
            return formatt.groups()
         except:
            return self.RE_ERROR
