import time

class vals():
    """
    define all the video parameters here
    """

    __author__ = "Sachin Patil (isachin@iitb.ac.in)"
    __version__ = "0.9"
    __date__ = "Thu Mar 14 10:39:52 2013"
    __copyright__ = "Copyright (c) 2013 Sachin Patil"
    __license__ = "GPL v3"


    fps=4
    duration=time.strftime('%H:%M:%S', time.strptime("00:15:00.0","%H:%M:%S.%f"))
    bitrate=320
    freq=45000
    width=800
    height=600
    size=15
        
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
    
    
        
        
