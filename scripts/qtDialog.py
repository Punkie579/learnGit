import sys
from PySide2 import QtCore, QtWidgets

print("This is PySide2 program!")

class StandaloneWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Standalone Window")
        self.setFixedSize(300, 400)

        self.createWidgets()
        self.createLayouts()
        self.createConnections()

    def createWidgets(self):
        self.close_button = QtWidgets.QPushButton("Close")


    def createLayouts(self):
        main_layout = QtWidgets.QHBoxLayout(self)
        main_layout.addWidget(self.close_button)

    def createConnections(self):
        self.close_button.clicked.connect(self.close)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = StandaloneWindow()
    window.show()

    app.exec_()

    print("Jens")