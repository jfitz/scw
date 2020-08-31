import sys
import argparse
from PyQt5.QtWidgets import (
    QDesktopWidget,
    QApplication,
    QWidget,
    QPushButton,
    QVBoxLayout,
    QLabel,
    QScrollArea
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

    return window

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Load image, select region, and convert to text.')
    parser.add_argument('inputfile')

    args = parser.parse_args()

    app = QApplication([])
    window = make_window(args.inputfile)
    window.setWindowTitle('Select and OCR')
    window.show()

    # exit and pass exit code from Qt application
    exit_code = app.exec_()
    sys.exit(exit_code)

