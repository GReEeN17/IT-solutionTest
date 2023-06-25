from moviepy.editor import ImageSequenceClip
import numpy as np
import cv2

# Function for drawing text on an image
def draw_text(txt, t):
    # Making image using numpy for it
    img = np.zeros((100, 100, 3), np.uint8)
    # Arguments to pass in opencv function
    font_size = 1
    # Text is "running" due to the fact that we are moving its x coordinate
    x = 100 - t * len(txt) * 6
    y = 50
    # Drawing text on an image using cv2 bibliothek from opencv
    cv2.putText(img, txt, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, font_size, (255, 255, 255), thickness=1)
    # Returning one frame from the hole video
    return img

def make_video(txt):
    # Duration of the resulting video
    duration = 3
    fps = 30
    # Making video using moviepy bibliothek
    video = ImageSequenceClip([draw_text(txt, t) for t in np.arange(0, duration, 1/fps)], fps=fps)
    # Saving video in current folder
    video.write_videofile('running_text.mp4', fps=fps)
