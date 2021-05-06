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
    video_data = [[] for i in range(0, 528)]

    def __init__(self, data_url: str):

        dir = "/Users/carsongrebosky/PycharmProjects/DIEM2/event_data/"
        files = os.listdir(dir)

        for i in files:
            if i == ".gitkeep":
                continue

            file = open(dir + i, "r")

            print("Gathering data for %s", i)

            # TODO: Change to detect frame-count?  Probably while.
            for j in range(0, 528):
                a, b = read_line(file.readline())
                self.video_data[j].append(a)
                self.video_data[j].append(b)

            file.close()
