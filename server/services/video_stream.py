import cv2
import requests
from ultralytics import YOLO

from server.services.watcher import identified_pothole

URL = "http://192.168.59.169"
AWB = True

model = YOLO('server/assets/best.pt')
print("model loaded...")

cap = cv2.VideoCapture(URL + ":81/stream")


def set_resolution(url: str, index: int = 1, verbose: bool = False):
    try:
        if verbose:
            resolutions = ("10: UXGA(1600x1200)\n9: SXGA(1280x1024)\n8: XGA(1024x768)\n7: SVGA(800x600)\n6: VGA("
                           "640x480)\n5: CIF(400x296)\n4: QVGA(320x240)\n3: HQVGA(240x176)\n0: QQVGA(160x120)")
            print("available resolutions\n{}".format(resolutions))

        if index in [10, 9, 8, 7, 6, 5, 4, 3, 0]:
            requests.get(url + "/control?var=framesize&val={}".format(index))
        else:
            print("Wrong index")
    except:
        print("SET_RESOLUTION: something went wrong")


set_resolution(URL, index=8)


def start_stream_capture():
    print("video stream monitoring started...")
    while True:
        if cap.isOpened():
            ret, frame = cap.read()

            results = model.predict(frame)

            for result in results:
                if len(result.boxes.xyxy) > 0:
                    identified_pothole(len(result.boxes.xyxy))
