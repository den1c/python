
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Testing(object):
    def setupUi(self, Testing):
        Testing.setObjectName("Testing")
        Testing.resize(751, 640)
        self.centralwidget = QtWidgets.QWidget(Testing)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(-20, -50, 791, 711))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(100, 40, 571, 61))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(90, 200, 601, 71))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(190, 470, 401, 61))
        self.pushButton.setObjectName("pushButton")
        self.splitter_6 = QtWidgets.QSplitter(self.tab)
        self.splitter_6.setGeometry(QtCore.QRect(180, 295, 521, 71))
        self.splitter_6.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_6.setObjectName("splitter_6")
        self.splitter_3 = QtWidgets.QSplitter(self.splitter_6)
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.splitter = QtWidgets.QSplitter(self.splitter_3)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.lineEdit = QtWidgets.QLineEdit(self.splitter)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_3)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.splitter_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.splitter_4 = QtWidgets.QSplitter(self.tab)
        self.splitter_4.setGeometry(QtCore.QRect(80, 400, 621, 21))
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.label_5 = QtWidgets.QLabel(self.splitter_4)
        self.label_5.setObjectName("label_5")
        self.dateEdit = QtWidgets.QDateEdit(self.splitter_4)
        self.dateEdit.setObjectName("dateEdit")
        self.label_6 = QtWidgets.QLabel(self.splitter_4)
        self.label_6.setObjectName("label_6")
        self.timeEdit = QtWidgets.QTimeEdit(self.splitter_4)
        self.timeEdit.setObjectName("timeEdit")
        self.splitter_5 = QtWidgets.QSplitter(self.tab)
        self.splitter_5.setGeometry(QtCore.QRect(83, 300, 101, 61))
        self.splitter_5.setOrientation(QtCore.Qt.Vertical)
        self.splitter_5.setObjectName("splitter_5")
        self.label_3 = QtWidgets.QLabel(self.splitter_5)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.splitter_5)
        self.label_4.setObjectName("label_4")
        self.Box = QtWidgets.QComboBox(self.tab)
        self.Box.setGeometry(QtCore.QRect(80, 100, 411, 41))
        self.Box.setCurrentText("")
        self.Box.setObjectName("Box")
        self.info = QtWidgets.QLabel(self.tab)
        self.info.setGeometry(QtCore.QRect(110, 170, 561, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(True)
        self.info.setFont(font)
        self.info.setText("")
        self.info.setAlignment(QtCore.Qt.AlignCenter)
        self.info.setObjectName("info")
        self.Box_2 = QtWidgets.QComboBox(self.tab)
        self.Box_2.setGeometry(QtCore.QRect(502, 100, 191, 41))
        self.Box_2.setObjectName("Box_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(100, 30, 581, 191))
        self.label_7.setFrameShape(QtWidgets.QFrame.Box)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.splitter_7 = QtWidgets.QSplitter(self.tab_2)
        self.splitter_7.setGeometry(QtCore.QRect(100, 240, 41, 141))
        self.splitter_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.splitter_7.setOrientation(QtCore.Qt.Vertical)
        self.splitter_7.setObjectName("splitter_7")
        self.v_1 = QtWidgets.QCheckBox(self.splitter_7)
        self.v_1.setObjectName("v_1")
        self.v_2 = QtWidgets.QCheckBox(self.splitter_7)
        self.v_2.setObjectName("v_2")
        self.v_3 = QtWidgets.QCheckBox(self.splitter_7)
        self.v_3.setObjectName("v_3")
        self.v_4 = QtWidgets.QCheckBox(self.splitter_7)
        self.v_4.setObjectName("v_4")
        self.splitter_8 = QtWidgets.QSplitter(self.tab_2)
        self.splitter_8.setGeometry(QtCore.QRect(150, 240, 531, 141))
        self.splitter_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.splitter_8.setOrientation(QtCore.Qt.Vertical)
        self.splitter_8.setObjectName("splitter_8")
        self.label_8 = QtWidgets.QLabel(self.splitter_8)
        self.label_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.splitter_8)
        self.label_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.splitter_8)
        self.label_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.splitter_8)
        self.label_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.splitter_9 = QtWidgets.QSplitter(self.tab_2)
        self.splitter_9.setGeometry(QtCore.QRect(80, 580, 631, 21))
        self.splitter_9.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_9.setObjectName("splitter_9")
        self.check_1 = QtWidgets.QCheckBox(self.splitter_9)
        self.check_1.setChecked(False)
        self.check_1.setObjectName("check_1")
        self.check_2 = QtWidgets.QCheckBox(self.splitter_9)
        self.check_2.setObjectName("check_2")
        self.check_3 = QtWidgets.QCheckBox(self.splitter_9)
        self.check_3.setObjectName("check_3")
        self.check_4 = QtWidgets.QCheckBox(self.splitter_9)
        self.check_4.setObjectName("check_4")
        self.check_5 = QtWidgets.QCheckBox(self.splitter_9)
        self.check_5.setObjectName("check_5")
        self.check_6 = QtWidgets.QCheckBox(self.splitter_9)
        self.check_6.setObjectName("check_6")
        self.check_7 = QtWidgets.QCheckBox(self.splitter_9)
        self.check_7.setObjectName("check_7")
        self.check_8 = QtWidgets.QCheckBox(self.splitter_9)
        self.check_8.setObjectName("check_8")
        self.check_9 = QtWidgets.QCheckBox(self.splitter_9)
        self.check_9.setObjectName("check_9")
        self.check_10 = QtWidgets.QCheckBox(self.splitter_9)
        self.check_10.setObjectName("check_10")
        self.splitter_10 = QtWidgets.QSplitter(self.tab_2)
        self.splitter_10.setGeometry(QtCore.QRect(120, 450, 551, 43))
        self.splitter_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.splitter_10.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_10.setObjectName("splitter_10")
        self.pushButton_2 = QtWidgets.QPushButton(self.splitter_10)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.splitter_10)
        self.pushButton_3.setObjectName("pushButton_3")
        self.warning = QtWidgets.QLabel(self.tab_2)
        self.warning.setGeometry(QtCore.QRect(150, 390, 531, 20))
        self.warning.setLineWidth(50)
        self.warning.setText("")
        self.warning.setObjectName("warning")
        self.lcdNumber = QtWidgets.QLCDNumber(self.tab_2)
        self.lcdNumber.setGeometry(QtCore.QRect(290, 500, 231, 41))
        self.lcdNumber.setObjectName("lcdNumber")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_12 = QtWidgets.QLabel(self.tab_3)
        self.label_12.setGeometry(QtCore.QRect(100, 0, 571, 161))
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tab_3)
        self.label_13.setGeometry(QtCore.QRect(100, 120, 571, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.result = QtWidgets.QLabel(self.tab_3)
        self.result.setGeometry(QtCore.QRect(240, 230, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setItalic(True)
        self.result.setFont(font)
        self.result.setAlignment(QtCore.Qt.AlignCenter)
        self.result.setObjectName("result")
        self.splitter_11 = QtWidgets.QSplitter(self.tab_3)
        self.splitter_11.setGeometry(QtCore.QRect(30, 180, 721, 41))
        self.splitter_11.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_11.setObjectName("splitter_11")
        self.label_14 = QtWidgets.QLabel(self.splitter_11)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.correct_answer = QtWidgets.QLCDNumber(self.splitter_11)
        self.correct_answer.setObjectName("correct_answer")
        self.label_15 = QtWidgets.QLabel(self.splitter_11)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.sum_of_correct_answers = QtWidgets.QLCDNumber(self.splitter_11)
        self.sum_of_correct_answers.setObjectName("sum_of_correct_answers")
        self.label_16 = QtWidgets.QLabel(self.splitter_11)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.ime_t = QtWidgets.QLCDNumber(self.splitter_11)
        self.ime_t.setObjectName("ime_t")
        self.splitter_12 = QtWidgets.QSplitter(self.tab_3)
        self.splitter_12.setGeometry(QtCore.QRect(100, 590, 551, 41))
        self.splitter_12.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_12.setObjectName("splitter_12")
        self.pushButton_5 = QtWidgets.QPushButton(self.splitter_12)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_4 = QtWidgets.QPushButton(self.splitter_12)
        self.pushButton_4.setObjectName("pushButton_4")
        self.widget = QtWidgets.QWidget(self.tab_3)
        self.widget.setGeometry(QtCore.QRect(60, 310, 661, 231))
        self.widget.setObjectName("widget")
        self.tabWidget.addTab(self.tab_3, "")
        Testing.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Testing)
        self.statusbar.setObjectName("statusbar")
        Testing.setStatusBar(self.statusbar)

        self.retranslateUi(Testing)
        QtCore.QMetaObject.connectSlotsByName(Testing)

    def retranslateUi(self, Testing):
        _translate = QtCore.QCoreApplication.translate
        Testing.setWindowTitle(_translate("Testing", "MainWindow"))
        self.label.setText(_translate("Testing", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">Тест по повышению классификации :</span></p><p align=\"center\"><br/></p></body></html>"))
        self.label_2.setText(_translate("Testing", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Заполните все поля для прохождения теста.</span></p><p align=\"center\"><span style=\" font-size:16pt;\">Fill in all the fields to pass the test.</span></p></body></html>"))
        self.pushButton.setText(_translate("Testing", "Начать тест."))
        self.label_5.setText(_translate("Testing", "<html><head/><body><p><span style=\" font-size:12pt;\">Дата прохождения теста :</span></p><p><br/></p></body></html>"))
        self.label_6.setText(_translate("Testing", "<html><head/><body><p><span style=\" font-size:12pt;\">Время начала тестирования :</span></p></body></html>"))
        self.label_3.setText(_translate("Testing", "<html><head/><body><p><span style=\" font-size:12pt;\">Ф.И.О.</span></p><p><br/></p></body></html>"))
        self.label_4.setText(_translate("Testing", "<html><head/><body><p><span style=\" font-size:12pt;\">Компания .</span></p><p><br/></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Testing", "Tab 1"))
        self.label_7.setText(_translate("Testing", "TextLabel"))
        self.v_1.setText(_translate("Testing", "1."))
        self.v_2.setText(_translate("Testing", "2."))
        self.v_3.setText(_translate("Testing", "3."))
        self.v_4.setText(_translate("Testing", "4."))
        self.check_1.setText(_translate("Testing", "1"))
        self.check_2.setText(_translate("Testing", "2"))
        self.check_3.setText(_translate("Testing", "3"))
        self.check_4.setText(_translate("Testing", "4"))
        self.check_5.setText(_translate("Testing", "5"))
        self.check_6.setText(_translate("Testing", "6"))
        self.check_7.setText(_translate("Testing", "7"))
        self.check_8.setText(_translate("Testing", "8"))
        self.check_9.setText(_translate("Testing", "9"))
        self.check_10.setText(_translate("Testing", "10"))
        self.pushButton_2.setText(_translate("Testing", "Предыдущий вопрос.\n"
"Previous question."))
        self.pushButton_3.setText(_translate("Testing", "Следующий вопрос.\n"
"Following question."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Testing", "Tab 2"))
        self.label_12.setText(_translate("Testing", "<html><head/><body><p><span style=\" font-size:14pt; color:#0055ff;\">Поздравляем Вас Морозов Денис.</span></p><p><span style=\" font-size:14pt; color:#0055ff;\">Вы успешно прошли тестирование, по повышению классификации</span></p><p><span style=\" font-size:14pt; color:#0055ff;\">&quot;Менедер по оптовым продажам&quot;.</span></p></body></html>"))
        self.label_13.setText(_translate("Testing", "Итоги тестирования :"))
        self.result.setText(_translate("Testing", "Отлично."))
        self.label_14.setText(_translate("Testing", "Вопросов было :"))
        self.label_15.setText(_translate("Testing", "Правильных ответов :"))
        self.label_16.setText(_translate("Testing", "Затрачено времени :"))
        self.pushButton_5.setText(_translate("Testing", "Начать заново."))
        self.pushButton_4.setText(_translate("Testing", "Закрыть."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Testing", "Страница"))