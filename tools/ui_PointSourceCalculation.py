# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_PointSourceCalculation.ui'
#
# Created: Mon Jan  9 11:18:58 2017
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_PointSourceCalculation_window(object):
    def setupUi(self, PointSourceCalculation_window):
        PointSourceCalculation_window.setObjectName(_fromUtf8("PointSourceCalculation_window"))
        PointSourceCalculation_window.setEnabled(True)
        PointSourceCalculation_window.resize(500, 522)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PointSourceCalculation_window.sizePolicy().hasHeightForWidth())
        PointSourceCalculation_window.setSizePolicy(sizePolicy)
        PointSourceCalculation_window.setMinimumSize(QtCore.QSize(500, 229))
        PointSourceCalculation_window.setSizeIncrement(QtCore.QSize(0, 0))
        PointSourceCalculation_window.setLocale(QtCore.QLocale(QtCore.QLocale.Italian, QtCore.QLocale.Italy))
        self.verticalLayoutWidget = QtGui.QWidget(PointSourceCalculation_window)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 19, 481, 101))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.source_layer_verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.source_layer_verticalLayout.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.source_layer_verticalLayout.setMargin(0)
        self.source_layer_verticalLayout.setObjectName(_fromUtf8("source_layer_verticalLayout"))
        self.source_layer_label = QtGui.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.source_layer_label.sizePolicy().hasHeightForWidth())
        self.source_layer_label.setSizePolicy(sizePolicy)
        self.source_layer_label.setObjectName(_fromUtf8("source_layer_label"))
        self.source_layer_verticalLayout.addWidget(self.source_layer_label)
        self.source_layer_comboBox = QtGui.QComboBox(self.verticalLayoutWidget)
        self.source_layer_comboBox.setObjectName(_fromUtf8("source_layer_comboBox"))
        self.source_layer_verticalLayout.addWidget(self.source_layer_comboBox)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.power_label = QtGui.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.power_label.sizePolicy().hasHeightForWidth())
        self.power_label.setSizePolicy(sizePolicy)
        self.power_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.power_label.setObjectName(_fromUtf8("power_label"))
        self.horizontalLayout_3.addWidget(self.power_label)
        self.power_comboBox = QtGui.QComboBox(self.verticalLayoutWidget)
        self.power_comboBox.setObjectName(_fromUtf8("power_comboBox"))
        self.horizontalLayout_3.addWidget(self.power_comboBox)
        self.source_layer_verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(PointSourceCalculation_window)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 470, 481, 31))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.progressBar = QtGui.QProgressBar(self.horizontalLayoutWidget_2)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.horizontalLayout.addWidget(self.progressBar)
        self.buttonBox = QtGui.QDialogButtonBox(self.horizontalLayoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout.addWidget(self.buttonBox)
        self.verticalLayoutWidget_2 = QtGui.QWidget(PointSourceCalculation_window)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 140, 481, 61))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.receiver_layer_verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.receiver_layer_verticalLayout.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.receiver_layer_verticalLayout.setMargin(0)
        self.receiver_layer_verticalLayout.setObjectName(_fromUtf8("receiver_layer_verticalLayout"))
        self.receiver_layer_label = QtGui.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.receiver_layer_label.sizePolicy().hasHeightForWidth())
        self.receiver_layer_label.setSizePolicy(sizePolicy)
        self.receiver_layer_label.setObjectName(_fromUtf8("receiver_layer_label"))
        self.receiver_layer_verticalLayout.addWidget(self.receiver_layer_label)
        self.receiver_layer_comboBox = QtGui.QComboBox(self.verticalLayoutWidget_2)
        self.receiver_layer_comboBox.setObjectName(_fromUtf8("receiver_layer_comboBox"))
        self.receiver_layer_verticalLayout.addWidget(self.receiver_layer_comboBox)
        self.verticalLayoutWidget_5 = QtGui.QWidget(PointSourceCalculation_window)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(10, 380, 481, 61))
        self.verticalLayoutWidget_5.setObjectName(_fromUtf8("verticalLayoutWidget_5"))
        self.rays_layer_verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_5)
        self.rays_layer_verticalLayout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.rays_layer_verticalLayout.setMargin(0)
        self.rays_layer_verticalLayout.setObjectName(_fromUtf8("rays_layer_verticalLayout"))
        self.rays_layer_checkBox = QtGui.QCheckBox(self.verticalLayoutWidget_5)
        self.rays_layer_checkBox.setEnabled(True)
        self.rays_layer_checkBox.setChecked(False)
        self.rays_layer_checkBox.setObjectName(_fromUtf8("rays_layer_checkBox"))
        self.rays_layer_verticalLayout.addWidget(self.rays_layer_checkBox)
        self.rays_layer_horizontalLayout = QtGui.QHBoxLayout()
        self.rays_layer_horizontalLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.rays_layer_horizontalLayout.setObjectName(_fromUtf8("rays_layer_horizontalLayout"))
        self.rays_layer_lineEdit = QtGui.QLineEdit(self.verticalLayoutWidget_5)
        self.rays_layer_lineEdit.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rays_layer_lineEdit.sizePolicy().hasHeightForWidth())
        self.rays_layer_lineEdit.setSizePolicy(sizePolicy)
        self.rays_layer_lineEdit.setObjectName(_fromUtf8("rays_layer_lineEdit"))
        self.rays_layer_horizontalLayout.addWidget(self.rays_layer_lineEdit)
        self.rays_layer_pushButton = QtGui.QPushButton(self.verticalLayoutWidget_5)
        self.rays_layer_pushButton.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rays_layer_pushButton.sizePolicy().hasHeightForWidth())
        self.rays_layer_pushButton.setSizePolicy(sizePolicy)
        self.rays_layer_pushButton.setObjectName(_fromUtf8("rays_layer_pushButton"))
        self.rays_layer_horizontalLayout.addWidget(self.rays_layer_pushButton)
        self.rays_layer_verticalLayout.addLayout(self.rays_layer_horizontalLayout)
        self.note_label_2 = QtGui.QLabel(PointSourceCalculation_window)
        self.note_label_2.setGeometry(QtCore.QRect(10, 360, 481, 21))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.note_label_2.sizePolicy().hasHeightForWidth())
        self.note_label_2.setSizePolicy(sizePolicy)
        self.note_label_2.setText(_fromUtf8("<html><head/><body><p><span style=\" font-style:italic;\">Optional</span></p></body></html>"))
        self.note_label_2.setObjectName(_fromUtf8("note_label_2"))
        self.research_ray_comboBox = QtGui.QComboBox(PointSourceCalculation_window)
        self.research_ray_comboBox.setGeometry(QtCore.QRect(10, 233, 131, 27))
        self.research_ray_comboBox.setObjectName(_fromUtf8("research_ray_comboBox"))
        self.research_ray_label = QtGui.QLabel(PointSourceCalculation_window)
        self.research_ray_label.setGeometry(QtCore.QRect(10, 211, 181, 20))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.research_ray_label.sizePolicy().hasHeightForWidth())
        self.research_ray_label.setSizePolicy(sizePolicy)
        self.research_ray_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.research_ray_label.setObjectName(_fromUtf8("research_ray_label"))
        self.verticalLayoutWidget_4 = QtGui.QWidget(PointSourceCalculation_window)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 280, 481, 63))
        self.verticalLayoutWidget_4.setObjectName(_fromUtf8("verticalLayoutWidget_4"))
        self.obstacles_layer_verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_4)
        self.obstacles_layer_verticalLayout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.obstacles_layer_verticalLayout.setMargin(0)
        self.obstacles_layer_verticalLayout.setObjectName(_fromUtf8("obstacles_layer_verticalLayout"))
        self.obstacles_layer_checkBox = QtGui.QCheckBox(self.verticalLayoutWidget_4)
        self.obstacles_layer_checkBox.setEnabled(True)
        self.obstacles_layer_checkBox.setChecked(False)
        self.obstacles_layer_checkBox.setObjectName(_fromUtf8("obstacles_layer_checkBox"))
        self.obstacles_layer_verticalLayout.addWidget(self.obstacles_layer_checkBox)
        self.obstacles_layer_comboBox = QtGui.QComboBox(self.verticalLayoutWidget_4)
        self.obstacles_layer_comboBox.setEnabled(False)
        self.obstacles_layer_comboBox.setObjectName(_fromUtf8("obstacles_layer_comboBox"))
        self.obstacles_layer_verticalLayout.addWidget(self.obstacles_layer_comboBox)
        self.line_3 = QtGui.QFrame(PointSourceCalculation_window)
        self.line_3.setGeometry(QtCore.QRect(10, 340, 481, 30))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))

        self.retranslateUi(PointSourceCalculation_window)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), PointSourceCalculation_window.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), PointSourceCalculation_window.reject)
        QtCore.QMetaObject.connectSlotsByName(PointSourceCalculation_window)

    def retranslateUi(self, PointSourceCalculation_window):
        PointSourceCalculation_window.setWindowTitle(_translate("PointSourceCalculation_window", "opeNoise - Point Source Calculation", None))
        self.source_layer_label.setText(_translate("PointSourceCalculation_window", "Point source layer (input point layer)", None))
        self.power_label.setText(_translate("PointSourceCalculation_window", "Field with power levels of the source:", None))
        self.receiver_layer_label.setText(_translate("PointSourceCalculation_window", "Receivers layer (input point layer)", None))
        self.rays_layer_checkBox.setText(_translate("PointSourceCalculation_window", "Sound rays layer (output line layer)", None))
        self.rays_layer_pushButton.setText(_translate("PointSourceCalculation_window", "Browse", None))
        self.research_ray_label.setText(_translate("PointSourceCalculation_window", "Research ray (m)", None))
        self.obstacles_layer_checkBox.setText(_translate("PointSourceCalculation_window", "Obstacles layer (input polygon layer)", None))

