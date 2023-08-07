import cv2

vid = cv2.VideoCapture(0)

if (vid.isOpened() == False):
    print('unable to read the feed')

height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(height)

width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
print(width)

fps  = int(vid.get(cv2.CAP_PROP_FPS))
print(fps)
output = cv2.VideoWriter('sample.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 30, (width, height))
while True: 
    ret, frame= vid.read()
    cv2.imshow('webcam', frame)
    output.write(frame)
    if cv2.waitKey(20) == 32:
        break
vid.release()
output.release()
cv2.destroyAllWindows()