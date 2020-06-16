from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import (QApplication, QWidget, QDialog)
import sys
from PyQt5.Qt import Qt
from PyQt5.QtGui import QIcon, QKeyEvent

from translation.main_Qt import Ui_MainWindow  # импорт нашего сгенерированного файла
from translation.list_of_languages import start_of_scrubbing

class mywindow(QtWidgets.QMainWindow, QWidget):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_2.setDisabled(True)
        self.ui.textEdit_2.setText('cdcdcdcdcfvfvfvfv')
        self.setWindowTitle('PyQt Translator')
        self.setWindowIcon(QIcon('st.png'))
        # Заполняем картинкаим кнопки.
        self.button_icon()
        # подсчет количества символов и отображение.
        self.counting_the_number_of_letters()
        # Установливаем значение по умолчанию.
        self.ui.comboBox.addItem('Русский')
        self.ui.comboBox_2.addItem('Английский')
        self.getting_a_selection()
        # Заполняем выбор языка для работы с ними.
        self.completions_comboBox()
        # ///////
        self.dialog = Dialog(self)
        self.ui.pushButton.clicked.connect(self.dialog.exec)
        # ///
        # Вычисляем выбраное значение пользователя.(после каждого изменения)
        self.ui.comboBox.activated.connect(self.getting_a_selection)
        self.ui.comboBox_2.activated.connect(self.getting_a_selection)


    def button_icon(self):
        # Устанавливаем картинкив кнопках.
        self.ui.pushButton_2.setIcon(QIcon('close.png'))
        self.ui.pushButton_2.setIconSize(QSize(40,40))
        self.ui.pushButton_2.clicked.connect(self.clear)
        self.ui.pushButton_3.setIcon(QIcon('icons8.png'))
        self.ui.pushButton_3.setIconSize(QSize(40, 40))
        self.ui.pushButton_4.setIcon(QIcon('icon4.png'))
        self.ui.pushButton_4.setIconSize(QSize(40, 40))

    def counting_the_number_of_letters(self):
        # подсчет количества символов и отображение
        quantity = len(self.ui.textEdit_2.toPlainText())
        self.ui.label.setText('{0}/1000'.format(quantity))

    def clear(self):
        # Очищаем модуль ввода.
        self.ui.textEdit_2.clear()
        self.counting_the_number_of_letters()


    def keyPressEvent(self, event):
        print(555)


    def completions_comboBox(self):
        # Заполняем выбор языка для работы с ними.
        language = start_of_scrubbing()
        for i in language:
            self.ui.comboBox.addItem(i)
            self.ui.comboBox_2.addItem(i)

    def getting_a_selection(self):
        # Вычисляем выбраное значение пользователем из comboBox.
        self.value_1 = self.ui.comboBox.currentText()
        self.value_2 = self.ui.comboBox_2.currentText()




class Dialog(QtWidgets.QDialog):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        self.main = root

        self.setWindowTitle('Выберите одно значение')
        self.setGeometry(320,350,600,200)





app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())