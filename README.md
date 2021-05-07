# DIEM2
This project is a continuation of the old [DIEM](https://thediemproject.wordpress.com) project.  The old version is 
severely outdated, slow, and limited.  The goal of this update isn't to provide more functionality, but to avoid
dependency hell and associated aging with the last version.


## Usage
An example of a full command to run this program would look something like this:
```python
python3 ~/PythonProjects/DIEM2/main.py hl ~/Downloads/advert_bbc4_bees_1024x576/video/advert_bbc4_bees_1024x576.mp4 ~/Downloads/advert_bbc4_bees_1024x576/event_data/
```
The command takes 3 arguments:
1. Processing Arguments.
2. URL of the video to modify.
3. URL of the folder enclosing eyetracking data.

Processing Arguments has 4 modes.  You can mix and match these as you like, e.g., you can pass `hocl` to do all 4 
processes on the same video, or just `h` to do a single process.  The processes are as follows:
* h: Color Heatmap (draws a heatmap over where people look)
* o: Occluded Heatmap (blocks out the background that people don't look at)
* c: Circles (draw circles at the positions where people look)
* l: Lines (draw lines from eye positions, this is helpful for visualizing eye movement)


## Dependencies
Currently, this makes use of only 2 dependencies: [OpenCV](https://pypi.org/project/opencv-python/) and 
[ffmpeg](https://ffmpeg.org).  Both of these are extraordinarily well-maintained.  This program assumes that the data
fed into this program is from an [Eyelink 1000](https://www.sr-research.com/eyelink-1000-plus/).