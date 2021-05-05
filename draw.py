import cv2
import numpy as np
import data

# region circle
def draw_circle(point: data.SingleEyeData, img: cv2.cv2, circle_radius=20, circle_color=(0, 255, 0), thickness=1):

    img = cv2.circle(img, (int(point.x), int(point.y)), circle_radius, circle_color, thickness=thickness)


# TODO: Change points datatype.  Well, I guess it doesn't matter too much, but the unzipped is ugly :(
def draw_circles(points: data.SingleFrameData, frame_number):
    img_url = "frames/f%04d.jpg" % frame_number
    img = cv2.imread(img_url)
    for i in points.eye_positions:
        draw_circle(i, img)

    cv2.imwrite(img_url, img)

    print("Drawn circles for " + img_url)
#endregion circle

#This may be useful to keep around, but I've decided not to use seaborn,
# as it's unacceptably slow and introduces dependencies
# region seaborn heatmap
# def draw_heatmap(points: data.SingleFrameData, frame_number, resolution=(25, 25)):
#     filename = "frames/f%04d" % frame_number + ".jpg"
#
#     datx: list[float] = list()
#     daty: list[float] = list()
#     for i in points.eye_positions:
#         datx.append(i.x)
#         daty.append(i.y)
#
#     plt.figure(figsize=resolution)
#     sns_plot = sns.kdeplot(x=datx, y=daty, cmap="vlag", shade=True, bw_adjust=.7, alpha=0.5, antialiased=True)
#
#     sns_plot.collections[0].set_alpha(0)
#     plt.axis("off")
#     plt.xlim(0, 3840)
#     plt.ylim(0, 2160)
#     plt.margins(0, 0)
#
#     bgimg = mpimg.imread(filename)
#     plt.imshow(bgimg)
#     # plt.show will display the plots in real time.  This is nice for debugging, but very slow
#     # plt.show()
#
#     fig = sns_plot.get_figure()
#     fig.savefig(filename, bbox_inches="tight", pad_inches=0, transparent=True)
#
#     fig.clf()
#     plt.close(fig)
#
#     print("Drawn heatmap for " + filename)
# endregion heatmap

# region opencv heatmap


def make_opencv_heatmap(points: data.SingleFrameData):
    # We're assuming, reasonably, that all frames are the same size, so just sample the 1st
    shape = cv2.imread("frames/f0001.jpg").shape

    black_img = np.zeros(shape, np.uint8)

    size = 20
    smooth = (81, 81)

    # This is good enough - it looks a bit janky with just one pass, but it takes too long
    # and is unnecessarily complex with programmatically-defined passes (say, 5 passes)
    for i in points.eye_positions:
        pos = (int(i.x), int(i.y))
        cv2.circle(black_img, pos, size * 2, (127, 127, 127), -1)
    for i in points.eye_positions:
        pos = (int(i.x), int(i.y))
        cv2.circle(black_img, pos, size, (255, 255, 255), -1)

    for _ in range(0, 4):
        cv2.blur(black_img, smooth, black_img)

    return black_img


def draw_opencv_occluded_heatmap(points: data.SingleFrameData, frame_number):
    filename = "frames/f%04d" % frame_number + ".jpg"

    img = cv2.imread(filename)
    black_img = make_opencv_heatmap(points)

    cv2.imwrite("cv_heatmap_test.jpg", black_img)
    black_img = black_img / 255
    img = img * black_img
    cv2.imwrite(filename, img)

    print("Drawn Occluded Heatmap for " + filename)


def draw_opencv_color_heatmap(points: data.SingleFrameData, frame_number):
    filename = "frames/f%04d" % frame_number + ".jpg"

    img = cv2.imread(filename)
    black_img = make_opencv_heatmap(points)
    false_colored = black_img.copy()

    cv2.applyColorMap(black_img, cv2.COLORMAP_JET, false_colored)
    black_img = black_img / 255
    cv2.threshold(black_img, 0.3, 1.0, cv2.THRESH_TRUNC, black_img)

    false_colored = false_colored * black_img
    img = cv2.add(img, false_colored, dtype=cv2.CV_64F)


    cv2.imwrite(filename, img)
    print("Drawn Color Heatmap for " + filename)

#endregion opencv heatmap
