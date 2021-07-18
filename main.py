from PyQt5 import QtWidgets
import ui
import sys


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ui.Ui_MainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
