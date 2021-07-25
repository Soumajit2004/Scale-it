import threading
import time
import sys
from custom_widget import Ui_pogress_widget
import cv2
from PIL import Image
from PyQt5 import QtWidgets


class Brain:
    def __init__(self, frame):
        self.warning = frame

    def run(self, img_instance, progress_layout):

        # Convert to OpenCV Image
        image = cv2.imread(img_instance.image)
        progress_layout.on_count_changed(6)

        # Loading Model
        sr = cv2.dnn_superres.DnnSuperResImpl_create()
        model_path = "assets/models/FSRCNN_x4.pb"
        sr.readModel(model_path)
        sr.setModel("fsrcnn", 4)
        progress_layout.on_count_changed(21)

        def thread(image):

            # Upscaling Image
            result_img = sr.upsample(image)
            cv2.imwrite("output/image.png", result_img)

        th_1 = threading.Thread(target=thread, args=[image])
        th_1.start()
        th_1.join()
        progress_layout.on_count_changed(61)

        # Resizing Image
        img = Image.open("output/image.png")
        progress_layout.on_count_changed(71)
        try:
            img = img.resize((int(img_instance.img_width), int(img_instance.img_height)))
        except ValueError:
            self.warning("Invalid Resolution!")
        else:
            progress_layout.on_count_changed(80)
            try:
                img.save(img_instance.saving_path)
                progress_layout.on_count_changed(89)
            except FileNotFoundError:
                self.warning("Invalid Saving Path!")
        finally:
            progress_layout.on_count_changed(99)
