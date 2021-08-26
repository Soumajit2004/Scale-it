import os
import threading
import time
import cv2
from PIL import Image


# This class converts images main process happens here used in ui.py --> convert_fnc()
class Brain:
    def __init__(self, warning_popup):
        # Warning function from ui.py
        self.warning = warning_popup

    def run(self, img_instance, progress_layout):
        """Converts Images and saves on saving path of img_instance"""

        # Open as OpenCV Image
        image = cv2.imread(img_instance.image)
        # Popup progressbar changed
        progress_layout.on_count_changed(6)

        # Loading Model
        sr = cv2.dnn_superres.DnnSuperResImpl_create()
        model_path = "assets/models/FSRCNN_x4.pb"
        sr.readModel(model_path)
        sr.setModel("fsrcnn", 4)
        # Popup progressbar changed
        progress_layout.on_count_changed(21)

        def thread(image_input):
            """Worker Thread Function for Upscalling Image"""
            # Scaling Image
            result_img = sr.upsample(image_input)
            # Saving Upscale Model Image
            cv2.imwrite("output/image.jpg", result_img)

        # Running Thread Function on diffrent Thread
        th_1 = threading.Thread(target=thread, args=[image])
        th_1.start()
        th_1.join()
        # Popup progressbar changed
        progress_layout.on_count_changed(61)
        # Waiting for 1 sec just in case
        time.sleep(1)

        # Resizing Image
        img = Image.open("output/image.jpg")
        # Popup progressbar changed
        progress_layout.on_count_changed(71)

        # Trying to Catch If Text is inserted in resolution field
        try:
            img = img.resize((int(img_instance.img_width), int(img_instance.img_height)))
        except ValueError:
            self.warning("Invalid Resolution!")
        else:
            # Popup progressbar changed
            progress_layout.on_count_changed(80)

            # Trying to catch if invalid path has been inputted
            try:
                img.save(img_instance.saving_path)
                progress_layout.on_count_changed(89)
            except FileNotFoundError:
                self.warning("Invalid Saving Path!")
        finally:
            # Popup progressbar changed
            progress_layout.on_count_changed(99)
            # Deleting the temporary image
            os.remove("output/image.jpg")
