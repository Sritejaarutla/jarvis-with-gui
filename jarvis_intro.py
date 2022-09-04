#code to play video in full screen mode

import cv2
import numpy as np
import ffpyplayer
#ffpyplayer for playing audio
from ffpyplayer.player import MediaPlayer
video_path="D:\Jarvis project\jarvis scifi intro.mp4"
window_name="window" #necessary for full screen
def JarvisIntro(video_path):
    video=cv2.VideoCapture(video_path)
    player = MediaPlayer(video_path)
    cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)#necessary for full screen
    cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)#necessary for full screen
    while True:
        grabbed, frame=video.read()
        audio_frame, val = player.get_frame()
        if not grabbed:
            print("End of video")
            break
        if cv2.waitKey(27) & 0xFF == ord("q"):#waitkey(27) is used for video duration speed ki idhi adjust according to video length
            break

            # 0xFF==ord("q") press q to quit from video

        cv2.imshow(window_name, frame)# for full screen
        if val != 'eof' and audio_frame is not None:
            #audio
            img, t = audio_frame
    video.release()
    cv2.destroyAllWindows()
# JarvisIntro(video_path)

