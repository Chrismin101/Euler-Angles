import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider, QVBoxLayout, QWidget, QOpenGLWidget, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QSurfaceFormat
from scipy.spatial.transform import Rotation as R

import OpenGL.GL as GL
from OpenGL import GLU
import numpy as np


class GLWidget(QOpenGLWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.rotX: float = 0.0
        self.rotY: float = 0.0
        self.rotZ: float = 0.0
        self.quad: GLU = GLU.gluNewQuadric()
        self.rings = self.create_rings()  # create 3 rings

    def initializeGL(self):
        print("init_gl called")
        GL.glClearColor(0.0, 0.0, 0.0, 1.0)
        GL.glEnable(GL.GL_DEPTH_TEST)

    def setRotX(self, val: float) -> None:
        self.rotX = val
        self.update()

    def setRotY(self, val: float) -> None:
        self.rotY = val
        self.update()

    def setRotZ(self, val: float) -> None:
        self.rotZ = val
        self.update()

    def resizeGL(self, height: int, width: int) -> None:
        print("resize_gl called")
        GL.glViewport(0, 0, width, height)
        GL.glMatrixMode(GL.GL_PROJECTION)
        GL.glLoadIdentity()
        aspect_ratio: float = width / float(height)
        GLU.gluPerspective(45.0, aspect_ratio, 1.0, 100.0)
        GL.glMatrixMode(GL.GL_MODELVIEW)

    def paintGL(self) -> None:
        print(f"rotX: {self.rotX}, rotY: {self.rotY}, rotZ: {self.rotZ}")  # Debugging print
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)

        GL.glPushMatrix()
        GL.glTranslate(0.0, 0.0, -80.0)
        GL.glScale(20.0, 20.0, 0.0)

        GL.glPushMatrix()
        GL.glRotate(self.rotX, 1.0, 0.0, 0.0)
        GL.glColor3f(1.0, 0.0, 0.0)
        self.draw_ring()
        GL.glPopMatrix()

        GL.glPushMatrix()
        GL.glRotate(self.rotY, 0.0, 1.0, 0.0)
        GL.glColor3f(0.0, 1.0, 0.0)
        self.draw_ring()
        GL.glPopMatrix()

        GL.glPushMatrix()
        GL.glRotate(self.rotZ, 0.0, 0.0, 1.0)
        GL.glColor3f(0.0, 0.0, 1.0)
        self.draw_ring()
        GL.glPopMatrix()

        GL.glPopMatrix()

    def draw_ring(self) -> None:
        slices = 50
        stacks = 10

        # Draw a cylinder that represents a ring
        quadric = GLU.gluNewQuadric()
        GLU.gluDisk(quadric, 0.90, 1.0, slices, stacks)

    def create_rings(self) -> list:
        # Create three rings for x, y, and z axes
        rings = {
            "x": self.create_ring(1.0, 0.5),
            "y": self.create_ring(0.5, 1.0),
            "z": self.create_ring(1.0, 1.0)
        }
        return rings

    @staticmethod
    def create_ring(inner_radius: float, outer_radius: float):
        # Creates a ring object using GLU quadric
        ring = GLU.gluNewQuadric()
        GLU.gluQuadricDrawStyle(ring, GLU.GLU_LINE)
        return {
            "inner_radius": inner_radius,
            "outer_radius": outer_radius,
            "ring": ring
        }



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("3D Ring Control")
        self.setGeometry(100, 100, 800, 600)

        self.gl_widget = GLWidget(self)
        self.gl_widget.setFixedSize(600, 600)

        # Layout to hold the OpenGL widget and the sliders
        layout = QVBoxLayout()

        # Add OpenGL widget
        layout.addWidget(self.gl_widget)

        # X-axis rotation control slider
        self.sliderX = QSlider(Qt.Horizontal)
        self.sliderX.setRange(-180, 180)
        self.sliderX.setValue(0)
        self.sliderX.setTickInterval(10)
        self.sliderX.setTickPosition(QSlider.TicksBelow)
        self.sliderX.valueChanged.connect(self.update_rotX)

        # Y-axis rotation control slider
        self.sliderY = QSlider(Qt.Horizontal)
        self.sliderY.setRange(-180, 180)
        self.sliderY.setValue(0)
        self.sliderY.setTickInterval(10)
        self.sliderY.setTickPosition(QSlider.TicksBelow)
        self.sliderY.valueChanged.connect(self.update_rotY)

        # Z-axis rotation control slider
        self.sliderZ = QSlider(Qt.Horizontal)
        self.sliderZ.setRange(-180, 180)
        self.sliderZ.setValue(0)
        self.sliderZ.setTickInterval(10)
        self.sliderZ.setTickPosition(QSlider.TicksBelow)
        self.sliderZ.valueChanged.connect(self.update_rotZ)

        layout.addWidget(QLabel("Rotate X-axis"))
        layout.addWidget(self.sliderX)
        layout.addWidget(QLabel("Rotate Y-axis"))
        layout.addWidget(self.sliderY)
        layout.addWidget(QLabel("Rotate Z-axis"))
        layout.addWidget(self.sliderZ)

        # Central widget for the window
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def update_rotX(self, value: int):
        self.gl_widget.setRotX(value)

    def update_rotY(self, value: int):
        self.gl_widget.setRotY(value)

    def update_rotZ(self, value: int):
        self.gl_widget.setRotZ(value)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()