import sys
from time import sleep
from os.path import join, dirname, abspath, basename, isdir
from os import listdir

from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Slot, QThread, Signal, QFile
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTreeWidgetItem

import c9_qt_modern.styles
import c9_qt_modern.windows

from ui_mainwindow import Ui_MainWindow

# _UI = join(dirname(abspath(__file__)), 'mainwindow.ui')


class ProgressThread(QThread):
    update = Signal(int)

    def run(self):
        progress = 20
        while True:
            progress += 1
            if progress == 100:
                progress = 0

            self.update.emit(progress)
            sleep(0.5)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.tooltiplabel.setToolTip("This is a tool tip that shows a tip about the tool")

        self.ui.actionLight.triggered.connect(self.lightTheme)
        self.ui.actionDark.triggered.connect(self.darkTheme)

        self.thread = ProgressThread()
        self.thread.update.connect(self.update_progress)
        self.thread.start()

        self.load_project_structure(dirname(dirname(abspath(__file__))), self.ui.treeWidget)

        for i in range(100):
            self.ui.comboBox_2.addItem("item {}".format(i))

    def load_project_structure(self, startpath, tree):
        for element in listdir(startpath):
            path_info = startpath + "/" + element
            parent_itm = QTreeWidgetItem(tree, [basename(element)])
            if isdir(path_info):
                self.load_project_structure(path_info, parent_itm)

    def update_progress(self, progress):
        self.ui.progressBar.setValue(progress)

    def lightTheme(self):
        c9_qt_modern.styles.light(QApplication.instance())

    def darkTheme(self):
        c9_qt_modern.styles.dark(QApplication.instance())

    @Slot()
    def on_pushButton_clicked(self):
        self.close()

    @Slot()
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Exit', 'Do you want to exit?')

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    c9_qt_modern.styles.dark(app)
    mw = c9_qt_modern.windows.ModernWindow(MainWindow())
    mw.show()

    sys.exit(app.exec())
