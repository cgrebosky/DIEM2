import video


if __name__ == '__main__':
    print("SPLITTING VIDEO")
    video.split_video("test_video.mp4")

    # print("PROCESSING FRAMES")
    # p = Pool(processes=8)
    # result = p.map(modify_image, range(1,len(os.listdir("frames"))))
    #
    # print("CREATING VIDEO")
    # video.create_video("out.mp4")





