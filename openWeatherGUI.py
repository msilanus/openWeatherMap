# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'openWeather.ui'
#
# Created: Wed Jan 18 18:08:31 2017
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(638, 882)
        self.cbCities = QtGui.QComboBox(Dialog)
        self.cbCities.setGeometry(QtCore.QRect(230, 30, 291, 33))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(12)
        self.cbCities.setFont(font)
        self.cbCities.setObjectName(_fromUtf8("cbCities"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 30, 201, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(119, 143, 211, 36))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(534, 30, 91, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(130, 186, 201, 36))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(130, 228, 201, 36))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(130, 270, 201, 36))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lblPression = QtGui.QLabel(Dialog)
        self.lblPression.setGeometry(QtCore.QRect(130, 312, 201, 36))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.lblPression.setFont(font)
        self.lblPression.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblPression.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblPression.setObjectName(_fromUtf8("lblPression"))
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(130, 354, 201, 36))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(130, 396, 201, 36))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(130, 438, 201, 36))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(339, 143, 221, 332))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.layoutWidget.setFont(font)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lblTemp = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.lblTemp.setFont(font)
        self.lblTemp.setObjectName(_fromUtf8("lblTemp"))
        self.verticalLayout.addWidget(self.lblTemp)
        self.lblHum = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.lblHum.setFont(font)
        self.lblHum.setObjectName(_fromUtf8("lblHum"))
        self.verticalLayout.addWidget(self.lblHum)
        self.lblVent = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.lblVent.setFont(font)
        self.lblVent.setObjectName(_fromUtf8("lblVent"))
        self.verticalLayout.addWidget(self.lblVent)
        self.lblDir = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.lblDir.setFont(font)
        self.lblDir.setObjectName(_fromUtf8("lblDir"))
        self.verticalLayout.addWidget(self.lblDir)
        self.lblPress = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.lblPress.setFont(font)
        self.lblPress.setObjectName(_fromUtf8("lblPress"))
        self.verticalLayout.addWidget(self.lblPress)
        self.lblNuages = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.lblNuages.setFont(font)
        self.lblNuages.setObjectName(_fromUtf8("lblNuages"))
        self.verticalLayout.addWidget(self.lblNuages)
        self.lblPluie = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.lblPluie.setFont(font)
        self.lblPluie.setObjectName(_fromUtf8("lblPluie"))
        self.verticalLayout.addWidget(self.lblPluie)
        self.lblNeige = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.lblNeige.setFont(font)
        self.lblNeige.setObjectName(_fromUtf8("lblNeige"))
        self.verticalLayout.addWidget(self.lblNeige)
        self.lblLocalisation = QtGui.QLabel(Dialog)
        self.lblLocalisation.setGeometry(QtCore.QRect(10, 100, 621, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lblLocalisation.setFont(font)
        self.lblLocalisation.setAlignment(QtCore.Qt.AlignCenter)
        self.lblLocalisation.setObjectName(_fromUtf8("lblLocalisation"))
        self.lblSymbole = QtGui.QLabel(Dialog)
        self.lblSymbole.setGeometry(QtCore.QRect(140, 490, 381, 281))
        self.lblSymbole.setFrameShape(QtGui.QFrame.Box)
        self.lblSymbole.setLineWidth(2)
        self.lblSymbole.setText(_fromUtf8(""))
        self.lblSymbole.setPixmap(QtGui.QPixmap(_fromUtf8("soleil.png")))
        self.lblSymbole.setAlignment(QtCore.Qt.AlignCenter)
        self.lblSymbole.setObjectName(_fromUtf8("lblSymbole"))
        self.lblTempRessLink = QtGui.QLabel(Dialog)
        self.lblTempRessLink.setGeometry(QtCore.QRect(30, 790, 331, 36))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.lblTempRessLink.setFont(font)
        self.lblTempRessLink.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblTempRessLink.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblTempRessLink.setObjectName(_fromUtf8("lblTempRessLink"))
        self.lblTempRessentie = QtGui.QLabel(Dialog)
        self.lblTempRessentie.setGeometry(QtCore.QRect(380, 790, 219, 36))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.lblTempRessentie.setFont(font)
        self.lblTempRessentie.setObjectName(_fromUtf8("lblTempRessentie"))
        self.lblHiLink = QtGui.QLabel(Dialog)
        self.lblHiLink.setGeometry(QtCore.QRect(30, 830, 331, 36))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.lblHiLink.setFont(font)
        self.lblHiLink.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblHiLink.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblHiLink.setObjectName(_fromUtf8("lblHiLink"))
        self.lblHI = QtGui.QLabel(Dialog)
        self.lblHI.setGeometry(QtCore.QRect(380, 830, 219, 36))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.lblHI.setFont(font)
        self.lblHI.setObjectName(_fromUtf8("lblHI"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.pbModifier)
        QtCore.QObject.connect(self.lblTempRessLink, QtCore.SIGNAL(_fromUtf8("linkActivated(QString)")), Dialog.goToWikiRefroidissementEolien)
        QtCore.QObject.connect(self.lblHiLink, QtCore.SIGNAL(_fromUtf8("linkActivated(QString)")), Dialog.goToWikiIndiceChaleur)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Météo dans ma ville", None))
        self.label.setText(_translate("Dialog", "Choisissez une ville :", None))
        self.label_2.setText(_translate("Dialog", "Température :", None))
        self.pushButton.setText(_translate("Dialog", "Modifier", None))
        self.label_3.setText(_translate("Dialog", "Humidité :", None))
        self.label_4.setText(_translate("Dialog", "Vent :", None))
        self.label_5.setText(_translate("Dialog", "Direction :", None))
        self.lblPression.setText(_translate("Dialog", "Pression :", None))
        self.label_7.setText(_translate("Dialog", "Nuages :", None))
        self.label_8.setText(_translate("Dialog", "Pluie :", None))
        self.label_9.setText(_translate("Dialog", "Neige :", None))
        self.lblTemp.setText(_translate("Dialog", "--.-- °C", None))
        self.lblHum.setText(_translate("Dialog", "--.-- %", None))
        self.lblVent.setText(_translate("Dialog", "--.-- m/s", None))
        self.lblDir.setText(_translate("Dialog", "--.-- °", None))
        self.lblPress.setText(_translate("Dialog", "--.-- hPa", None))
        self.lblNuages.setText(_translate("Dialog", "--.-- %", None))
        self.lblPluie.setText(_translate("Dialog", "--.-- mm", None))
        self.lblNeige.setText(_translate("Dialog", "--.-- mm", None))
        self.lblLocalisation.setText(_translate("Dialog", "Météo  ", None))
        self.lblTempRessLink.setText(_translate("Dialog", "<html><head/><body><p><a href=\"https://fr.wikipedia.org/wiki/Refroidissement_éolien\"><span style=\" text-decoration: underline; color:#0000ff;\">Température ressentie :</span></a></p></body></html>", None))
        self.lblTempRessentie.setText(_translate("Dialog", "--.-- °C", None))
        self.lblHiLink.setText(_translate("Dialog", "<html><head/><body><p><a href=\"https://fr.wikipedia.org/wiki/Indice_de_chaleur\"><span style=\" text-decoration: underline; color:#0000ff;\">Indice de chaleur :</span></a></p></body></html>", None))
        self.lblHI.setText(_translate("Dialog", "--.-- °C", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

