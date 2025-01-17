# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mudurmakina.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mudurmakina(object):
    def setupUi(self, mudurmakina):
        mudurmakina.setObjectName("mudurmakina")
        mudurmakina.resize(1024, 768)
        mudurmakina.setMinimumSize(QtCore.QSize(1023, 768))
        mudurmakina.setMaximumSize(QtCore.QSize(1024, 768))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/admin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mudurmakina.setWindowIcon(icon)
        self.layoutWidget = QtWidgets.QWidget(mudurmakina)
        self.layoutWidget.setGeometry(QtCore.QRect(830, 40, 191, 351))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_mekle = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_mekle.sizePolicy().hasHeightForWidth())
        self.btn_mekle.setSizePolicy(sizePolicy)
        self.btn_mekle.setMinimumSize(QtCore.QSize(50, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_mekle.setFont(font)
        self.btn_mekle.setStyleSheet("background-color: rgb(111, 111, 111);\n"
"color: rgb(238, 119, 15);\n"
"border -radius : 5px")
        self.btn_mekle.setIconSize(QtCore.QSize(25, 25))
        self.btn_mekle.setObjectName("btn_mekle")
        self.verticalLayout_2.addWidget(self.btn_mekle)
        self.btn_msil = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_msil.sizePolicy().hasHeightForWidth())
        self.btn_msil.setSizePolicy(sizePolicy)
        self.btn_msil.setMinimumSize(QtCore.QSize(50, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_msil.setFont(font)
        self.btn_msil.setStyleSheet("background-color: rgb(111, 111, 111);\n"
"color: rgb(238, 119, 15);\n"
"border -radius : 5px")
        self.btn_msil.setIconSize(QtCore.QSize(25, 25))
        self.btn_msil.setObjectName("btn_msil")
        self.verticalLayout_2.addWidget(self.btn_msil)
        self.btn_mara = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_mara.sizePolicy().hasHeightForWidth())
        self.btn_mara.setSizePolicy(sizePolicy)
        self.btn_mara.setMinimumSize(QtCore.QSize(50, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_mara.setFont(font)
        self.btn_mara.setStyleSheet("background-color: rgb(111, 111, 111);\n"
"color: rgb(238, 119, 15);\n"
"border -radius : 5px")
        self.btn_mara.setIconSize(QtCore.QSize(25, 25))
        self.btn_mara.setObjectName("btn_mara")
        self.verticalLayout_2.addWidget(self.btn_mara)
        self.btn_mguncel = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_mguncel.sizePolicy().hasHeightForWidth())
        self.btn_mguncel.setSizePolicy(sizePolicy)
        self.btn_mguncel.setMinimumSize(QtCore.QSize(50, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_mguncel.setFont(font)
        self.btn_mguncel.setStyleSheet("background-color: rgb(111, 111, 111);\n"
"color: rgb(238, 119, 15);\n"
"border -radius : 5px")
        self.btn_mguncel.setIconSize(QtCore.QSize(25, 25))
        self.btn_mguncel.setObjectName("btn_mguncel")
        self.verticalLayout_2.addWidget(self.btn_mguncel)
        self.btn_mgeridon = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_mgeridon.sizePolicy().hasHeightForWidth())
        self.btn_mgeridon.setSizePolicy(sizePolicy)
        self.btn_mgeridon.setMinimumSize(QtCore.QSize(50, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_mgeridon.setFont(font)
        self.btn_mgeridon.setStyleSheet("background-color: rgb(111, 111, 111);\n"
"color: rgb(238, 119, 15);\n"
"border -radius : 5px")
        self.btn_mgeridon.setIconSize(QtCore.QSize(25, 25))
        self.btn_mgeridon.setObjectName("btn_mgeridon")
        self.verticalLayout_2.addWidget(self.btn_mgeridon)
        self.btn_mgrafik = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_mgrafik.sizePolicy().hasHeightForWidth())
        self.btn_mgrafik.setSizePolicy(sizePolicy)
        self.btn_mgrafik.setMinimumSize(QtCore.QSize(50, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_mgrafik.setFont(font)
        self.btn_mgrafik.setStyleSheet("background-color: rgb(111, 111, 111);\n"
"color: rgb(238, 119, 15);\n"
"border -radius : 5px")
        self.btn_mgrafik.setIconSize(QtCore.QSize(25, 25))
        self.btn_mgrafik.setObjectName("btn_mgrafik")
        self.verticalLayout_2.addWidget(self.btn_mgrafik)
        self.layoutWidget_2 = QtWidgets.QWidget(mudurmakina)
        self.layoutWidget_2.setGeometry(QtCore.QRect(30, 730, 130, 20))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_makinasayisi = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_makinasayisi.setFont(font)
        self.label_makinasayisi.setObjectName("label_makinasayisi")
        self.horizontalLayout_5.addWidget(self.label_makinasayisi)
        self.label_makinasonuc = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_makinasonuc.setFont(font)
        self.label_makinasonuc.setText("")
        self.label_makinasonuc.setObjectName("label_makinasonuc")
        self.horizontalLayout_5.addWidget(self.label_makinasonuc)
        self.groupBox = QtWidgets.QGroupBox(mudurmakina)
        self.groupBox.setGeometry(QtCore.QRect(10, 30, 811, 341))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(1024, 768))
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget_3 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget_3.setGeometry(QtCore.QRect(0, 20, 401, 301))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_model = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_model.setFont(font)
        self.label_model.setObjectName("label_model")
        self.horizontalLayout.addWidget(self.label_model)
        spacerItem = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lineEdit_model = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_model.setMaxLength(11)
        self.lineEdit_model.setObjectName("lineEdit_model")
        self.horizontalLayout.addWidget(self.lineEdit_model)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_sicaklik = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_sicaklik.setFont(font)
        self.label_sicaklik.setObjectName("label_sicaklik")
        self.horizontalLayout_2.addWidget(self.label_sicaklik)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.lineEdit_sicaklik = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_sicaklik.setMaxLength(20)
        self.lineEdit_sicaklik.setObjectName("lineEdit_sicaklik")
        self.horizontalLayout_2.addWidget(self.lineEdit_sicaklik)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_basinc = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_basinc.setFont(font)
        self.label_basinc.setObjectName("label_basinc")
        self.horizontalLayout_3.addWidget(self.label_basinc)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.lineEdit_basinc = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_basinc.setMaxLength(20)
        self.lineEdit_basinc.setObjectName("lineEdit_basinc")
        self.horizontalLayout_3.addWidget(self.lineEdit_basinc)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.cw_eklenmet = QtWidgets.QCalendarWidget(self.groupBox)
        self.cw_eklenmet.setGeometry(QtCore.QRect(410, 50, 391, 271))
        self.cw_eklenmet.setObjectName("cw_eklenmet")
        self.label_eklenmet = QtWidgets.QLabel(self.groupBox)
        self.label_eklenmet.setGeometry(QtCore.QRect(410, 10, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_eklenmet.setFont(font)
        self.label_eklenmet.setObjectName("label_eklenmet")
        self.tbWidget_bilgiler = QtWidgets.QTableWidget(mudurmakina)
        self.tbWidget_bilgiler.setGeometry(QtCore.QRect(120, 380, 681, 321))
        self.tbWidget_bilgiler.setRowCount(50)
        self.tbWidget_bilgiler.setColumnCount(4)
        self.tbWidget_bilgiler.setObjectName("tbWidget_bilgiler")

        self.retranslateUi(mudurmakina)
        QtCore.QMetaObject.connectSlotsByName(mudurmakina)

    def retranslateUi(self, mudurmakina):
        _translate = QtCore.QCoreApplication.translate
        mudurmakina.setWindowTitle(_translate("mudurmakina", "Form"))
        self.btn_mekle.setText(_translate("mudurmakina", "Makina Ekle"))
        self.btn_msil.setText(_translate("mudurmakina", "Makina Sil"))
        self.btn_mara.setText(_translate("mudurmakina", "Makina Ara"))
        self.btn_mguncel.setText(_translate("mudurmakina", "Güncelle"))
        self.btn_mgeridon.setText(_translate("mudurmakina", "Geri Dön"))
        self.btn_mgrafik.setText(_translate("mudurmakina", "Grafik Çiz"))
        self.label_makinasayisi.setText(_translate("mudurmakina", "Makina Sayısı :"))
        self.groupBox.setTitle(_translate("mudurmakina", "Makina Bilgileri"))
        self.label_model.setText(_translate("mudurmakina", "Makina Model :"))
        self.label_sicaklik.setText(_translate("mudurmakina", "Sıcaklık :"))
        self.label_basinc.setText(_translate("mudurmakina", "Basınç : "))
        self.label_eklenmet.setText(_translate("mudurmakina", "Eklenme Tarihi : "))
import icons_rc
