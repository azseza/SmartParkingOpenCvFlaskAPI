"""
Parking monitor Status
"""
from .motion_detector import MotionDetector


class MonitorThread():
    def __init__(self, video_feed, idParking):
        self.idParking = idParking
        self.video_fead = video_feed
    def start(self, video_feed, idParking):
        mon = MotionDetector(video_feed, idParking, 1)
        mon.detect_motion()
        
