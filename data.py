import os


def read_line(line: str):
    words = line.split()

    a = SingleEyeData(words[1], words[2], words[3], words[4])
    b = SingleEyeData(words[5], words[6], words[7], words[8])

    return a, b


class SingleEyeData:
    def __init__(self, x, y, dil, event):
        self.x = float(x)
        self.y = float(y)
        self.dil = float(dil)
        self.event = int(event)


class MovieData:
    # This is 33 seconds of 30fps footage, this is a reasonable buffer to have.
    # More space can be added on the fly, but that takes time, so we start with some space allocated
    video_data = [[] for i in range(0, 1000)]

    def __init__(self, data_url: str):

        files = os.listdir(data_url)

        for i in files:
            if i == ".gitkeep":
                continue

            file = open(data_url + i, "r")

            print("Processing data for %s dataset" % i)

            # TODO: Change to detect frame-count?  Probably while.
            frame = 0
            for line in file:
                a, b = read_line(line)

                try:
                    self.video_data[frame].append(a)
                    self.video_data[frame].append(b)
                except IndexError:
                    self.video_data.append([])
                    self.video_data.append([])
                    self.video_data[frame].append(a)
                    self.video_data[frame].append(b)

                frame += 1

            file.close()
