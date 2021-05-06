import os
from multiprocessing import Pool

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

    # print("SPLITTING VIDEO")
    # video.split_video(sys.argv[2])

    data.MovieData("event_data")
    args = sys.argv[1]

    for i in range(1, len(os.listdir("frames"))):
        manipulate_frame(args, i)

    # 4 processes seems to be the best on my computer.  This may be different on yours.
    # TODO: Figure out multithreading!  The code below kinda works, but I still have to manage variable-sharing... :(
    # p = Pool(processes=4)
    # result = p.map(
    #     l_manipulate_frame,
    #     range(1, len(os.listdir("frames")))
    # )

    endT = time.time()
    dT = endT - startT
    print("Time Elapsed: %d" % dT)

    print("CREATING VIDEO")
    video.create_video("PROCESSED" + sys.argv[2])
