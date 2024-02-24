import cv2

trdict = {'csrt': cv2.TrackerCSRT_create,
          'kcf': cv2.TrackerKCF_create,
          'mil': cv2.TrackerMIL_create}

tracker = trdict['csrt']()
v = cv2.VideoCapture('move.mp4')

ret, frame = v.read()
1
if not ret or frame is None:
    print("Error: Unable to read the video frame.")
    exit(1)

cv2.imshow('Frame', frame)
bb = cv2.selectROI('Frame', frame)
tracker.init(frame, bb)

while True:
    ret, frame = v.read()
    if not ret or frame is None:
        break

    success, box = tracker.update(frame)
    if success:
        x, y, w, h = [int(a) for a in box]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('Frame', frame)
    key = cv2.waitKey(5) & 0xFF
    if key == ord('q'):
        break

v.release()
cv2.destroyAllWindows()
