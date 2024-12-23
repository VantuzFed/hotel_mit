# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reg_client.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLayout,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 600)
        Form.setMinimumSize(QSize(800, 600))
        Form.setMaximumSize(QSize(800, 600))
        palette = QPalette()
        brush = QBrush(QColor(225, 208, 169, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(46, 44, 43, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(69, 66, 65, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(57, 55, 54, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(23, 22, 22, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(31, 29, 29, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        brush6 = QBrush(QColor(215, 201, 163, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        brush7 = QBrush(QColor(36, 34, 33, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush8 = QBrush(QColor(0, 0, 0, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush8)
        brush9 = QBrush(QColor(167, 164, 0, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush9)
        brush10 = QBrush(QColor(23, 22, 21, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush10)
        brush11 = QBrush(QColor(255, 255, 220, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush8)
        brush12 = QBrush(QColor(255, 255, 255, 127))
        brush12.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        brush13 = QBrush(QColor(239, 239, 239, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush13)
        brush14 = QBrush(QColor(255, 255, 255, 255))
        brush14.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush14)
        brush15 = QBrush(QColor(202, 202, 202, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush15)
        brush16 = QBrush(QColor(159, 159, 159, 255))
        brush16.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush16)
        brush17 = QBrush(QColor(184, 184, 184, 255))
        brush17.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush17)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush14)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush14)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush13)
        brush18 = QBrush(QColor(118, 118, 118, 255))
        brush18.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush18)
        brush19 = QBrush(QColor(48, 140, 198, 255))
        brush19.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush19)
        brush20 = QBrush(QColor(247, 247, 247, 255))
        brush20.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush20)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush8)
        brush21 = QBrush(QColor(0, 0, 0, 128))
        brush21.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush21)
#endif
        brush22 = QBrush(QColor(135, 124, 100, 255))
        brush22.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush22)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush22)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush22)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush23 = QBrush(QColor(177, 177, 177, 255))
        brush23.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush23)
        brush24 = QBrush(QColor(145, 145, 145, 255))
        brush24.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush24)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush20)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush21)
#endif
        Form.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Rubik"])
        Form.setFont(font)
        self.button = QPushButton(Form)
        self.button.setObjectName(u"button")
        self.button.setGeometry(QRect(0, 2, 80, 25))
        self.button_reg = QPushButton(Form)
        self.button_reg.setObjectName(u"button_reg")
        self.button_reg.setGeometry(QRect(339, 477, 141, 25))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(98, 40, 631, 171))
        font1 = QFont()
        font1.setFamilies([u"Rubik"])
        font1.setPointSize(48)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(237, 290, 341, 164))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.ent_email = QLineEdit(self.layoutWidget)
        self.ent_email.setObjectName(u"ent_email")
        self.ent_email.setEchoMode(QLineEdit.EchoMode.Normal)

        self.gridLayout.addWidget(self.ent_email, 3, 1, 1, 1)

        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 2, 1, 1, 1)

        self.ent_phone = QLineEdit(self.layoutWidget)
        self.ent_phone.setObjectName(u"ent_phone")
        self.ent_phone.setEchoMode(QLineEdit.EchoMode.Normal)

        self.gridLayout.addWidget(self.ent_phone, 5, 0, 1, 1)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)

        self.ent_lname = QLineEdit(self.layoutWidget)
        self.ent_lname.setObjectName(u"ent_lname")

        self.gridLayout.addWidget(self.ent_lname, 3, 0, 1, 1)

        self.ent_mname = QLineEdit(self.layoutWidget)
        self.ent_mname.setObjectName(u"ent_mname")

        self.gridLayout.addWidget(self.ent_mname, 1, 1, 1, 1)

        self.ent_doc_id = QLineEdit(self.layoutWidget)
        self.ent_doc_id.setObjectName(u"ent_doc_id")
        self.ent_doc_id.setEnabled(True)

        self.gridLayout.addWidget(self.ent_doc_id, 5, 1, 1, 1)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 4, 1, 1, 1)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 0, 1, 1, 1)

        self.ent_fname = QLineEdit(self.layoutWidget)
        self.ent_fname.setObjectName(u"ent_fname")

        self.gridLayout.addWidget(self.ent_fname, 1, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f \u043a\u043b\u0438\u0435\u043d\u0442\u0430", None))
        self.button.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.button_reg.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0424\u043e\u0440\u043c\u0430 \u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u0438\n"
"\u041a\u043b\u0438\u0435\u043d\u0442\u0430", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"E-mail:", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u0418\u043c\u044f:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u041f\u0430\u0441\u043f\u043e\u0440\u0442\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435:", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e:", None))
    # retranslateUi

