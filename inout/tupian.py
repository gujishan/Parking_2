import cv2
from hyperlpr import *



def scan_tu(image):
    image = cv2.imread(image)
    a=HyperLPR_plate_recognition(image)
    return a[0][0]

# if __name__ == '__main__':
#     path='./image/123.jpg'
#     print(type(path))
#     print(scan_tu(path))

# input_file_path = os.path.dirname('123.jpg')
# print(input_file_path)