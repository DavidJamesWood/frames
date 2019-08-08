# Program To Read video and Extract Frames
import re
import os
import imageio
import imageio_ffmpeg

# Function to extract frames
def FrameCapture(path):

    # Used as counter variable
    count = 0
    # checks whether frames were extracted
    success = 1
    # Process video
    vid = imageio.get_reader(path)
    # file name
    tail = os.path.split(path)[1]
    # iterate through frames
    for image in vid.iter_data():
        # write each frame
        imageio.imwrite(os.path.join('/pfs/out', os.path.splitext(tail)[0]+'%d.jpeg' % count), image)
        count += 1

# Driver Code
if __name__ == '__main__':
    # walk /pfs/videos and call frames on every file found
    for dirpath, dirs, files in os.walk('/pfs/videos'):
        for file in files:
            # Calling the function
            FrameCapture(os.path.join(dirpath, file))
