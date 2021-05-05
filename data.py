import numpy as np


class SingleEyeData:
    dil = 0
    event = 0

    # TODO: Change to be initialized via string, not randomized.  This works for now, tho
    def __init__(self):
        self.x = np.random.normal(500, 50)
        self.y = np.random.normal(500, 50)


class SingleFrameData:
    frame_number = 0

    def __init__(self):
        self.eye_positions: list[SingleEyeData] = list()
        for i in range(0, 25):
            self.eye_positions.append(SingleEyeData())


class MovieData:

    def __init__(self):
        self.video_data: list[SingleFrameData] = list()
        for i in range(0, 528):
            self.video_data.append(SingleFrameData())
            self.video_data[i].frame_number = i+1
