from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets
import ui
from PIL.ExifTags import TAGS
import os
from hurry.filesize import alternative, size


class ImageWidget:
    def __init__(self, image_path, widget_id, date_label, space_label, format_label, color_label, width_input,
                 height_input):
        # Labels
        self.date_label = date_label
        self.space_label = space_label
        self.format_label = format_label
        self.color_label = color_label
        self.width_input = width_input
        self.height_input = height_input

        # Raw Image Path
        self.widget_id = widget_id
        self.image = image_path
        self.pil_img = Image.open(image_path)
        self.saving_path = image_path

        # Dimensions
        self.img_width, self.img_height = self.pil_img.size

        # Image Name
        self.image_name = self.image.split("/")[-1]
        # Processing Image Name If Required
        if len(self.image_name) > 10:
            self.short_name = ""
            for l in self.image_name:
                if len(self.short_name) < 8:
                    self.short_name += l
            self.short_name += "..."
            self.image_name = self.short_name

    def setup(self):
        self.Form = QtWidgets.QWidget()
        self.Form.setObjectName("self.Form")
        self.Form.resize(500, 100)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Form.sizePolicy().hasHeightForWidth())
        self.Form.setSizePolicy(sizePolicy)
        self.Form.setMinimumSize(QtCore.QSize(0, 100))
        self.Form.setMaximumSize(QtCore.QSize(16777215, 100))
        self.Form.setStyleSheet("background-color:#98DED9; border-radius:8px;")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.Form)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("assets/images/image.png"))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.image_label = QtWidgets.QLabel(self.Form)
        font = QtGui.QFont()
        font.setFamily("Poppins SemiBold")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.image_label.setFont(font)
        self.image_label.setStyleSheet("QLabel{\n"
                                       "color:#161D6F;\n"
                                       "border:0px;\n"
                                       "}")
        self.image_label.setObjectName("image_label")
        self.horizontalLayout.addWidget(self.image_label)
        spacerItem = QtWidgets.QSpacerItem(240, 20, QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.Form)
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "border: 1px solid #C7FFD8;\n"
                                      "border-radius: 8px;\n"
                                      "padding: 5px;\n"
                                      "background-color:#BFFFFE;\n"
                                      "color:#161D6F;\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "background-color:#C7FFD8;\n"
                                      "border: 1px solid #98DED9;\n"
                                      "}\n"
                                      "QPushButton:pressed {\n"
                                      "background-color:#161D6F;\n"
                                      "color:#98DED9;\n"
                                      "}")
        self.pushButton.setText("")
        self.pushButton.clicked.connect(self.open_image)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/images/arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(50, 50))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.delete = QtWidgets.QPushButton(self.Form)
        self.delete.setStyleSheet("QPushButton{\n"
                                  "border: 1px solid #C7FFD8;\n"
                                  "border-radius: 8px;\n"
                                  "padding: 5px;\n"
                                  "background-color:#BFFFFE;\n"
                                  "color:#161D6F;\n"
                                  "}\n"
                                  "QPushButton:hover{\n"
                                  "background-color:#C7FFD8;\n"
                                  "border: 1px solid #98DED9;\n"
                                  "}\n"
                                  "QPushButton:pressed {\n"
                                  "background-color:#161D6F;\n"
                                  "color:#98DED9;\n"
                                  "}")
        self.delete.setText("")
        self.delete.clicked.connect(self.delete_fnc)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assets/images/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete.setIcon(icon1)
        self.delete.setIconSize(QtCore.QSize(50, 50))
        self.delete.setObjectName("delete")
        self.horizontalLayout.addWidget(self.delete)
        self.image_label.setText(self.image_name)
        self.Form.mousePressEvent = self.widget_selected
        return self.Form

    def delete_fnc(self):
        # Iterate through image list and finds widget
        for i in ui.image_list:
            if i.widget_id == self.widget_id:
                ui.image_list.remove(i)
        # Removes Widget
        self.Form.deleteLater()

    def open_image(self):
        # Opens Image
        img = Image.open(self.image)
        img.show()

    def widget_selected(self, event):
        # Getting Data
        data_dict = {}

        img_data = self.pil_img.getexif()
        for tag_id in img_data:
            # get the tag name, instead of human unreadable tag id
            tag = TAGS.get(tag_id, tag_id)
            data = img_data.get(tag_id)
            # decode bytes

            data_dict[tag] = data
        print(data_dict)
        # Getting Date Data
        try:
            date_time = data_dict["DateTime"]
        except KeyError:
            date = "0000-00-00"
        else:
            date = date_time.split()[0]
            date = date.split(":")
            final_date = ""
            for d in date[:-1]:
                final_date += f"{d}-"
            final_date += date[-1]
            date = final_date
        # Updating DateLabel
        self.date_label.setText(date)

        # Getting Image Size
        space = os.path.getsize(self.image)
        self.space_label.setText(size(space, system=alternative))

        # Getting Image Format
        self.format_label.setText(self.pil_img.format)

        # Getting Color Space of Image
        exif = self.pil_img.getexif() or {}
        if exif.get(0xA001) == 1 or exif.get(0x0001) == 'R98':
            self.color_label.setText('sRGB')
        elif exif.get(0xA001) == 2 or exif.get(0x0001) == 'R03':
            self.color_label.setText('AdobeRGB')
        elif exif.get(0xA001) is None and exif.get(0x0001) is None:
            self.color_label.setText('----')
        else:
            self.color_label.setText('----')

        # Updating Resolution Field
        self.width_input.setText(str(self.img_width))
        self.height_input.setText(str(self.img_height))

