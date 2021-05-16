import os


def split_video(url: str):
    # -loglevel panic
    os.system("ffmpeg -i  " + url + " frames/f%04d.jpg")


def create_video(url: str, framerate=30):
    # The HIGHER crf means LOWER quality and LOWER file size.
    # This may be useful for making quick mock-ups, but for anything professional, 30 or lower is probably best.
    crf = 30
    # -loglevel panic
    os.system("ffmpeg -y -r 30 -i frames/f%04d.jpg -strict experimental -vcodec libx264 -preset "
              "ultrafast -crf {crf} {url}".format(crf=crf, url=url))
