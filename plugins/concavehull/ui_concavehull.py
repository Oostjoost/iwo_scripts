# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\0000200_Entwicklung\ConcaveHull_for_QGIS\concavehull\ui_concavehull.ui'
#
# Created: Fri Jan 09 15:52:44 2015
#      by: PyQt4 UI code generator 4.10.2
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

class Ui_ConcaveHull(object):
    def setupUi(self, ConcaveHull):
        ConcaveHull.setObjectName(_fromUtf8("ConcaveHull"))
        ConcaveHull.resize(388, 560)
        self.verticalLayout = QtGui.QVBoxLayout(ConcaveHull)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(ConcaveHull)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 60))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 62))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.hs_neighbors = QtGui.QSlider(self.groupBox)
        self.hs_neighbors.setMinimum(2)
        self.hs_neighbors.setMaximum(25)
        self.hs_neighbors.setPageStep(5)
        self.hs_neighbors.setProperty("value", 3)
        self.hs_neighbors.setOrientation(QtCore.Qt.Horizontal)
        self.hs_neighbors.setTickPosition(QtGui.QSlider.TicksBelow)
        self.hs_neighbors.setTickInterval(2)
        self.hs_neighbors.setObjectName(_fromUtf8("hs_neighbors"))
        self.horizontalLayout.addWidget(self.hs_neighbors)
        self.sb_neighbors = QtGui.QSpinBox(self.groupBox)
        self.sb_neighbors.setMinimum(2)
        self.sb_neighbors.setMaximum(25)
        self.sb_neighbors.setProperty("value", 3)
        self.sb_neighbors.setObjectName(_fromUtf8("sb_neighbors"))
        self.horizontalLayout.addWidget(self.sb_neighbors)
        self.verticalLayout.addWidget(self.groupBox)
        self.gb_clustering = QtGui.QGroupBox(ConcaveHull)
        self.gb_clustering.setMinimumSize(QtCore.QSize(0, 0))
        self.gb_clustering.setCheckable(True)
        self.gb_clustering.setChecked(False)
        self.gb_clustering.setObjectName(_fromUtf8("gb_clustering"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.gb_clustering)
        self.verticalLayout_4.setContentsMargins(-1, -1, 9, 0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.frame = QtGui.QFrame(self.gb_clustering)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Plain)
        self.frame.setLineWidth(0)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout_4.addWidget(self.frame)
        self.frame_2 = QtGui.QFrame(self.gb_clustering)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_2.setLineWidth(0)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.hs_neighborhood_list_size = QtGui.QSlider(self.frame_2)
        self.hs_neighborhood_list_size.setMinimum(4)
        self.hs_neighborhood_list_size.setMaximum(100)
        self.hs_neighborhood_list_size.setPageStep(5)
        self.hs_neighborhood_list_size.setProperty("value", 5)
        self.hs_neighborhood_list_size.setOrientation(QtCore.Qt.Horizontal)
        self.hs_neighborhood_list_size.setTickPosition(QtGui.QSlider.TicksBelow)
        self.hs_neighborhood_list_size.setTickInterval(5)
        self.hs_neighborhood_list_size.setObjectName(_fromUtf8("hs_neighborhood_list_size"))
        self.horizontalLayout_3.addWidget(self.hs_neighborhood_list_size)
        self.sb_neighborhood_list_size = QtGui.QSpinBox(self.frame_2)
        self.sb_neighborhood_list_size.setMinimum(4)
        self.sb_neighborhood_list_size.setMaximum(100)
        self.sb_neighborhood_list_size.setProperty("value", 5)
        self.sb_neighborhood_list_size.setObjectName(_fromUtf8("sb_neighborhood_list_size"))
        self.horizontalLayout_3.addWidget(self.sb_neighborhood_list_size)
        self.verticalLayout_4.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.gb_clustering)
        self.groupBox_2 = QtGui.QGroupBox(ConcaveHull)
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.ls_layers = QtGui.QListWidget(self.groupBox_2)
        self.ls_layers.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.ls_layers.setObjectName(_fromUtf8("ls_layers"))
        self.verticalLayout_2.addWidget(self.ls_layers)
        self.cb_selected_only = QtGui.QCheckBox(self.groupBox_2)
        self.cb_selected_only.setObjectName(_fromUtf8("cb_selected_only"))
        self.verticalLayout_2.addWidget(self.cb_selected_only)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.gb_output = QtGui.QGroupBox(ConcaveHull)
        self.gb_output.setObjectName(_fromUtf8("gb_output"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.gb_output)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.rb_new_memory_layer = QtGui.QRadioButton(self.gb_output)
        self.rb_new_memory_layer.setChecked(True)
        self.rb_new_memory_layer.setObjectName(_fromUtf8("rb_new_memory_layer"))
        self.verticalLayout_3.addWidget(self.rb_new_memory_layer)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(20, 0, -1, 0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.ed_memory_layer = QtGui.QLineEdit(self.gb_output)
        self.ed_memory_layer.setEnabled(True)
        self.ed_memory_layer.setObjectName(_fromUtf8("ed_memory_layer"))
        self.horizontalLayout_5.addWidget(self.ed_memory_layer)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.rb_existing_layer = QtGui.QRadioButton(self.gb_output)
        self.rb_existing_layer.setChecked(False)
        self.rb_existing_layer.setObjectName(_fromUtf8("rb_existing_layer"))
        self.verticalLayout_3.addWidget(self.rb_existing_layer)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(20, 0, -1, -1)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.cb_output = QtGui.QComboBox(self.gb_output)
        self.cb_output.setEnabled(False)
        self.cb_output.setEditable(False)
        self.cb_output.setObjectName(_fromUtf8("cb_output"))
        self.horizontalLayout_6.addWidget(self.cb_output)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.rb_shapefile = QtGui.QRadioButton(self.gb_output)
        self.rb_shapefile.setObjectName(_fromUtf8("rb_shapefile"))
        self.verticalLayout_3.addWidget(self.rb_shapefile)
        self.widget = QtGui.QWidget(self.gb_output)
        self.widget.setEnabled(False)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_5.setContentsMargins(20, 0, 0, 0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.ed_output_layer = QtGui.QLineEdit(self.widget)
        self.ed_output_layer.setReadOnly(True)
        self.ed_output_layer.setObjectName(_fromUtf8("ed_output_layer"))
        self.horizontalLayout_4.addWidget(self.ed_output_layer)
        self.bt_file_browser = QtGui.QPushButton(self.widget)
        self.bt_file_browser.setObjectName(_fromUtf8("bt_file_browser"))
        self.horizontalLayout_4.addWidget(self.bt_file_browser)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.cb_add_to_map = QtGui.QCheckBox(self.widget)
        self.cb_add_to_map.setObjectName(_fromUtf8("cb_add_to_map"))
        self.verticalLayout_5.addWidget(self.cb_add_to_map)
        self.verticalLayout_3.addWidget(self.widget)
        self.verticalLayout.addWidget(self.gb_output)
        self.buttonBox = QtGui.QDialogButtonBox(ConcaveHull)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ConcaveHull)
        self.cb_output.setCurrentIndex(-1)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ConcaveHull.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ConcaveHull.reject)
        QtCore.QObject.connect(self.hs_neighbors, QtCore.SIGNAL(_fromUtf8("sliderMoved(int)")), self.sb_neighbors.setValue)
        QtCore.QObject.connect(self.sb_neighbors, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.hs_neighbors.setValue)
        QtCore.QObject.connect(self.hs_neighborhood_list_size, QtCore.SIGNAL(_fromUtf8("sliderMoved(int)")), self.sb_neighborhood_list_size.setValue)
        QtCore.QObject.connect(self.sb_neighborhood_list_size, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.hs_neighborhood_list_size.setValue)
        QtCore.QObject.connect(self.rb_shapefile, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.widget.setEnabled)
        QtCore.QObject.connect(self.rb_new_memory_layer, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.ed_memory_layer.setEnabled)
        QtCore.QObject.connect(self.rb_existing_layer, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.cb_output.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(ConcaveHull)

    def retranslateUi(self, ConcaveHull):
        ConcaveHull.setWindowTitle(_translate("ConcaveHull", "ConcaveHull", None))
        self.groupBox.setToolTip(_translate("ConcaveHull", "Specify the number of nearest neighbors to start with", None))
        self.groupBox.setTitle(_translate("ConcaveHull", "Number of neighbors", None))
        self.gb_clustering.setToolTip(_translate("ConcaveHull", "Check and specify a neighborhood size to cluster the data prior constructing a hull", None))
        self.gb_clustering.setTitle(_translate("ConcaveHull", "Find SNN clusters", None))
        self.label.setText(_translate("ConcaveHull", "Neighborhood size", None))
        self.groupBox_2.setTitle(_translate("ConcaveHull", "Input layers", None))
        self.ls_layers.setToolTip(_translate("ConcaveHull", "Select one or more input layers", None))
        self.cb_selected_only.setToolTip(_translate("ConcaveHull", "Use only selected features on input layers", None))
        self.cb_selected_only.setText(_translate("ConcaveHull", "Use selected features only", None))
        self.gb_output.setTitle(_translate("ConcaveHull", "Output layer", None))
        self.rb_new_memory_layer.setText(_translate("ConcaveHull", "New memory layer", None))
        self.ed_memory_layer.setToolTip(_translate("ConcaveHull", "Type in the name of a new memory layer", None))
        self.ed_memory_layer.setText(_translate("ConcaveHull", "ConcaveHull", None))
        self.rb_existing_layer.setText(_translate("ConcaveHull", "Existing layer", None))
        self.cb_output.setToolTip(_translate("ConcaveHull", "Choose an existing polygon layer from the list", None))
        self.rb_shapefile.setText(_translate("ConcaveHull", "New shapefile", None))
        self.ed_output_layer.setToolTip(_translate("ConcaveHull", "Browse for the location of a new or existing Shape file", None))
        self.bt_file_browser.setToolTip(_translate("ConcaveHull", "Browse for the location of a new or existing Shape file", None))
        self.bt_file_browser.setText(_translate("ConcaveHull", "Browse ...", None))
        self.cb_add_to_map.setToolTip(_translate("ConcaveHull", "Add the new layer to the map", None))
        self.cb_add_to_map.setText(_translate("ConcaveHull", "Add result to map", None))