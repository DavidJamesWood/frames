# Program To Read video
# and Extract Frames
import cv2
import re
import os

# Function to extract frames
def FrameCapture(path, outDir):

    # check if output dir exists
    if not os.path.exists(outDir):
        # create directory with the video name
        try:
            os.mkdir(outDir)
        except OSError:
            print ("Creation of the directory %s failed" % outDir)
        else:
            print ("Successfully created the directory %s " % outDir)

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

            # Saves the frames with frame-count
            cv2.imwrite(outDir+"/frame%d.jpg" % count, image)

            count += 1
    else:
        print("Video is already processed.")

# Driver Code
if __name__ == '__main__':

    path = '/Users/davidwood/Ocean_Waves_slow_motion_videvo.mov'

    outDir = re.search(r'^.*(\\|\/)(.*)\..*$', path).group(2)

    # Calling the function
    FrameCapture(path, outDir)
