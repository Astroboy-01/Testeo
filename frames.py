import cv2
import time

 
video = cv2.VideoCapture(0)
    
num_frames = 100
    
print("Capturando {0} frames".format(num_frames))

start = time.time()
    
for i in range(0, num_frames):
    ret, frame = video.read()

end = time.time()
 
seconds = end - start
print("Tiempo de captura: {0} seconds".format(seconds))

fps  = num_frames / seconds
print("Frames per second estimado: {0}".format(fps))
video.release()