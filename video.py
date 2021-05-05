import os

# TODO: Change these to OpenCV based, I'd rather avoid dependencies


def split_video(url: str):
    # -loglevel panic
    os.system("ffmpeg -i  " + url + " frames/f%04d.jpg")


def create_video(url: str, framerate=30):
    # -loglevel panic
    os.system("ffmpeg -y -r 30 -i frames/f%04d.jpg -strict experimental -vcodec libx264 -preset "
              "ultrafast -crf 30 " + url)
