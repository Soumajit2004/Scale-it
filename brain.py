import threading

import cv2
from PIL import Image
from PyQt5 import QtWidgets


class Brain:
    def __init__(self, frame):
        self.frame = frame

    def run(self, img_instance):

        # Convert to OpenCV Image
        image = cv2.imread(img_instance.image)

        # Loading Model
        sr = cv2.dnn_superres.DnnSuperResImpl_create()
        model_path = "assets/models/FSRCNN_x4.pb"
        sr.readModel(model_path)
        sr.setModel("fsrcnn", 4)

        def thread(image):

            # Upscaling Image
            result_img = sr.upsample(image)
            cv2.imwrite("output/image.png", result_img)

        th_1 = threading.Thread(target=thread, args=[image])
        th_1.start()
        th_1.join()

        # Resizing Image
        img = Image.open("output/image.png")
        try:
            img = img.resize((int(img_instance.img_width), int(img_instance.img_height)))
        except ValueError:
            self.frame("Invalid Resolution!")
        else:
            try:
                img.save(img_instance.saving_path)
            except FileNotFoundError:
                self.frame("Invalid Saving Path!")
