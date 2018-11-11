# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'score_window_ui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1438, 855)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(664, 540))
        MainWindow.setMaximumSize(QtCore.QSize(1600, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setSizePolicy(sizePolicy)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalWidget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        # sizePolicy.setHeightForWidth(self.verticalWidget.sizePolicy().hasHeightForWidth())
        self.verticalWidget.setSizePolicy(sizePolicy)
        self.verticalWidget.setMaximumSize(QtCore.QSize(1048, 15000))
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cameraWidget = CVVideoWidget(self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cameraWidget.sizePolicy().hasHeightForWidth())
        self.cameraWidget.setSizePolicy(sizePolicy)
        self.cameraWidget.setMaximumSize(QtCore.QSize(1024, 768))
        self.cameraWidget.setObjectName("cameraWidget")
        self.verticalLayout.addWidget(self.cameraWidget)
        self.widget = QtWidgets.QWidget(self.verticalWidget)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 100))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setMinimumSize(QtCore.QSize(323, 100))
        self.groupBox.setMaximumSize(QtCore.QSize(323, 200))
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 12)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.playButton = QtWidgets.QPushButton(self.groupBox)
        self.playButton.setEnabled(False)
        self.playButton.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.playButton.setFont(font)
        self.playButton.setIconSize(QtCore.QSize(32, 32))
        self.playButton.setObjectName("playButton")
        self.horizontalLayout.addWidget(self.playButton)
        self.pauseButton = QtWidgets.QPushButton(self.groupBox)
        self.pauseButton.setEnabled(False)
        self.pauseButton.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pauseButton.setFont(font)
        self.pauseButton.setIconSize(QtCore.QSize(32, 32))
        self.pauseButton.setObjectName("pauseButton")
        self.horizontalLayout.addWidget(self.pauseButton)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_2.setMinimumSize(QtCore.QSize(200, 100))
        self.groupBox_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.trialStatusButton = QtWidgets.QPushButton(self.groupBox_2)
        self.trialStatusButton.setGeometry(QtCore.QRect(30, 30, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.trialStatusButton.setFont(font)
        self.trialStatusButton.setObjectName("trialStatusButton")
        self.horizontalLayout_2.addWidget(self.groupBox_2)
        self.widget1 = QtWidgets.QWidget(self.widget)
        self.widget1.setMinimumSize(QtCore.QSize(0, 70))
        self.widget1.setMaximumSize(QtCore.QSize(16777215, 110))
        self.widget1.setObjectName("widget1")
        self.gridLayout = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.widget1)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.widget1)
        self.label.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.destLabel = QtWidgets.QLabel(self.widget1)
        self.destLabel.setObjectName("destLabel")
        self.gridLayout.addWidget(self.destLabel, 3, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)
        self.sourceLabel = QtWidgets.QLabel(self.widget1)
        self.sourceLabel.setObjectName("sourceLabel")
        self.gridLayout.addWidget(self.sourceLabel, 1, 1, 1, 1)
        self.horizontalLayout_2.addWidget(self.widget1)
        self.logoLabel = QtWidgets.QLabel(self.widget)
        self.logoLabel.setMaximumSize(QtCore.QSize(200, 32))
        self.logoLabel.setText("")
        self.logoLabel.setPixmap(QtGui.QPixmap(":/logo/logo1.png"))
        self.logoLabel.setObjectName("logoLabel")
        self.horizontalLayout_2.addWidget(self.logoLabel)
        self.verticalLayout.addWidget(self.widget)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.groupBox1 = QtWidgets.QGroupBox(self.verticalWidget)
        self.groupBox1.setMaximumSize(QtCore.QSize(16777215, 60))
        self.groupBox1.setObjectName("groupBox1")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox1)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.scaleComboBox = QtWidgets.QComboBox(self.groupBox1)
        self.scaleComboBox.setEnabled(False)
        self.scaleComboBox.setCurrentText("")
        self.scaleComboBox.setObjectName("scaleComboBox")
        self.horizontalLayout_4.addWidget(self.scaleComboBox)
        self.line_2 = QtWidgets.QFrame(self.groupBox1)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_4.addWidget(self.line_2)
        self.mirroredButton = QtWidgets.QCheckBox(self.groupBox1)
        self.mirroredButton.setObjectName("mirroredButton")
        self.horizontalLayout_4.addWidget(self.mirroredButton)
        self.line_5 = QtWidgets.QFrame(self.groupBox1)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout_4.addWidget(self.line_5)
        self.label_4 = QtWidgets.QLabel(self.groupBox1)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.rotateComboBox = QtWidgets.QComboBox(self.groupBox1)
        self.rotateComboBox.setObjectName("rotateComboBox")
        self.horizontalLayout_4.addWidget(self.rotateComboBox)
        self.line_3 = QtWidgets.QFrame(self.groupBox1)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_4.addWidget(self.line_3)
        self.displayTsCheckBox = QtWidgets.QCheckBox(self.groupBox1)
        self.displayTsCheckBox.setObjectName("displayTsCheckBox")
        self.horizontalLayout_4.addWidget(self.displayTsCheckBox)
        self.line_4 = QtWidgets.QFrame(self.groupBox1)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout_4.addWidget(self.line_4)
        self.rawVideoCheckBox = QtWidgets.QCheckBox(self.groupBox1)
        self.rawVideoCheckBox.setEnabled(False)
        self.rawVideoCheckBox.setObjectName("rawVideoCheckBox")
        self.horizontalLayout_4.addWidget(self.rawVideoCheckBox)
        self.verticalLayout.addWidget(self.groupBox1)
        self.horizontalLayout_7.addWidget(self.verticalWidget)
        self.sidebarContainer = QtWidgets.QFrame(self.centralwidget)
        self.sidebarContainer.setMinimumSize(QtCore.QSize(350, 0))
        self.sidebarContainer.setMaximumSize(QtCore.QSize(350, 16777215))
        self.sidebarContainer.setFrameShape(QtWidgets.QFrame.Box)
        self.sidebarContainer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sidebarContainer.setLineWidth(2)
        self.sidebarContainer.setMidLineWidth(1)
        self.sidebarContainer.setObjectName("sidebarContainer")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.sidebarContainer)
        self.verticalLayout_6.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.sidebarWidget = QtWidgets.QWidget(self.sidebarContainer)
        self.sidebarWidget.setMinimumSize(QtCore.QSize(0, 30))
        self.sidebarWidget.setObjectName("sidebarWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.sidebarWidget)
        self.verticalLayout_5.setContentsMargins(0, 6, 0, 6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.sidebarWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 15))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.trialLabel = QtWidgets.QLabel(self.sidebarWidget)
        self.trialLabel.setMinimumSize(QtCore.QSize(0, 50))
        self.trialLabel.setMaximumSize(QtCore.QSize(16777215, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.trialLabel.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.trialLabel.setFont(font)
        self.trialLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.trialLabel.setObjectName("trialLabel")
        self.verticalLayout_5.addWidget(self.trialLabel)
        self.countdownWidget = QtWidgets.QWidget(self.sidebarWidget)
        self.countdownWidget.setMinimumSize(QtCore.QSize(0, 60))
        self.countdownWidget.setObjectName("countdownWidget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.countdownWidget)
        self.verticalLayout_7.setContentsMargins(0, 6, 0, 6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.countdownWidget)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 15))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_7.addWidget(self.label_6)
        self.countDownLabel = QtWidgets.QLabel(self.countdownWidget)
        self.countDownLabel.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(30)
        self.countDownLabel.setFont(font)
        self.countDownLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.countDownLabel.setObjectName("countDownLabel")
        self.verticalLayout_7.addWidget(self.countDownLabel)
        self.line = QtWidgets.QFrame(self.countdownWidget)
        self.line.setLineWidth(5)
        self.line.setMidLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_7.addWidget(self.line)
        self.verticalLayout_5.addWidget(self.countdownWidget)
        self.verticalLayout_6.addWidget(self.sidebarWidget)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem3)
        self.horizontalLayout_7.addWidget(self.sidebarContainer)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1438, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionOpen_Live_Session = QtWidgets.QAction(MainWindow)
        self.actionOpen_Live_Session.setObjectName("actionOpen_Live_Session")
        self.actionOpen_Video_Session = QtWidgets.QAction(MainWindow)
        self.actionOpen_Video_Session.setObjectName("actionOpen_Video_Session")
        self.actionStop_Acquisition = QtWidgets.QAction(MainWindow)
        self.actionStop_Acquisition.setObjectName("actionStop_Acquisition")
        self.menuFile.addAction(self.actionOpen_Live_Session)
        self.menuFile.addAction(self.actionOpen_Video_Session)
        self.menuFile.addAction(self.actionStop_Acquisition)
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cameraWidget.setToolTip(_translate("MainWindow", "Video Viewer for Behavioral Tracking"))
        self.cameraWidget.setWhatsThis(_translate("MainWindow", "A Video Viewer for OpenCV based behavioral trackingusing PyQt."))
        self.groupBox.setTitle(_translate("MainWindow", "Trial Controls"))
        self.playButton.setText(_translate("MainWindow", "START TRIAL"))
        self.playButton.setShortcut(_translate("MainWindow", "Ctrl+Right"))
        self.pauseButton.setText(_translate("MainWindow", "END TRIAL"))
        self.pauseButton.setShortcut(_translate("MainWindow", "Ctrl+Space, Meta+Space"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Trial Status"))
        self.trialStatusButton.setText(_translate("MainWindow", "IDLE"))
        self.label_2.setText(_translate("MainWindow", "Writing to:"))
        self.label.setText(_translate("MainWindow", "Playing from:"))
        self.destLabel.setText(_translate("MainWindow", "NO DEST"))
        self.sourceLabel.setText(_translate("MainWindow", "NO SOURCE"))
        self.groupBox1.setTitle(_translate("MainWindow", "Video Output Controls"))
        self.label_3.setText(_translate("MainWindow", "Image scale"))
        self.mirroredButton.setText(_translate("MainWindow", "Mirrored"))
        self.label_4.setText(_translate("MainWindow", "Rotate (degrees)"))
        self.displayTsCheckBox.setText(_translate("MainWindow", "Display TStamps"))
        self.rawVideoCheckBox.setText(_translate("MainWindow", "Save raw video"))
        self.label_5.setText(_translate("MainWindow", "Current Trial"))
        self.trialLabel.setText(_translate("MainWindow", "0"))
        self.label_6.setText(_translate("MainWindow", "Remaining time in Trial"))
        self.countDownLabel.setText(_translate("MainWindow", "0:00.00"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionOpen_Live_Session.setText(_translate("MainWindow", "Open Live Session..."))
        self.actionOpen_Video_Session.setText(_translate("MainWindow", "Open Video Session..."))
        self.actionStop_Acquisition.setText(_translate("MainWindow", "Stop Acquisition"))

from score_behavior.cv_video_widget import CVVideoWidget
import score_behavior.logo_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

