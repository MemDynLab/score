import cv2
import numpy as np

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets

import logging

logger = logging.getLogger(__name__)


class OpenCVQImage(QtGui.QImage):
    def __init__(self, opencv_bgr_img):

        h, w, n_channels = opencv_bgr_img.shape
        depth = opencv_bgr_img.dtype
        if depth != np.uint8 or n_channels != 3:
            raise ValueError("the input image must be 8-bit, 3-channel")

        # it's assumed the image is in BGR format
        opencv_rgb_img = cv2.cvtColor(opencv_bgr_img, cv2.COLOR_BGR2RGB)
        self._imgData = opencv_rgb_img.tostring()
        super(OpenCVQImage, self).__init__(self._imgData, w, h,
                                           QtGui.QImage.Format_RGB888)


class CVVideoWidget(QtWidgets.QWidget):
    new_frame = QtCore.pyqtSignal(np.ndarray, name="CameraWidget.new_frame")
    key_action = QtCore.pyqtSignal(str, name="CameraWidget.key_action")
    mouse_press_action_signal = QtCore.pyqtSignal(int, int, name="CameraWidget.mouse_press_action_signal")
    mouse_move_action_signal = QtCore.pyqtSignal(int, int, name="CameraWidget.mouse_move_action_signal")
    mouse_release_action_signal = QtCore.pyqtSignal(int, int, name="CameraWidget.mouse_release_action_signal")

    def __init__(self, parent=None, flags=None):
        if flags:
            flags_ = flags
        else:
            # noinspection PyUnresolvedReferences
            flags_ = QtCore.Qt.WindowFlags()
        super(CVVideoWidget, self).__init__(parent, flags=flags_)
        self._camera_device = None
        self._frame = None
        self.setMinimumSize(640, 480)
        self.setMaximumSize(640, 480)

    def set_device(self, camera_device):
        if camera_device:
            self._camera_device = camera_device
            self._camera_device.new_frame.connect(self._on_new_frame)
            self._camera_device.size_changed_signal.connect(self.size_changed)
            self.updateGeometry()

    @QtCore.pyqtSlot()
    def size_changed(self):
        w, h = self._camera_device.display_frame_size
        self.setMinimumSize(w, h)
        self.setMaximumSize(w, h)
        self.resize(w, h)
        self.updateGeometry()

    def sizeHint(self):
        if self._camera_device:
            try:
                w, h = self._camera_device.display_frame_size
                return QtCore.QSize(w, h)
            except AttributeError:
                logger.debug("display frame size calculation failed, camera device {}".format(self._camera_device))
                return QtCore.QSize(800, 600)
        else:
            return QtCore.QSize(800, 600)

    @QtCore.pyqtSlot(np.ndarray)
    def _on_new_frame(self, frame):
        self._frame = frame.copy()
        self.new_frame.emit(self._frame)
        self.update()

    def changeEvent(self, e):
        if self._camera_device is not None and e.type() == QtCore.QEvent.EnabledChange:
            if self.isEnabled():
                self._camera_device.new_frame.connect(self._on_new_frame)
            else:
                self._camera_device.new_frame.disconnect(self._on_new_frame)

    def paintEvent(self, e):
        if self._frame is None:
            painter = QtGui.QPainter(self)
            painter.fillRect(self.rect(), QtCore.Qt.darkGray)
            return
        painter = QtGui.QPainter(self)
        painter.drawImage(QtCore.QPoint(0, 0), OpenCVQImage(self._frame))

    def mousePressEvent(self, a0: QtGui.QMouseEvent):
        self.mouse_press_action_signal.emit(a0.x(), a0.y())

    def mouseMoveEvent(self, a0: QtGui.QMouseEvent):
        if self.rect().contains(a0.pos()):
            self.mouse_move_action_signal.emit(a0.x(), a0.y())
        else:
            # code -1, -1 emitted when the mouse is dragged outside of the widget
            self.mouse_move_action_signal.emit(-1, -1)

    def mouseReleaseEvent(self, a0: QtGui.QMouseEvent):
        self.mouse_release_action_signal.emit(a0.x(), a0.y())
