import os

import draw
import sys
import time
import data
import video
import cv2
import argparse


def manipulate_frame(_args, frame_number: int):
    img_url = "frames/f%04d.jpg" % frame_number
    img = cv2.imread(img_url)

    if frame_number > len(data.MovieData.video_data):
        return

    if _args.process.find('h') >= 0:
        img = draw.draw_opencv_color_heatmap(frame_number, img)

    if _args.process.find('o') >= 0:
        img = draw.draw_opencv_occluded_heatmap(frame_number, img)


    if _args.process.find('c') >= 0:
        img = draw.draw_circles(frame_number, img)

    if _args.process.find('l') >= 0:
        img = draw.draw_lines(frame_number, img)

    if not _args.nowrite:
        cv2.imwrite(img_url, img)
    if _args.show:
        cv2.imshow("DIEM2 - press any 'ESC' to stop", img)
    if _args.verbose:
        print("Processed frame %d" % frame_number)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Process a video to visualize eye-movements")
    parser.add_argument('process', type=str, help="The processing arguments.  See README.md")
    parser.add_argument('video', type=str, help="The url of the input video")
    parser.add_argument('data', type=str, help="The enclosing folder of the data")
    parser.add_argument('--nosplit', help="Skip the split-video-into-frames step", action="store_true")
    parser.add_argument('--nocreate', help="don't actually write to a video, just make frames", action="store_true")
    parser.add_argument('--nowrite', help="don't actually write to frames, useful with --show", action="store_true")
    parser.add_argument('--show', help="show the results in real-time in a window. To stop, press 'ESC' key", action="store_true")
    parser.add_argument('--verbose', help="print a message with every process", action="store_true")
    args = parser.parse_args()

    if not args.nosplit:
        print("SPLITTING VIDEO")
        video.split_video(sys.argv[2])

    print("PROCESSING DATA")
    data.MovieData(args.data, args)

    print("PROCESSING FRAMES")
    for i in range(1, len(os.listdir("frames"))):
        manipulate_frame(args, i)

        if args.show and cv2.waitKey(1) & 0xFF == 27:
            break

    if not args.nocreate:
        print("CREATING VIDEO")
        video.create_video(args.video[:-4] + "_PROCESSED.mp4")
