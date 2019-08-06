# Program To Read video and Extract Frames
import cv2
import re
import os

# Function to extract frames
def FrameCapture(path):

    # Path to video file
    vidObj = cv2.VideoCapture(path)
    # Used as counter variable
    count = 0
    # checks whether frames were extracted
    success = 1

    while success:
        # vidObj object calls read
        # function extract frames
        success, image = vidObj.read()
        # filename
        tail = os.path.split(path)[1]
        # Saves the frames with frame-count
        cv2.imwrite(os.path.join('/pfs/out', os.path.splitext(tail)[0]+'%d.jpeg' % count), image)
        count += 1

# Driver Code
if __name__ == '__main__':
    # walk /pfs/images and call make_edges on every file found
    for dirpath, dirs, files in os.walk('/pfs/videos'):
        for file in files:
            # Calling the function
            FrameCapture(os.path.join(dirpath, file))
