from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from ui import Ui_MainWindow
import os

class EasyEditor(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.workdir = None
        self.filename = None
        self.connects()

    def connects(self):
        self.ui.folder_btn.clicked.connect(self.choose_folder)
        # self.ui.action.triggered.connect(self.choose_folder)

    def filter(self, filenames):
        images = []
        for filename in filenames:
            if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
                images.append(filename)

        return images

    def show_image_list(self):
        filenames = os.listdir(self.workdir)
        self.ui.image_list.clear()
        images = self.filter(filenames)
        self.ui.image_list.addItems(images)

    def choose_folder(self):
        try:
            self.workdir = QFileDialog.getExistingDirectory()
            self.show_image_list()
        except:
            pass





app = QApplication([])
ex = EasyEditor()
ex.show()
app.exec_()
