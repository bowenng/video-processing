import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

def extract_frames(video_file, save_to_folder, save_every_frame=10, starting_frame=10):
    capture = cv2.VideoCapture(video_file)
    
    frame_name = 1
    n_frame = starting_frame
    total_frames = capture.get(cv2.CAP_PROP_FRAME_COUNT) - starting_frame
    
    progress_bar = " " * 10 + '0%'
    progress = 0
    
    print('start extracting frames...')
    print(progress_bar, end='\r')
    
    while capture.isOpened():
        n_frame += 1
        ret, frame = capture.read()
        
        if n_frame % save_every_frame == 0:
            cv2.imwrite(os.path.join('CapturedFrames', 'YourName', '{}.jpg'.format(frame_name)), frame)
            frame_name += 1
        
        if (n_frame / total_frames) > (progress/100):
            progress += 1
            progress_bar = ("=" * (progress//10)) + '>' + (' ' * (10-progress//10)) + '{}%'.format(progress)
            print(progress_bar, end='\r')  
        if n_frame >= total_frames:
            break
    # When everything done, release the capture
    print('='*10 + '>' + '100%')
    print('Finished')
    capture.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    file = os.path.join('VideoSrc', 'yourname.flv')
    save_to = os.path.join('CapturedFrames', 'YourName')
    extract_frames(file, save_to)