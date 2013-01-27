#!/usr/bin/env python2.7
import time

class vals():
    """
    define all the video parameters here
    """
    fps=2
    duration=time.strptime("00:10:00.0","%H:%M:%S.%f")
    bitrate=320
    freq=45000
    width=600
    height=480
    # size ???
        
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

    def __init__(self):
        pass
    
    
        
        
