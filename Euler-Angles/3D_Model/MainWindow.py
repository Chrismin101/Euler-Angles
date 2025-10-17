try:
    from collections.abc import Mapping
except ImportError:
    from collections import Mapping
import GLWidget
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QSlider


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('beans')
        self.height: int = 300
        self.width: int = 300
        self.resize(self.width, self.height)
        self.gl_widget: GLWidget = GLWidget.GLWidget(self)
        self.initGUI()

        timer: QTimer = QTimer(self)
        timer.setInterval(20)  # 20 milli-sec
        # THIS IS OUR EVENT it calls PAINT-GL ever 20 ms
        timer.timeout.connect(self.gl_widget.update)
        timer.start()

    def initGUI(self) -> None:
        central_widget: QWidget = QWidget()
        gui_layout: QVBoxLayout = QVBoxLayout()
        central_widget.setLayout(gui_layout)

        # opengl widget
        gui_layout.addWidget(self.gl_widget)

        # sliders
        sliderX: QSlider = QSlider(Qt.Horizontal)
        sliderX.setRange(0, 360)
        sliderX.valueChanged.connect(lambda val: self.gl_widget.setRotX(val))

        sliderY: QSlider = QSlider(Qt.Horizontal)
        sliderY.setRange(0, 360)
        sliderY.valueChanged.connect(lambda val: self.gl_widget.setRotY(val))

        sliderZ: QSlider = QSlider(Qt.Horizontal)
        sliderZ.setRange(0, 360)
        sliderZ.valueChanged.connect(lambda val: self.gl_widget.setRotZ(val))

        gui_layout.addWidget(sliderX)
        gui_layout.addWidget(sliderY)
        gui_layout.addWidget(sliderZ)

        self.setCentralWidget(central_widget)
