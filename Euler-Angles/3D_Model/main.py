import MainWindow
from PyQt5.QtWidgets import QApplication
import sys


# READ GITHUB HISTORY COMMITS
if __name__ == '__main__':

    app: QApplication = QApplication(sys.argv)
    win: MainWindow = MainWindow.MainWindow()
    win.show()
    sys.exit(app.exec_())
    # this need to commit
