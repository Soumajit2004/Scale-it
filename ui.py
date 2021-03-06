from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from custom_widget import ImageWidget, Ui_pogress_widget
from brain import Brain

image_list = []
widget_selected = 1


class Ui_MainWindow(object):

    def __init__(self, MainWindow):
        # Initializing File Selector
        self.file_selector = QtWidgets.QFileDialog()

        # Initializing main UI Selector
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 720)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/images/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color:#F6F6F6;")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 80))
        self.frame.setStyleSheet("QFrame{\n"
                                 "border:1px solid #98DED9;\n"
                                 "border-bottom:0px;\n"
                                 "}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(30, -1, 30, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 10))
        font = QtGui.QFont()
        font.setFamily("Poppins SemiBold")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
                                 "border: 0px;\n"
                                 "color:#161D6F;\n"
                                 "}")
        self.label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(549, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.add_image = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Poppins SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.add_image.setFont(font)
        self.add_image.setStyleSheet("QPushButton{\n"
                                     "border: 1px solid #C7FFD8;\n"
                                     "border-radius: 8px;\n"
                                     "padding:3px 15px;\n"
                                     "background-color:#98DED9;\n"
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assets/images/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_image.setIcon(icon1)
        self.add_image.setIconSize(QtCore.QSize(30, 30))
        self.add_image.setFlat(False)
        self.add_image.setObjectName("add_image")
        self.horizontalLayout_2.addWidget(self.add_image)
        self.convert = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Poppins SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.convert.setFont(font)
        self.convert.setStyleSheet("QPushButton{\n"
                                   "border: 1px solid #C7FFD8;\n"
                                   "border-radius: 8px;\n"
                                   "padding:3px 15px;\n"
                                   "background-color:#98DED9;\n"
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
        self.convert.setFlat(False)
        self.convert.setObjectName("convert")
        self.horizontalLayout_2.addWidget(self.convert)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QtCore.QSize(400, 0))
        self.frame_3.setStyleSheet("QFrame{\n"
                                   "border:1px solid #98DED9;\n"
                                   "}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 150))
        self.frame_5.setStyleSheet("QFrame{\n"
                                   "border:1px solid #C7FFD8;\n"
                                   "border-radius:8px;\n"
                                   "background-color:#98DED9;\n"
                                   "color:#161D6F;\n"
                                   "}")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Poppins SemiBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{\n"
                                   "color:#161D6F;\n"
                                   "border:0px;\n"
                                   "}")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.frame_7 = QtWidgets.QFrame(self.frame_5)
        self.frame_7.setStyleSheet("QFrame{\n"
                                   "border:0px;\n"
                                   "}")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setContentsMargins(10, -1, 10, -1)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.img_width = QtWidgets.QLineEdit(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_width.sizePolicy().hasHeightForWidth())
        self.img_width.setSizePolicy(sizePolicy)
        self.img_width.setMinimumSize(QtCore.QSize(50, 0))
        self.img_width.setMaximumSize(QtCore.QSize(130, 16777215))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(16)
        self.img_width.setFont(font)
        self.img_width.setAcceptDrops(False)
        self.img_width.setAutoFillBackground(False)
        self.img_width.setStyleSheet("QLineEdit{\n"
                                     "padding: 2px;\n"
                                     "border: 1px solid #BFFFFE;\n"
                                     "border-radius:8px;\n"
                                     "background-color: #BFFFFE;\n"
                                     "color: #161D6F;\n"
                                     "}")
        self.img_width.setInputMask("")
        self.img_width.setText("")
        self.img_width.setMaxLength(4)
        self.img_width.setAlignment(QtCore.Qt.AlignCenter)
        self.img_width.setReadOnly(False)
        self.img_width.setObjectName("img_width")
        self.horizontalLayout_3.addWidget(self.img_width)
        self.label_3 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("Poppins SemiBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel{\n"
                                   "border: 0px;\n"
                                   "color:#161D6F;\n"
                                   "}")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.img_height = QtWidgets.QLineEdit(self.frame_7)
        self.img_height.setMaximumSize(QtCore.QSize(130, 16777215))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(16)
        self.img_height.setFont(font)
        self.img_height.setAcceptDrops(False)
        self.img_height.setStyleSheet("QLineEdit{\n"
                                      "padding: 2px;\n"
                                      "border: 1px solid #BFFFFE;\n"
                                      "border-radius:8px;\n"
                                      "background-color: #BFFFFE;\n"
                                      "color: #161D6F;\n"
                                      "}")
        self.img_height.setMaxLength(4)
        self.img_height.setAlignment(QtCore.Qt.AlignCenter)
        self.img_height.setReadOnly(False)
        self.img_height.setObjectName("img_height")
        self.horizontalLayout_3.addWidget(self.img_height)
        self.verticalLayout_3.addWidget(self.frame_7)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.frame_12 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy)
        self.frame_12.setMinimumSize(QtCore.QSize(0, 150))
        self.frame_12.setStyleSheet("QFrame{\n"
                                    "border:1px solid #C7FFD8;\n"
                                    "border-radius:8px;\n"
                                    "background-color:#98DED9;\n"
                                    "color:#161D6F;\n"
                                    "}")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_6 = QtWidgets.QLabel(self.frame_12)
        font = QtGui.QFont()
        font.setFamily("Poppins SemiBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("QLabel{\n"
                                   "color:#161D6F;\n"
                                   "border:0px;\n"
                                   "}")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_8.addWidget(self.label_6)
        self.frame_13 = QtWidgets.QFrame(self.frame_12)
        self.frame_13.setStyleSheet("QFrame{\n"
                                    "border:0px;\n"
                                    "}")
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.saving_pathfield = QtWidgets.QLineEdit(self.frame_13)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        self.saving_pathfield.setFont(font)
        self.saving_pathfield.setStyleSheet("QLineEdit{\n"
                                            "padding: 2px;\n"
                                            "border: 1px solid #BFFFFE;\n"
                                            "border-radius:8px;\n"
                                            "background-color: #BFFFFE;\n"
                                            "color: #161D6F;\n"
                                            "}")
        self.saving_pathfield.setObjectName("saving_pathfield")
        self.horizontalLayout_7.addWidget(self.saving_pathfield)
        self.save_path = QtWidgets.QPushButton(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_path.sizePolicy().hasHeightForWidth())
        self.save_path.setSizePolicy(sizePolicy)
        self.save_path.setMinimumSize(QtCore.QSize(10, 0))
        self.save_path.setMaximumSize(QtCore.QSize(34, 34))
        self.save_path.setStyleSheet("QPushButton{\n"
                                     "border: 1px solid #C7FFD8;\n"
                                     "border-radius: 4px;\n"
                                     "padding:1px;\n"
                                     "background-color:#98DED9;\n"
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
        self.save_path.setObjectName("save_path")
        self.horizontalLayout_7.addWidget(self.save_path)
        self.verticalLayout_8.addWidget(self.frame_13)
        self.verticalLayout_2.addWidget(self.frame_12)
        self.frame_6 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_6.setStyleSheet("QFrame{\n"
                                   "border:1px solid #C7FFD8;\n"
                                   "border-radius:8px;\n"
                                   "background-color:#98DED9;\n"
                                   "color:#161D6F;\n"
                                   "}")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Poppins SemiBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("border:0px;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.scrollArea = QtWidgets.QScrollArea(self.frame_6)
        self.scrollArea.setStyleSheet("backgriund-color:#98DED9;\n"
                                      "border:0px;")
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 325, 458))
        self.scrollAreaWidgetContents.setStyleSheet("background-color:#98DED9;\n"
                                                    "border:0px;")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_8 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_8.setMinimumSize(QtCore.QSize(0, 80))
        self.frame_8.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_8.setStyleSheet("QFrame{\n"
                                   "padding: 2px;\n"
                                   "border: 1px solid #BFFFFE;\n"
                                   "border-radius:8px;\n"
                                   "background-color: #BFFFFE;\n"
                                   "}")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(26)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        spacerItem1 = QtWidgets.QSpacerItem(109, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.img_size = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(26)
        self.img_size.setFont(font)
        self.img_size.setAlignment(QtCore.Qt.AlignCenter)
        self.img_size.setObjectName("img_size")
        self.horizontalLayout_4.addWidget(self.img_size)
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(12)
        self.verticalLayout_5.addWidget(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_9.setMinimumSize(QtCore.QSize(0, 80))
        self.frame_9.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_9.setStyleSheet("QFrame{\n"
                                   "padding: 2px;\n"
                                   "border: 1px solid #BFFFFE;\n"
                                   "border-radius:8px;\n"
                                   "background-color: #BFFFFE;\n"
                                   "}")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_8 = QtWidgets.QLabel(self.frame_9)
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(26)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        spacerItem2 = QtWidgets.QSpacerItem(49, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.img_color = QtWidgets.QLabel(self.frame_9)
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(26)
        self.img_color.setFont(font)
        self.img_color.setObjectName("img_color")
        self.horizontalLayout_5.addWidget(self.img_color)
        self.verticalLayout_5.addWidget(self.frame_9)
        self.frame_10 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_10.setMinimumSize(QtCore.QSize(0, 80))
        self.frame_10.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_10.setStyleSheet("QFrame{\n"
                                    "padding: 2px;\n"
                                    "border: 1px solid #BFFFFE;\n"
                                    "border-radius:8px;\n"
                                    "background-color: #BFFFFE;\n"
                                    "}")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_10 = QtWidgets.QLabel(self.frame_10)
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(26)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_6.addWidget(self.label_10)
        spacerItem3 = QtWidgets.QSpacerItem(14, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.img_format = QtWidgets.QLabel(self.frame_10)
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(26)
        self.img_format.setFont(font)
        self.img_format.setObjectName("img_format")
        self.horizontalLayout_6.addWidget(self.img_format)
        self.verticalLayout_5.addWidget(self.frame_10)
        self.frame_11 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_11.setMinimumSize(QtCore.QSize(0, 160))
        self.frame_11.setMaximumSize(QtCore.QSize(16777215, 160))
        self.frame_11.setStyleSheet("QFrame{\n"
                                    "padding: 2px;\n"
                                    "border: 1px solid #BFFFFE;\n"
                                    "border-radius:8px;\n"
                                    "background-color: #BFFFFE;\n"
                                    "}")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_12 = QtWidgets.QLabel(self.frame_11)
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_6.addWidget(self.label_12)
        self.img_date = QtWidgets.QLabel(self.frame_11)
        font = QtGui.QFont()
        font.setFamily("Poppins Light")
        font.setPointSize(26)
        self.img_date.setFont(font)
        self.img_date.setAlignment(QtCore.Qt.AlignCenter)
        self.img_date.setObjectName("img_date")
        self.verticalLayout_6.addWidget(self.img_date)
        self.verticalLayout_5.addWidget(self.frame_11)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem4)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_4.addWidget(self.scrollArea)
        self.verticalLayout_2.addWidget(self.frame_6)
        self.horizontalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setStyleSheet("QFrame{\n"
                                   "border:1px solid #98DED9;\n"
                                   "border-left:0px;\n"
                                   "}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setLineWidth(1)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.frame_4)
        self.scrollArea_2.setMinimumSize(QtCore.QSize(750, 540))
        self.scrollArea_2.setStyleSheet("border:0px;")
        self.scrollArea_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 676, 636))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.gallery = QtWidgets.QVBoxLayout()
        self.gallery.setContentsMargins(20, 20, 20, 20)
        self.gallery.setSpacing(15)
        self.gallery.setAlignment(QtCore.Qt.AlignTop)
        self.gallery.setObjectName("gallery")
        self.verticalLayout_9.addLayout(self.gallery)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_7.addWidget(self.scrollArea_2)
        self.horizontalLayout.addWidget(self.frame_4)
        self.verticalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)

        # ----------------------------------- My Code ------------------------------------------------------------

        # Initializing Brain class
        self.brain = Brain(self.warning_shower)

        # Connecting Buttons
        self.add_image.clicked.connect(self.add_image_fnc)
        self.convert.clicked.connect(self.convert_fnc)
        self.img_width.textChanged.connect(self.change_width)
        self.img_height.textChanged.connect(self.change_height)
        self.saving_pathfield.textChanged.connect(self.change_saving_path)
        self.save_path.clicked.connect(self.choose_saving_path)

        # ----------------------------------- My code ------------------------------------------------------------

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Scale It"))
        self.label.setText(_translate("MainWindow", "Scale It"))
        self.add_image.setText(_translate("MainWindow", "Add Image"))
        self.convert.setText(_translate("MainWindow", "Convert"))
        self.label_2.setText(_translate("MainWindow", "Resolution"))
        self.img_width.setPlaceholderText(_translate("MainWindow", "Width"))
        self.label_3.setText(_translate("MainWindow", "X"))
        self.img_height.setPlaceholderText(_translate("MainWindow", "Height"))
        self.label_6.setText(_translate("MainWindow", "Saving Path"))
        self.saving_pathfield.setPlaceholderText(_translate("MainWindow", "Enter Saving Path"))
        self.save_path.setText(_translate("MainWindow", "..."))
        self.label_4.setText(_translate("MainWindow", "Details"))
        self.label_5.setText(_translate("MainWindow", "Size:"))
        self.img_size.setText(_translate("MainWindow", "--"))
        self.label_8.setText(_translate("MainWindow", "Color:"))
        self.img_color.setText(_translate("MainWindow", "----"))
        self.label_10.setText(_translate("MainWindow", "Formart:"))
        self.img_format.setText(_translate("MainWindow", "---"))
        self.label_12.setText(_translate("MainWindow", "Date Created"))
        self.img_date.setText(_translate("MainWindow", "0000-00-00"))

    # ------------------------------------------ My Functions --------------------------------------------------------

    def warning_shower(self, text):
        """Shows Warnings with the text inputted"""
        # Showing Warning
        QtWidgets.QMessageBox.warning(self.frame_2, "Scale-it", text)

    def add_image_fnc(self):
        """Add Custom Image Widget to the ui and image instance on image list"""

        # Getting Filename
        img_path = self.file_selector.getOpenFileName(caption='Select Image',
                                                      filter="Image files (*.jpg *.png *.jpeg)")[0]

        # Checking for null img_path
        if img_path:
            try:
                # Create Widget
                image_widget_class = ImageWidget(image_path=img_path, widget_id=len(image_list) + 1,
                                                 date_label=self.img_date, space_label=self.img_size,
                                                 format_label=self.img_format, color_label=self.img_color,
                                                 width_input=self.img_width, height_input=self.img_height,
                                                 save_input=self.saving_pathfield)

                # Adding to Image list
                image_list.append(image_widget_class)
                print(image_list)

                # Build Custom Widget
                widget = image_widget_class.setup()
                self.gallery.addWidget(widget)

            except FileNotFoundError:
                print("Invalid Image Path")

    def convert_fnc(self):
        """ This function converts all image instance on image_list using Brain class"""

        # Converting Image
        for i in image_list:
            # Progress Popup
            progress_dialoge = QtWidgets.QDialog(self.frame_2)
            progress_dialoge.setMinimumWidth(400)
            progress_layout = Ui_pogress_widget()
            progress_dialoge.setLayout(progress_layout.setupUi())
            progress_layout.p_name.setText(i.image_name)
            progress_dialoge.setWindowTitle("Scale-it")
            progress_dialoge.show()
            QApplication.processEvents()

            # Calling brain on image instance
            self.brain.run(i, progress_layout)

            # Deleting progressbar after task finished
            progress_dialoge.deleteLater()

        # Showing Warning if no image selected
        if len(image_list) == 0:
            self.warning_shower("Please add images to continue.")

    def change_width(self):
        """Detecting if the user changed width of a image"""

        if widget_selected != 0:

            for i in image_list:
                if i.widget_id == widget_selected:
                    i.img_width = self.img_width.text()

    def change_height(self):
        """Detecting if the user changed height of a image"""

        if widget_selected != 0:

            for i in image_list:
                if i.widget_id == widget_selected:
                    i.img_height = self.img_height.text()

    def change_saving_path(self):
        """Detecting if the user changed saving path of a image"""

        if widget_selected != 0:

            for i in image_list:
                if i.widget_id == widget_selected:
                    i.saving_path = self.saving_pathfield.text()

    def choose_saving_path(self):
        """Detecting if the user browsed and changed saving path of a image"""

        if widget_selected != 0:
            save_path = self.file_selector.getSaveFileName(caption='Save Image',
                                                           filter="Image files (*.jpg *.png *.jpeg)")[0]
            if save_path != "":
                for i in image_list:
                    if i.widget_id == widget_selected:
                        i.saving_path = save_path
                        self.saving_pathfield.setText(i.saving_path)
