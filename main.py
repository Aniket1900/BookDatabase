from PyQt5 import QtCore, QtWidgets, uic
import sys

from ViewModel.Main import MainWindow

class BookDatabase(QtWidgets.QApplication):
    def __init__(self, *args, **kwargs):
        super(BookDatabase, self).__init__(*args)
        self.main_window = MainWindow()
        self.main_window.show()

def main():
    app = BookDatabase(sys.argv)
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
