import os
from multiprocessing import Pool

import draw
import sys
import time
import data
import video


def manipulate_frame(data: data.SingleFrameData, args: str, frame_number: int):

    if args.find('h') >= 0:
        draw.draw_opencv_color_heatmap(data, frame_number)

    if args.find('o') >= 0:
        draw.draw_opencv_occluded_heatmap(data, frame_number)

    if args.find('c') >= 0:
        draw.draw_circles(data, frame_number)


movie = data.MovieData()


def l_manipulate_frame(f_num):
    manipulate_frame(movie.video_data[f_num-1], sys.argv[1], f_num)


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

    movie = data.MovieData()
    args = sys.argv[1]

    for i in range(1, len(os.listdir("frames"))):
        l_manipulate_frame(i)

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
