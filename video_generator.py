import cv2
import numpy as np

# Define video settings
width, height = 640, 480
fps = 24
duration = 3
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('test_video.mp4', fourcc, fps, (width, height))

# create and write dummt frames
for _ in range(fps * duration):
    frame = np.zeros((height, width, 3), dtype=np.uint8) # black frame
    out.write(frame)

out.release()
print("video saved as test_video.mp4")