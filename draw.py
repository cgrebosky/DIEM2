import cv2
import numpy as np
import data


def draw_circle(point: data.SingleEyeData, img: cv2.cv2, circle_color=(0, 255, 0), thickness=1):
    cv2.circle(img, (int(point.x), int(point.y)), int(point.radius), circle_color, thickness=thickness)


def draw_circles(frame_number, img):
    for i in data.MovieData.video_data[frame_number-1]:
        draw_circle(i, img)

    return img


def draw_lines(frame_number, img):
    # A bit ugly, but it works.  There may be a clearer way to do this
    for i in range(0, len(data.MovieData.video_data[frame_number-1])):
        pre = data.MovieData.video_data[frame_number-1][i]
        post = data.MovieData.video_data[frame_number][i]

        if pre.event != 1 or post.event != 1:
            continue

        pre_pos = (int(pre.x), int(pre.y))
        post_pos = (int(post.x), int(post.y))

        img = cv2.line(img, pre_pos, post_pos, (0, 255, 0), 1)

    return img


def make_opencv_heatmap(frame_number):
    # We're assuming, reasonably, that all frames are the same size, so just sample the 1st
    shape = cv2.imread("frames/f0001.jpg").shape

    black_img = np.zeros(shape, np.uint8)

    size = 20
    smooth = (81, 81)

    # This is good enough - it looks a bit janky with just one pass, but it takes too long
    # and is unnecessarily complex with programmatically-defined passes (say, 5 passes)
    for i in data.MovieData.video_data[frame_number-1]:
        pos = (int(i.x), int(i.y))
        cv2.circle(black_img, pos, size * 2, (127, 127, 127), -1)
    for i in data.MovieData.video_data[frame_number-1]:
        pos = (int(i.x), int(i.y))
        cv2.circle(black_img, pos, size, (255, 255, 255), -1)

    for _ in range(0, 4):
        cv2.blur(black_img, smooth, black_img)

    return black_img


def draw_opencv_occluded_heatmap(frame_number, img):
    black_img = make_opencv_heatmap(frame_number)

    black_img = black_img / 255
    img = img * black_img / 255

    return img


def draw_opencv_color_heatmap(frame_number, img):
    black_img = make_opencv_heatmap(frame_number)
    false_colored = black_img.copy()

    cv2.applyColorMap(black_img, cv2.COLORMAP_JET, false_colored)

    black_img = black_img / 255
    img = img / 255
    false_colored = false_colored / 255

    cv2.threshold(black_img, 0.3, 1.0, cv2.THRESH_TRUNC, black_img)
    false_colored = false_colored * black_img
    img = cv2.add(img, false_colored, dtype=cv2.CV_64F)

    return img
