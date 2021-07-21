import cv2
from PIL import Image


class Brain:

    def run(self, img_instance):
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

        # Resizing Image
        img = Image.open("output/image.png")
        img = img.resize((int(img_instance.img_width), int(img_instance.img_height)))
        img.save(img_instance.saving_path)
