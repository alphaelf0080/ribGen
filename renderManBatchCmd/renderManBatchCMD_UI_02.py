# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/alpha.DESKTOP-1S1STEK/Documents/GitHub/ribGen/renderManBatchCMD_UI_02.ui'
#
# Created: Mon Feb 20 17:42:36 2017
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(692, 605)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 101, 16))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 30, 101, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_frameStart = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_frameStart.setGeometry(QtCore.QRect(100, 30, 110, 20))
        self.lineEdit_frameStart.setObjectName("lineEdit_frameStart")
        self.lineEdit_frameEnd = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_frameEnd.setGeometry(QtCore.QRect(320, 30, 110, 20))
        self.lineEdit_frameEnd.setObjectName("lineEdit_frameEnd")
        self.lineEdit_Project = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_Project.setGeometry(QtCore.QRect(140, 150, 531, 20))
        self.lineEdit_Project.setObjectName("lineEdit_Project")
        self.lineEdit_filePath = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_filePath.setGeometry(QtCore.QRect(140, 180, 531, 20))
        self.lineEdit_filePath.setObjectName("lineEdit_filePath")
        self.pushButton_createBatchCmd = QtGui.QPushButton(self.centralwidget)
        self.pushButton_createBatchCmd.setGeometry(QtCore.QRect(30, 270, 181, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(90, 112, 103))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(90, 112, 103))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(90, 112, 103))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.pushButton_createBatchCmd.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_createBatchCmd.setFont(font)
        self.pushButton_createBatchCmd.setObjectName("pushButton_createBatchCmd")
        self.pushButton_setProject = QtGui.QPushButton(self.centralwidget)
        self.pushButton_setProject.setGeometry(QtCore.QRect(30, 150, 91, 23))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 71, 104))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 71, 104))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 71, 104))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.pushButton_setProject.setPalette(palette)
        self.pushButton_setProject.setObjectName("pushButton_setProject")
        self.pushButton_setFilePath = QtGui.QPushButton(self.centralwidget)
        self.pushButton_setFilePath.setGeometry(QtCore.QRect(30, 180, 91, 23))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 71, 104))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 71, 104))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 71, 104))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.pushButton_setFilePath.setPalette(palette)
        self.pushButton_setFilePath.setObjectName("pushButton_setFilePath")
        self.lineEdit_filePath_renderCmd = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_filePath_renderCmd.setGeometry(QtCore.QRect(230, 270, 441, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.lineEdit_filePath_renderCmd.setFont(font)
        self.lineEdit_filePath_renderCmd.setObjectName("lineEdit_filePath_renderCmd")
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 210, 81, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_prmanReleated = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_prmanReleated.setGeometry(QtCore.QRect(140, 210, 531, 20))
        self.lineEdit_prmanReleated.setObjectName("lineEdit_prmanReleated")
        self.lineEdit_resX = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_resX.setEnabled(False)
        self.lineEdit_resX.setGeometry(QtCore.QRect(130, 70, 61, 20))
        self.lineEdit_resX.setObjectName("lineEdit_resX")
        self.lineEdit_resY = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_resY.setEnabled(False)
        self.lineEdit_resY.setGeometry(QtCore.QRect(196, 70, 61, 20))
        self.lineEdit_resY.setObjectName("lineEdit_resY")
        self.lineEdit_modifyMaxSample = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_modifyMaxSample.setEnabled(False)
        self.lineEdit_modifyMaxSample.setGeometry(QtCore.QRect(400, 70, 61, 20))
        self.lineEdit_modifyMaxSample.setObjectName("lineEdit_modifyMaxSample")
        self.checkBox_exportLog = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_exportLog.setGeometry(QtCore.QRect(30, 102, 281, 16))
        self.checkBox_exportLog.setChecked(True)
        self.checkBox_exportLog.setObjectName("checkBox_exportLog")
        self.checkBox_modifyRESXY = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_modifyRESXY.setGeometry(QtCore.QRect(30, 70, 91, 16))
        self.checkBox_modifyRESXY.setObjectName("checkBox_modifyRESXY")
        self.checkBox_modifyMaxSample = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_modifyMaxSample.setGeometry(QtCore.QRect(280, 70, 121, 16))
        self.checkBox_modifyMaxSample.setObjectName("checkBox_modifyMaxSample")
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 120, 681, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 380, 681, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.lineEdit_MayaFile = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_MayaFile.setGeometry(QtCore.QRect(190, 458, 471, 31))
        self.lineEdit_MayaFile.setObjectName("lineEdit_MayaFile")
        self.pushButton_setMayaFile = QtGui.QPushButton(self.centralwidget)
        self.pushButton_setMayaFile.setGeometry(QtCore.QRect(20, 458, 151, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 71, 104))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 71, 104))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 71, 104))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.pushButton_setMayaFile.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_setMayaFile.setFont(font)
        self.pushButton_setMayaFile.setObjectName("pushButton_setMayaFile")
        self.checkBox_frameStep = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_frameStep.setGeometry(QtCore.QRect(500, 30, 51, 16))
        self.checkBox_frameStep.setObjectName("checkBox_frameStep")
        self.lineEdit_frameStep = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_frameStep.setEnabled(False)
        self.lineEdit_frameStep.setGeometry(QtCore.QRect(560, 30, 61, 20))
        self.lineEdit_frameStep.setObjectName("lineEdit_frameStep")
        self.pushButton_genRenderJob = QtGui.QPushButton(self.centralwidget)
        self.pushButton_genRenderJob.setGeometry(QtCore.QRect(20, 520, 151, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(193, 125, 113))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(193, 125, 113))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(193, 125, 113))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.pushButton_genRenderJob.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_genRenderJob.setFont(font)
        self.pushButton_genRenderJob.setObjectName("pushButton_genRenderJob")
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 400, 91, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_fileNamePrefix = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_fileNamePrefix.setGeometry(QtCore.QRect(130, 400, 531, 20))
        self.lineEdit_fileNamePrefix.setObjectName("lineEdit_fileNamePrefix")
        self.checkBox_divide = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_divide.setGeometry(QtCore.QRect(500, 70, 71, 16))
        self.checkBox_divide.setObjectName("checkBox_divide")
        self.lineEdit_divide = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_divide.setEnabled(False)
        self.lineEdit_divide.setGeometry(QtCore.QRect(560, 70, 61, 20))
        self.lineEdit_divide.setObjectName("lineEdit_divide")
        self.radioButton_single = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_single.setGeometry(QtCore.QRect(40, 240, 81, 16))
        self.radioButton_single.setChecked(True)
        self.radioButton_single.setObjectName("radioButton_single")
        self.radioButton_multifiles = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_multifiles.setGeometry(QtCore.QRect(130, 240, 91, 16))
        self.radioButton_multifiles.setObjectName("radioButton_multifiles")
        self.pushButton_submitDeadLine = QtGui.QPushButton(self.centralwidget)
        self.pushButton_submitDeadLine.setGeometry(QtCore.QRect(30, 310, 181, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(90, 112, 103))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(90, 112, 103))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(90, 112, 103))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.pushButton_submitDeadLine.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_submitDeadLine.setFont(font)
        self.pushButton_submitDeadLine.setObjectName("pushButton_submitDeadLine")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 692, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "renderManBatchRender", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Frame Start", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Frame End", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_createBatchCmd.setText(QtGui.QApplication.translate("MainWindow", "Create batchRender file", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_setProject.setText(QtGui.QApplication.translate("MainWindow", "set Project", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_setFilePath.setText(QtGui.QApplication.translate("MainWindow", "set File Path", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_filePath_renderCmd.setText(QtGui.QApplication.translate("MainWindow", "c:/temp/renderManRender.bat", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "PRMAN related", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_prmanReleated.setText(QtGui.QApplication.translate("MainWindow", "prman -t:0 -Progress -recover 0 -logfile c:/temp/render.log -loglevel 4 -checkpoint 5m -cwd ", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_exportLog.setText(QtGui.QApplication.translate("MainWindow", "export LogFile(batchRenderFileName.log)", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_modifyRESXY.setText(QtGui.QApplication.translate("MainWindow", "Modify ResXY", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_modifyMaxSample.setText(QtGui.QApplication.translate("MainWindow", "Modify Max Sample", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_setMayaFile.setText(QtGui.QApplication.translate("MainWindow", "set Maya File", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_frameStep.setText(QtGui.QApplication.translate("MainWindow", "Step", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_frameStep.setText(QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_genRenderJob.setText(QtGui.QApplication.translate("MainWindow", "Generate RenderJob", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "file Name Prefix", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_fileNamePrefix.setText(QtGui.QApplication.translate("MainWindow", "<Scene>/<RenderLayer>/<RenderLayer>", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_divide.setText(QtGui.QApplication.translate("MainWindow", "Divide", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_divide.setText(QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_single.setText(QtGui.QApplication.translate("MainWindow", "single file", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_multifiles.setText(QtGui.QApplication.translate("MainWindow", "mulit Files", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_submitDeadLine.setText(QtGui.QApplication.translate("MainWindow", "submit to DeadLine", None, QtGui.QApplication.UnicodeUTF8))

