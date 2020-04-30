import cv2
from hyperlpr import HyperLPR_plate_recognition
def scan():
    gailv={}
    cap=cv2.VideoCapture(0)
    cap.open(0)
    ass=[]
    while True:
        ret,frame=cap.read()
        cv2.imshow('frame',frame)
        a = HyperLPR_plate_recognition(frame)
        if len(a)!=0:
            ass.append(a)
        if len(ass)==20:
            break
        if cv2.waitKey(1)==ord('q'):
            break
    cv2.destroyAllWindows()
    cap.release()
    # print(ass)
    for i in ass:
        for q in i:
            gailv[q[0]]=q[1]
    max_a=max(zip(gailv.keys(),gailv.values()))
    return max_a[0]

