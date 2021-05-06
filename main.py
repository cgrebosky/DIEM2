import os

import draw
import sys
import time
import data
import video


def manipulate_frame(_args: str, frame_number: int):

    if _args.find('h') >= 0:
        draw.draw_opencv_color_heatmap(frame_number)

    if _args.find('o') >= 0:
        draw.draw_opencv_occluded_heatmap(frame_number)

    if _args.find('c') >= 0:
        draw.draw_circles(frame_number)


if __name__ == '__main__':
    args = sys.argv[1]
    video_name = sys.argv[2]
    data_url = sys.argv[3]
    print("args: %s" % args)
    print("video: %s" % video_name)
    print("data url: %s" % data_url)

    startT = time.time()

    print("SPLITTING VIDEO")
    video.split_video(sys.argv[2])

    data.MovieData("event_data")

    for i in range(1, len(os.listdir("frames"))):
        manipulate_frame(args, i)

    print("CREATING VIDEO")
    video.create_video(sys.argv[2][:-4] + "_PROCESSED.mp4")

    endT = time.time()
    dT = endT - startT
    print("Time Elapsed: %d" % dT)
