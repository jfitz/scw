import sys
import argparse
from PyQt5.QtWidgets import (
    QApplication,
    QDesktopWidget,
    QLabel,
    QMainWindow,
    QPushButton,
    QScrollArea,
    QVBoxLayout,
    QWidget
)
from PyQt5.QtGui import QIcon, QPixmap, QPalette


def make_window(filename):
    desktop = QDesktopWidget()
    avail_geom = desktop.availableGeometry()
    desk_width = avail_geom.width()
    desk_height = avail_geom.height()
    print('desktop: ' + str(desk_height) + 'x' + str(desk_width))

    pixmap = QPixmap(filename)
    pixmap_height = pixmap.height()
    pixmap_width = pixmap.width()

    print('pixmap: ' + str(pixmap_height) + 'x' + str(pixmap_width))

    window = QWidget()
    layout = QVBoxLayout()

    label = QLabel()
    label.setPixmap(pixmap)
    scrollArea = QScrollArea()
    scrollArea.setBackgroundRole(QPalette.Dark)
    scrollArea.setWidget(label)
    layout.addWidget(scrollArea)

    layout.addWidget(QPushButton('Top'))
    layout.addWidget(QPushButton('Bottom'))

    window.setLayout(layout)

    window_height = window.height()
    window_width = window.width()

    window_top = int(desk_height * 0.1)
    window_left = int(desk_width * 0.1)

    print('window: ' + str(window_height) + 'x' + str(window_width))

    if pixmap_height > desk_height * 0.8:
        window_height = int(desk_height * 0.8)

    if pixmap_width > desk_width * 0.8:
        window_width = int(desk_width * 0.8)

    # window_height = int(pixmap_height * 0.9)
    # window_width = int(pixmap_width * 0.9)
    print('window: ' + str(window_height) + 'x' + str(window_width))

    window.setGeometry(window_left, window_top, window_width, window_height)


class ScwWindow(QMainWindow):

    def __init__(self, filename):
        super().__init__()

        self.initUI(filename)

    def initUI(self, filename):
        desktop = QDesktopWidget()
        avail_geom = desktop.availableGeometry()
        desk_width = avail_geom.width()
        desk_height = avail_geom.height()
        print('desktop: ' + str(desk_height) + 'x' + str(desk_width))

        pixmap = QPixmap(filename)
        pixmap_height = pixmap.height()
        pixmap_width = pixmap.width()

        print('pixmap: ' + str(pixmap_height) + 'x' + str(pixmap_width))

        label = QLabel()
        label.setPixmap(pixmap)
        scrollArea = QScrollArea()
        scrollArea.setBackgroundRole(QPalette.Dark)
        scrollArea.setWidget(label)

        self.setCentralWidget(scrollArea)

        self.statusBar().showMessage('Ready')

        window_height = self.height()
        window_width = self.width()

        window_top = int(desk_height * 0.1)
        window_left = int(desk_width * 0.1)

        print('window: ' + str(window_height) + 'x' + str(window_width))

        if pixmap_height > desk_height * 0.8:
            window_height = int(desk_height * 0.8)

        if pixmap_width > desk_width * 0.8:
            window_width = int(desk_width * 0.8)

        # window_height = int(pixmap_height * 0.9)
        # window_width = int(pixmap_width * 0.9)
        print('window: ' + str(window_height) + 'x' + str(window_width))

        self.setGeometry(window_left, window_top, window_width, window_height)

        # self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Statusbar')
        self.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Load image, select region, and convert to text.')

    parser.add_argument('inputfile')

    args = parser.parse_args()

    app = QApplication([])
    ex = ScwWindow(args.inputfile)

    # exit and pass exit code from Qt application
    exit_code = app.exec_()
    sys.exit(exit_code)
