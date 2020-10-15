from PyQt5 import QtWidgets
from PyQt5.QtCore import QDate, QTime, QTimer
from PyQt5.QtWidgets import (QApplication, QWidget, QMessageBox, QListWidget, QErrorMessage)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

import sys
import datetime
import json
import time

from main_.PyQt___window import Ui_Testing  # импорт нашего сгенерированного файла
from main_.info_test import info  # импорт модуля
from main_.results import test_results  # В модуле расчитываеться результат тестирования.

# Глабальные переменые:
ind = -1
ind_v = 0
# Список ответов на вопросы.
recording_the_response = []
# Время на прохождения тестирования по умолчанию.
time_ = 900
time_report_ = 0
# Количество вопросов на тестировании.
number_of_questions = 10


class mywindow(QtWidgets.QMainWindow, QWidget):

    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_Testing()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('/home/denis-linux/Загрузки/111.png'))
        button = self.ui.pushButton_3
        button.setToolTip('Следующий вопрос.')
        button.setIcon(QIcon('/home/denis-linux/Загрузки/111.png'))
        button.setIconSize(QSize(30,30))

        button_1 = self.ui.pushButton_2
        button_1.setToolTip('Предыдущий вопрос.')
        button_1.setIcon(QIcon('/home/denis-linux/Загрузки/113.png'))
        button_1.setIconSize(QSize(30, 30))

        # Устанавливаем заначения даты и время по умолчанию.
        date_ = QDate(datetime.datetime.today())
        self.ui.dateEdit.setDate(date_)
        time_ = QTime(datetime.datetime.now().time())
        self.ui.timeEdit.setTime(time_)
        # Время на прохождения теста.
        self.timer = QTimer(self)

        tests = ["","Менедер по оптовым продажам","Менеджер по закупкам","Товаровед",
                 "Старший кладовщик","Офис менеджер"]
        for i in tests:
            self.ui.Box.addItem(i)

        test_subgroup = ["Полноценный тест","Экспресс тест"]
        for i in test_subgroup:
            self.ui.Box_2.addItem(i)

        self.ui.Box.activated.connect(self.info_test)

        # Действия при нажаните на кнопку "Начать тест".
        self.ui.pushButton.clicked.connect(self.passing_the_test)
        # Переход на новый вопрос.
        self.ui.pushButton_3.clicked.connect(self.number_of_responses)
        #  Переход к предыдущему вопросу.
        self.ui.pushButton_2.clicked.connect(self.previous_question)


    def info_test(self):
        """
        При изменении элемента в comboBox отображаем информацио о
        тестировании (количество вопросов,максимальное время прохождения теста)
        """
        global time_,number_of_questions,time_report_
        show_info = info(self)
        try:
            time_ = show_info[0]
            time_report_ = show_info[0]
            number_of_questions = show_info[1]
        except:
            self.ui.info.setText('Выберите пожалуйста тест для прохождения!!!!')


    def passing_the_test(self):
        if self.ui.lineEdit.text() == '' or self.ui.lineEdit_2.text() == '':
            self.connectError()
        else:
            self.ui.tabWidget.setCurrentIndex(1)
            self.following_question()
            # Создаем обратный отчет времени.
            self.timer.timeout.connect(self.time_report)
            self.start_time()
            a = time.strftime("%M:%S", time.localtime(time_))
            self.ui.lcdNumber.setNumDigits(5)
            self.ui.lcdNumber.display(a)

    def connectError(self):

        text = 'Пример заполнения полей :\n' \
               '"Смирнов Игорь Сегревич "\n' \
               '"ИвЭнергоСбыт"'
        input_error = QErrorMessage()
        input_error.showMessage(text)
        input_error.exec()

    #  Следующий вопрос.
    def following_question(self):
        global ind
        if ind == -1:
            pass
        else:
            self.track_responses()
        ind += 1
        if ind < 10:
            # Получаем данные из json файла.
            with open('vopros.json', 'r')as f:
                data_json = json.load(f)
                question = data_json[ind]['question']
                option_1 = data_json[ind]['option_1']
                option_2 = data_json[ind]['option_2']
                option_3 = data_json[ind]['option_3']
                try:
                    option_4 = data_json[ind]['option_4']
                except KeyError:
                    option_4 = 'Не знаю.'

            self.ui.label_7.setText(question)
            self.ui.label_8.setText(option_1)
            self.ui.label_9.setText(option_2)
            self.ui.label_10.setText(option_3)
            self.ui.label_11.setText(option_4)

        else:
            self.ui.tabWidget.setCurrentIndex(2)
            self.test_results()
            self.timer.stop()

    def number_of_responses(self):
        # Проверяем число ответов.(должно быть неболее 1 ответа на 1 вопрос).
        answer = self.reading_the_selected_response()
        quantity = 0
        for i in answer:
            if i:
                quantity += 1
        if quantity == 0:
            self.ui.warning.setText('Выберите один вариант ответа на вопрос !!! ')
        elif quantity >= 2:
            self.ui.warning.setText('Выберите только один вариант ответа на вопрос !!! ')
        else:
            self.ui.warning.setText('')
            self.following_question()

    # Предыдущий вопрос.
    def previous_question(self):
        global ind, ind_v
        ind -= 1
        if ind > - 1:
            ind_v -= 1
            self.step_back(ind_v)
            self.reset_the_response()
            self.deleting_the_last_entry()
            # Получаем данные из json файла.
            with open('vopros.json', 'r')as f:
                data_json = json.load(f)
                question = data_json[ind]['question']
                option_1 = data_json[ind]['option_1']
                option_2 = data_json[ind]['option_2']
                option_3 = data_json[ind]['option_3']
                try:
                    option_4 = data_json[ind]['option_4']
                except KeyError:
                    option_4 = 'Не знаю.'

            self.ui.label_7.setText(question)
            self.ui.label_8.setText(option_1)
            self.ui.label_9.setText(option_2)
            self.ui.label_10.setText(option_3)
            self.ui.label_11.setText(option_4)

        else:
            ind = 0

    def start_time(self):
        self.timer.start(1000)

    def time_report(self):
        global time_,time_report_
        time_-= 1
        a = time.strftime("%M:%S", time.localtime(time_))
        self.ui.lcdNumber.setNumDigits(5)
        self.ui.lcdNumber.display(a)

    def track_responses(self):
        global recording_the_response, ind_v
        # Получем ответ
        checked = self.reading_the_selected_response()
        ind_checked = 1
        for i in checked:
            if i:
                recording_the_response.append(ind_checked)
            ind_checked += 1
        # Очищаем все варианты ответа.
        self.reset_the_response()
        self.step_forward(ind_v)
        ind_v += 1

    def reading_the_selected_response(self):
        # Создаем список из вариантов ответаб и возвращаем его.
        read_the_response = [self.ui.v_1.isChecked(), self.ui.v_2.isChecked(),
                             self.ui.v_3.isChecked(), self.ui.v_4.isChecked()]

        return read_the_response

    def reset_the_response(self):
        # Обнуляем все варианты ответов
        self.ui.v_1.setChecked(False)
        self.ui.v_2.setChecked(False)
        self.ui.v_3.setChecked(False)
        self.ui.v_4.setChecked(False)

    def step_forward(self, ind_v):
        movement = True
        self.step(movement)

    def step_back(self, ind_v):
        movement = False
        self.step(movement)
    def step(self,movement):

        v = [self.ui.check_1, self.ui.check_2, self.ui.check_3, self.ui.check_4, self.ui.check_5,
             self.ui.check_6, self.ui.check_7, self.ui.check_8, self.ui.check_9, self.ui.check_10]
        if movement:
            v[ind].setChecked(True)
        else:
            v[ind].setChecked(False)

    def deleting_the_last_entry(self):
        # При нажатии кнопки "Предыдущий вопрос" удаляем последний ответ на вопрос.
        global recording_the_response
        del_ = recording_the_response.pop()


    def checking_the_correct_answer(self, ind_checked=0):
        """
        Проверяем правильность ответа,
        "Зеленым цветом" указываем правильный ответ,
        "Красным цветом" указываем НЕправильный ответ
        """


    def test_results(self):
        # С помощью этого модуля выводим результат тестирования.
        global recording_the_response,time_,number_of_questions,time_report_
        time_ = time_report_ - time_
        user_test = self.ui.Box.currentText()
        user = self.ui.lineEdit.text()
        test_results(self,recording_the_response,number_of_questions,time_,time_report_,user_test
                     ,user)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()

    sys.exit(app.exec())