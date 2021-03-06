

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui

import os
import sys
import traceback
import io
import pkg_resources
import tempfile

from score_behavior import GIT_VERSION
# noinspection PyUnresolvedReferences
from score_behavior.score_controller import VideoDeviceManager, CameraDeviceManager
from score_behavior.score_window_ui import Ui_MainWindow
from score_behavior.ObjectSpace.analyzer import ObjectSpaceFrameAnalyzer
from score_behavior.score_analyzer import FrameAnalyzer
from score_behavior.global_defs import DeviceState, supported_camera_types
from score_behavior.score_config import config_init, get_config_section, config_dict


import logging
logger = logging.getLogger(__name__)


# noinspection PyAttributeOutsideInit
class ScorerMainWindow(QtWidgets.QMainWindow):
    key_action = QtCore.pyqtSignal(str, name="ScorerMainWindow.key_action")
    comments_received = QtCore.pyqtSignal(str, name='ScorerMainWindow.comments_received')

    def __init__(self):
        super(ScorerMainWindow, self).__init__(flags=QtCore.Qt.WindowFlags())
        self.do_track = True
        self.read_config()
        self.log = logging.getLogger(__name__)
        self.log.info('Initializing main window')

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setMenuBar(self.ui.menubar)
        self.session_file = None
        self._device = None
        self._analyzer = None
        self.ui.actionQuit.triggered.connect(self.close_all)
        self.ui.actionOpen_Live_Session.triggered.connect(self.get_live_session_file_to_open)
        self.ui.actionOpen_Video_Session.triggered.connect(self.get_video_session_file_to_open)
        self.ui.actionStop_Acquisition.setEnabled(False)
        self.ui.cameraWidget.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.ui.rawVideoCheckBox.setEnabled(False)
        self.ui.displayTsCheckBox.setChecked(True)
        self.setWindowTitle("Score")
        self.comments_dialog = None

    def read_config(self):
        pass
        # d = get_config_section("general")
        # if "do_track" in d:
        #     self.do_track = bool(d["do_track"])

    @property
    def device(self):
        return self._device

    @device.setter
    def device(self, dev):
        self._device = dev
        if dev:
            self.ui.cameraWidget.set_device(self.device)
            # noinspection PyUnresolvedReferences
            self.ui.cameraWidget.key_action.connect(self._analyzer.obj_state_change)
            self.ui.mirroredButton.setEnabled(True)
            self.ui.mirroredButton.setTristate(False)
            self.ui.mirroredButton.toggled.connect(self.device.set_mirror)
            self.ui.rotateComboBox.setEnabled(True)
            self.ui.rotateComboBox.currentIndexChanged.connect(self.device.set_rotate)
            self.ui.playButton.clicked.connect(self.device.start_trial_acquisition)
            self.ui.pauseButton.clicked.connect(self.device.stop_trial_acquisition)
            self.ui.actionStop_Acquisition.triggered.connect(self.device.stop_acquisition)
            self.ui.rawVideoCheckBox.toggled.connect(self.device.set_raw_out)
            self.ui.rawVideoCheckBox.setChecked(self.device.save_raw_video)
            self.ui.rawVideoCheckBox.setEnabled(True)
            self.ui.displayTsCheckBox.toggled.connect(self.device.set_display_time)
            self.ui.trialStatusButton.clicked.connect(self.trial_state_toggle_ongoing)
            self.device.time_remaining_signal.connect(self.ui.countDownLabel.setText)
            self.device.state_changed_signal.connect(self.change_device_state)
            self.change_device_state(dev.state)
            self._analyzer.device = self.device
            # self.device.can_acquire_signal.connect(self.change_acquisition_state)
            # self.change_acquisition_state(dev.can_acquire)
            # self.device.is_acquiring_signal.connect(self.acquisition_started_stopped)
            # self.device.is_paused_signal.connect(self.has_paused)
            self.device.size_changed_signal.connect(self.video_size_changed)
            self.device.video_out_file_changed_signal.connect(self.ui.destLabel.setText)
            self._analyzer.trial_number_changed_signal.connect(self.ui.trialLabel.setText)
            self.device.error_signal.connect(self.error_and_close)
            self.device.yes_no_question_signal.connect(self.yes_no_question)

            # noinspection PyUnresolvedReferences
            self.yes_no_answer_signal.connect(self.device.yes_no_answer)

            self.ui.cameraWidget.mouse_press_action_signal.connect(self._analyzer.mouse_press_action)
            self.ui.cameraWidget.mouse_move_action_signal.connect(self._analyzer.mouse_move_action)
            self.ui.cameraWidget.mouse_release_action_signal.connect(self._analyzer.mouse_release_action)
            self.ui.cameraWidget.key_action.connect(self._analyzer.obj_state_change)
            self.device.set_analyzer(self._analyzer)
            # noinspection PyUnresolvedReferences
            self.key_action.connect(self._analyzer.obj_state_change)

            # if self._analyzer.tracker:
            #     self.ui.sidebarWidget.layout().addWidget(self._analyzer.tracker_controller.widget)
            self.setFocus()
            self.log.info('Setting device to {}'.format(dev))
        else:
            self.log.info("resetting acquisition device")

    @QtCore.pyqtSlot()
    def video_size_changed(self):
        (w, h) = self.device.display_frame_size
        self.log.debug('Video size changed to {}, {}'.format(w, h))
        self.ui.cameraWidget.resize(w, h)
        self.updateGeometry()
        self.adjustSize()

    @QtCore.pyqtSlot(FrameAnalyzer.TrialState)
    def update_trial_state(self, state):
        if state == FrameAnalyzer.TrialState.IDLE:
            self.ui.trialStatusButton.setText("IDLE")
            self.ui.trialStatusButton.setStyleSheet("QPushButton { background-color : white; color : black; }")
        elif state == FrameAnalyzer.TrialState.READY:
            self.ui.trialStatusButton.setText("READY")
            self.ui.trialStatusButton.setStyleSheet("QPushButton { background-color : white; color : black; }")
        elif state == FrameAnalyzer.TrialState.ONGOING:
            self.ui.trialStatusButton.setText("ONGOING")
            self.ui.trialStatusButton.setStyleSheet("QPushButton { background-color : red; color : black; }")
        elif state == FrameAnalyzer.TrialState.COMPLETED:
            self.ui.trialStatusButton.setText("COMPLETED")
            self.ui.trialStatusButton.setStyleSheet("QPushButton { background-color : white; color : black; }")

    @QtCore.pyqtSlot()
    def video_finished(self):
        self.log.info('Video completed')
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)

        msg.setText("Video Completed")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        msg.exec_()

    @QtCore.pyqtSlot(DeviceState)
    def change_device_state(self, state):
        if state == DeviceState.NOT_READY:
            self.ui.playButton.setEnabled(False)
            self.ui.pauseButton.setEnabled(False)
            self.ui.scaleComboBox.setEnabled(True)
            self.ui.rotateComboBox.setEnabled(True)
            self.ui.mirroredButton.setEnabled(True)
        elif state == DeviceState.READY:
            self.ui.playButton.setEnabled(True)
            self.ui.pauseButton.setEnabled(False)
            self.ui.actionStop_Acquisition.setEnabled(False)
            self.ui.scaleComboBox.setEnabled(True)
            self.ui.rotateComboBox.setEnabled(True)
            self.ui.mirroredButton.setEnabled(True)
        elif state == DeviceState.ACQUIRING:
            self.ui.playButton.setEnabled(False)
            self.ui.pauseButton.setEnabled(True)
            self.ui.actionStop_Acquisition.setEnabled(True)
            self.ui.scaleComboBox.setEnabled(False)
            self.ui.rotateComboBox.setEnabled(False)
            self.ui.mirroredButton.setEnabled(False)

    @QtCore.pyqtSlot(str, str)
    def info_dialog(self, title, text):
        QtWidgets.QMessageBox.information(self, title, text)

    @QtCore.pyqtSlot(str)
    def error_and_close(self, e):
        self.log.error('Closing due to: {}'.format(e))
        error = QtWidgets.QErrorMessage()
        error.showMessage(e)
        error.exec_()
        self.close_all()

    yes_no_answer_signal = QtCore.pyqtSignal(bool, name='ScorerWindow.yes_no_answer_signal')

    @QtCore.pyqtSlot(str)
    def yes_no_question(self, q):
        self.log.debug('Y/N question')
        reply = QtWidgets.QMessageBox.question(self, 'Question', q, QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        self.yes_no_answer_signal.emit(reply == QtWidgets.QMessageBox.Yes)

    @QtCore.pyqtSlot()
    def close_all(self):
        self.log.debug('Closing all')
        if self.device:
            self.device.cleanup()

        if self._analyzer:
            self._analyzer.close()
        QtCore.QCoreApplication.quit()

    def get_camera_id_to_open(self):
        # n_cameras = find_how_many_cameras()
        n_cameras = 5
        self.log.debug("n_cameras: {}".format(n_cameras))
        ops = [str(i) for i in range(n_cameras)]
        import time
        time.sleep(1)

        if len(ops) == 1:
            cam = ops[0]
        else:
            # noinspection PyCallByClass,PyTypeChecker,PyArgumentList
            dialog_out = QtWidgets.QInputDialog.getItem(self, "Open Camera", "Which camera id do you want to open?",
                                                        ops)
            if not dialog_out[1]:
                return
            cam = int(dialog_out[0])
        self.log.debug('Chose camera {}'.format(cam))
        return cam

    # noinspection PyArgumentList
    @QtCore.pyqtSlot()
    def get_video_file_to_open(self):
        self.log.debug('Asking for video location to open...')
        # noinspection PyCallByClass,PyTypeChecker
        dialog_out = QtWidgets.QFileDialog.getOpenFileName(self, "Open Video File",
                                                           os.getcwd(), "Videos (*.mp4 *.avi)")
        open_video_file = dialog_out[0]
        if open_video_file:
            self.set_video_in(open_video_file)
        else:
            self.log.debug('No video file location given. Doing nothing.'.format(open_video_file))

    # noinspection PyArgumentList
    @QtCore.pyqtSlot()
    def get_live_session_file_to_open(self):
        self.log.debug('Asking for session file location to open...')
        # noinspection PyCallByClass,PyTypeChecker
        dialog_out = QtWidgets.QFileDialog.getOpenFileName(self, "Open Live Session File",
                                                           os.getcwd(), "CSV (*.sheet.csv)")
        session_file = dialog_out[0]
        self.open_live_session(session_file)

    def open_live_session(self, session_file, first_trial=0):
        if session_file:
            self.session_file = session_file
            self.log.info('Session file opened: {}'.format(self.session_file))
        else:
            self.log.info('No session file given. Doing nothing.')
        d = get_config_section("video")
        if "camera_type" in d and d["camera_type"] not in supported_camera_types:
            raise TypeError("unsupported camera type: ", d["camera_type"])

        if "camera_id" in d:
            cam_id = d["camera_id"]
        else:
            cam_id = self.get_camera_id_to_open()
        self.set_camera(cam_id, first_trial)

        # setting video parameters from config file
        if "display_scale" in d:
            v = str(d["display_scale"])
            if v not in self.device.scales_possible:
                raise ValueError("Scale value " + str(v) + " not allowed")
            self.ui.scaleComboBox.setCurrentIndex(self.device.scales_possible.index(v))
        if "video_rotate" in d:
            v = str(d["video_rotate"])
            rs = [str(i) for i in self.device.rotate_options]
            if v not in rs:
                raise ValueError("Rotate value " + str(v) + " not allowed")
            self.ui.rotateComboBox.setCurrentIndex(rs.index(v))
        if "video_mirror" in d:
            self.ui.mirroredButton.setCheckState(d["video_mirror"])

        if "video_raw_out" in d:
            self.ui.rawVideoCheckBox.setCheckState(d["video_raw_out"])

    # noinspection PyMethodMayBeStatic
    def get_video_session_file_to_open(self):

        self.log.debug("Setting video session ")

        dialog_out = QtWidgets.QFileDialog.getOpenFileName(self, "Open Video Session File",
                                                           os.getcwd(), "CSV (*_sheet.csv)")
        # video_in_filename = QtWidgets.QFileDialog.getOpenFileName(self, "Open Video Session File",
        #                                                           os.getcwd(), "Videos (*.mp4 *.avi)")
        # video_in_filename = video_in_filename[0]
        self.session_file = dialog_out[0]
        self.set_video_in()

    def set_camera(self, camera_id, first_trial=0):
        self.log.debug('Set camera to {}'.format(camera_id))
        if self.device:
            self.device.cleanup()
        self._analyzer = ObjectSpaceFrameAnalyzer(self.device, parent=self)

        self._analyzer.set_session(self.session_file, mode='live', first_trial=first_trial)
        self._analyzer.error_signal.connect(self.error_and_close)
        self._analyzer.post_trial_dialog_trigger_signal.connect(self.info_dialog)
        self._analyzer.trial_state_changed_signal.connect(self.update_trial_state)
        self.device = CameraDeviceManager(camera_id=camera_id, analyzer=self._analyzer, parent_window=self)
        self.ui.sourceLabel.setText("Camera: " + str(camera_id))
        self.ui.scaleComboBox.addItems(self.device.scales_possible)
        self.ui.scaleComboBox.setCurrentIndex(self.device.scale_init)
        self.ui.scaleComboBox.setEnabled(True)
        self.ui.scaleComboBox.currentIndexChanged.connect(self.device.change_scale)
        self.ui.rotateComboBox.addItems([str(i) for i in self.device.rotate_options])
        self.ui.rotateComboBox.setEnabled(True)
        self.ui.rotateComboBox.setCurrentIndex(0)
        self.ui.rotateComboBox.currentIndexChanged.connect(self.device.set_rotate)

    def set_video_in(self):
        if self.device:
            self.device.cleanup()
        self._analyzer = ObjectSpaceFrameAnalyzer(self.device, parent=self)
        self._analyzer.set_session(self.session_file, mode='video')
        self._analyzer.error_signal.connect(self.error_and_close)
        self.device = VideoDeviceManager(analyzer=self._analyzer, parent_window=self)
        self.device.video_in_changed_signal.connect(self.ui.sourceLabel.setText)
        self.device.init_device()

        self.ui.scaleComboBox.addItems(self.device.scales_possible)
        self.ui.scaleComboBox.setCurrentIndex(self.device.scale_init)
        self.ui.scaleComboBox.setEnabled(True)
        self.ui.scaleComboBox.currentIndexChanged.connect(self.device.change_scale)
        self.ui.scaleComboBox.setEnabled(False)
        self.device.video_finished_signal.connect(self.video_finished)

    def keyPressEvent(self, event):
        self.log.log(5, "key pressed {}, isAutorepeat {}".format(event.key(), event.isAutoRepeat()))
        if self.device:
            keymap = self._analyzer.key_interface()
            if not event.isAutoRepeat() and event.key() in keymap:
                msg = keymap[event.key()] + '1'
                self.key_action.emit(msg)
        event.accept()

    def keyReleaseEvent(self, event):
        self.log.log(5, "key released {}, isAutorepeat {}".format(event.key(), event.isAutoRepeat()))
        if self.device:
            keymap = self._analyzer.key_interface()
            if not event.isAutoRepeat() and event.key() in keymap:
                msg = keymap[event.key()] + '0'
                self.key_action.emit(msg)
        event.accept()

    def trial_state_toggle_ongoing(self):
        self.log.log(5, 'trial state toggle button clicked')
        msg = 'TR1'
        self.key_action.emit(msg)

def excepthook(exc_type, exc_value, tracebackobj):
    """
    Global function to catch unhandled exceptions.

    @param exc_type exception type
    @param exc_value exception value
    @param tracebackobj traceback object
    """
    notice = """An unhandled exception occurred. Please report the problem\n"""

    tbinfofile = io.StringIO()
    traceback.print_tb(tracebackobj, None, tbinfofile)
    tbinfofile.seek(0)
    tbinfo = tbinfofile.getvalue()
    errmsg = '{}: \n{}'.format(str(exc_type), str(exc_value))
    sections = [notice, errmsg, tbinfo]
    msg = '\n'.join(sections)
    try:
        logger.error(msg)
    except IOError:
        pass
    errorbox = QtWidgets.QMessageBox()
    errorbox.setText(str(notice) + str(msg))
    errorbox.exec_()
    sys.exit(-1)


def _main():

    import argparse
    logging.basicConfig(filename='score_log.log', level=logging.INFO, filemode='w',
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logging.info('Starting Score with git version {}'.format(GIT_VERSION))

    parser = argparse.ArgumentParser(description='Experiment control and tracking for behavior.', prog='score')
    parser.add_argument('--debug', help="Run in debug mode", action='store_true')
    parser.add_argument('--config', nargs=1, help="Read a default config file")
    parser.add_argument('--version', action='version', version='%(prog)s ' + GIT_VERSION)
    parser.add_argument('--live', nargs=1, help="open a live file with sheet file ")
    parser.add_argument('--video', nargs=1, help="open a video file with sheet file ")
    parser.add_argument('--firsttrial', nargs=1, help="specify the first trial in the sheet to be run")
    args = parser.parse_args()
    fname = None
    if args.config:
        fname = args.config[0]
    config_init(fname)
    d = get_config_section("general")
    run_debug = d['debug']
    if args.debug:
        run_debug = True
    if run_debug:
        level = logging.DEBUG
    else:
        level = logging.INFO

    live_session = None
    if args.live:
        live_session = args.live[0]

    video_session = None
    if args.video:
        video_session = args.video[0]

    first_trial = 0
    if args.firsttrial:
        first_trial = int(args.firsttrial[0])
    logging.getLogger().setLevel(level)
    logging.info("Configuration information: {}".format(str(config_dict)))

    if run_debug:
        logging.info("Running in debug mode")
    else:
        logging.info("Running in release mode")

    try:
        app = QtWidgets.QApplication(sys.argv)
        icon_file_bytes = pkg_resources.resource_string(__name__, "resources/icons/memdyn_logo_square.png")
        icon_file = tempfile.NamedTemporaryFile()
        icon_file.write(icon_file_bytes)
        app.setWindowIcon(QtGui.QIcon(icon_file.name))
        icon_file.close()
        window = ScorerMainWindow()
        window.show()
        app.quitOnLastWindowClosed = True
        # noinspection PyUnresolvedReferences
        app.lastWindowClosed.connect(window.close_all)
        if live_session:
            window.open_live_session(live_session, first_trial)
        if video_session:
            window.session_file = video_session
            window.set_video_in()
        logging.info("Starting app")
        app.exec_()
        logging.info('All done.')
    except Exception as e:
        logging.error("Uncaught exception: {}".format(str(e)))


sys.excepthook = excepthook

if __name__ == '__main__':
    _main()
