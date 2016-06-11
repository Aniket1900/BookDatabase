from PyQt5 import QtCore, QtWidgets, uic
import sys


class BookDatabase(QtWidgets.QApplication):
    def __init__(self, *args, **kwargs):
        super(BookDatabase, self).__init__(*args)
        self.main_window = MainWindow()
        self.main_window.show()

class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        uic.loadUi('Views/Main.ui', self)

def main():
    app = BookDatabase(sys.argv)
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
