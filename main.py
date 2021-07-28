from PyQt5 import QtWidgets, QtGui
import ui
import sys


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    # Loading Fonts from assets
    QtGui.QFontDatabase.addApplicationFont('assets/Poppins/Poppins-Bold.ttf')
    QtGui.QFontDatabase.addApplicationFont('assets/Poppins/Poppins-Black.ttf')
    QtGui.QFontDatabase.addApplicationFont('assets/Poppins/Poppins-SemiBold.ttf')
    QtGui.QFontDatabase.addApplicationFont('assets/Poppins/Poppins-Regular.ttf')
    QtGui.QFontDatabase.addApplicationFont('assets/Poppins/Poppins-Medium.ttf')

    ui = ui.Ui_MainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
