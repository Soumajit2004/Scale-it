import cv2
from PIL import Image
import threading


class Brain:

    def __init__(self):
        pass

    def upscale_img(self, img_instance, width, height):

        def upscale():
            # Convert to OpenCV Image
            img = cv2.imread(img_instance.image)

            # Loading Model
            sr = cv2.dnn_superres.DnnSuperResImpl_create()
            model_path = "assets/models/FSRCNN_x4.pb"
            sr.readModel(model_path)
            sr.setModel("fsrcnn", 4)

            # Upscaling Image
            result_img = sr.upsample(img)
            cv2.imwrite("output/image.png", result_img)

        # Multi Threading
        threading_1 = threading.Thread(target=upscale)
        threading_1.start()
        threading_1.join()

        # Resizing Image
        img = Image.open("output/image.png")
        img = img.resize((width, height))
        img.show()

