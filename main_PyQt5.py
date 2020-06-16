from functools import partial

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QSplashScreen, QDialog, QVBoxLayout, QHBoxLayout, \
    QLabel, QPushButton, QComboBox, QLineEdit, QLCDNumber
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import time
import json
import random

from hero_Qt._pyqt5__ import Ui_hero

class The_choice_of_the_hero(QDialog):
    """
    Диалоговое окно для выбора персонажа.
    Отображаеться 4 персонажа и их характиристики,
    небольшое описание персонажа можно получить при наведении мышки на персонажа.

    """
    def __init__(self):
        super().__init__()
        self.ui_hero()
        self.show()

    def ui_hero(self):

        self.setWindowTitle('Выберите пожалуйста персонажа ')
        self.resize(500,150)

        choice_hero = []
        ind_hero = 0
        with open('info_hero.json', 'r')as fr:
            text = json.load(fr)

        for i in range(4):
            # Создание вертикального группировки модулей.
            self.vbox = QVBoxLayout()
            self.pixmap = QPixmap(str(text[ind_hero]['foto']))
            self.hero = QLabel()
            self.hero.setToolTip((str(text[ind_hero]['info'])))
            self.hero.setPixmap(self.pixmap)
            self.hero_info = QLabel('Имя : {0}'.format(text[ind_hero]['name']))
            # Создание горизонтальной группировки модулей.
            self.hbox = QHBoxLayout()
            self.characteristic1 = QPixmap('h1.png')
            self.characteristic2 = QPixmap('h2.png')
            self.characteristic3 = QPixmap('h3.png')
            self.characteristic4 = QPixmap('h4.jpg')
            self.c_h1 = QLabel()
            self.c_h1.setToolTip('Атака {0}'.format(text[ind_hero]['attack']))
            self.c_h1.setPixmap(self.characteristic1)
            self.c_h2 = QLabel()
            self.c_h2.setToolTip('Защита {0}'.format(text[ind_hero]['protection']))
            self.c_h2.setPixmap(self.characteristic2)
            self.c_h3 = QLabel()
            self.c_h3.setToolTip('Сила {0}'.format(text[ind_hero]['force']))
            self.c_h3.setPixmap(self.characteristic3)
            self.c_h4 = QLabel()
            self.c_h4.setToolTip('Энергия {0}'.format(text[ind_hero]['energy']))
            self.c_h4.setPixmap(self.characteristic4)
            # Упаковка характиристик в горизонтальный блок.
            self.hbox.addWidget(self.c_h1)
            self.hbox.addWidget(self.c_h2)
            self.hbox.addWidget(self.c_h3)
            self.hbox.addWidget(self.c_h4)
            # Создание кнопки выбора персонажа.
            self.btn = QPushButton('Выбрать героя')
            self.btn.clicked.connect(partial(self.exit_The_choice_of_the_hero,ind_hero))

            # Упаковка вертикальном положении.
            self.vbox.addWidget(self.hero)
            self.vbox.addWidget(self.hero_info)
            self.vbox.addLayout(self.hbox)
            self.vbox.addWidget(self.btn)

            choice_hero.append(self.vbox)

            ind_hero +=1

        # Отображение всех модулей.
        box_hor = QHBoxLayout()
        for i in choice_hero:
            box_hor.addLayout(i)

        self.setLayout(box_hor)

    def exit_The_choice_of_the_hero(self,selected_hero):
        """
        Закрываем диалоговое окно" ВЫбор персонажа",
        передаем параметром какаго персонажа выбрал пользователь.
        После этого выполняеться загрузка главного окна и загрузка всех характиристик персонажа.
        """
        self.close()
        self.selected_hero = selected_hero

class Window(QtWidgets.QMainWindow, QWidget):
    """"
    Класс главного окна.

    """
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_hero()
        self.ui.setupUi(self)
        self.ui_window()

    def ui_window(self):
        # Обрисовываем две кнопки (кросок кубиков и сундук )
        self.dialog = Dialog_cubes()
        self.ui.pushButton_4.clicked.connect(self.dialog.exec)
        self.ui.pushButton_4.setIcon(QIcon('3971-4.jpg'))
        self.ui.pushButton_4.setIconSize(QSize(40,40))
        self.ui.pushButton_4.setToolTip('Пробросить кубики.')

        self.ui.pushButton_5.setIcon(QIcon('chest.png'))
        self.ui.pushButton_5.setIconSize(QSize(40,40))
        self.ui.pushButton_5.setToolTip('Попытать удачу.')

        dd = QPixmap('no_foto.png')
        dd = dd.scaled(400,400)

        self.ui.label.setPixmap(dd)





    def load_data(self,sp):
        # Заставка.
        data_sp = ['Загрузка данных','Загрузка характиристики героя','Загрузка навыков героя'
                   ,'Загрузка оружия героя','Загрузка снаряжения героя']
        ind = 0
        for i in range(1,11):
            if i % 2 == 0:
                #Имитируем загрузку
                sp.showMessage('{0} .... {1}%'.format(data_sp[ind] ,i * 10),
                            QtCore.Qt.AlignCenter|QtCore.Qt.AlignBottom,QtCore.Qt.red)
                ind +=1
                time.sleep(2)
            else:
                sp.showMessage('{0} .... {1}%'.format(data_sp[ind], i * 10),
                               QtCore.Qt.AlignCenter | QtCore.Qt.AlignBottom, QtCore.Qt.red)
                time.sleep(2)

class Dialog_cubes(QDialog):

    """
    Класс используеться для имитации броска кубиков игроком.
    """
    # Диалоговое окно для броска кубиков.
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Бросок кубиков.')
        self.setGeometry(420,350,400,200)
        self.displaying_components()

    def displaying_components(self):
        # Разновидность кубиков заливаем в список.
        cubes = ['1d4','1d6','1d8','1d12','1d16','1d20']
        # Количество кубиков
        cubes_quantity = [1,2,3,4,5]
        # Создание горизонтальной группировки модулей.
        self.hbox = QHBoxLayout()
        self.combo = QComboBox()
        for i in cubes:
            self.combo.addItem(i)

        self.quantity = QLabel('X')

        self.combo_quantity = QComboBox()
        for i in cubes_quantity:
            self.combo_quantity.addItem(str(i))

        self.plus = QLabel(' + навыки :')
        self.line = QLineEdit('0')

        self.hbox.addWidget(self.combo)
        self.hbox.addWidget(self.quantity)
        self.hbox.addWidget(self.combo_quantity)
        self.hbox.addWidget(self.plus)
        self.hbox.addWidget(self.line)

        self.btn = QPushButton('Прокинуть кубики.')
        self.btn.setIcon(QIcon('3971-4.jpg'))
        self.btn.setIconSize(QSize(40,40))
        self.btn.clicked.connect(partial(self.random_cubes))
        self.conclusion = QLCDNumber()
        self.conclusion.display('0')
        # Расписываем получение значения.
        self.decryption = QLabel()
        # Вертикаальная группировка модулей.
        self.group_v = QVBoxLayout()
        self.group_v.addLayout(self.hbox)
        self.group_v.addWidget(self.btn)
        self.group_v.addWidget(self.conclusion)
        self.group_v.addWidget(self.decryption)

        self.setLayout(self.group_v)


    def random_cubes(self):
        # Получем значение кубиков,используем модуль ramdom для получение случайного числа.
        obtained_value = self.combo.currentText()
        if len(obtained_value) == 3:
            obtained_value = obtained_value[-1]
        else:
            obtained_value = obtained_value[-2:]
        # Создаем список выпавших костей.
        bones = []
        # Обходим циклом количество костей введеных пользователем.
        f = 0
        for i in range(0,int(self.combo_quantity.currentText())):
            random_int = random.randint(1,int(obtained_value))
            bones.append(random_int)
            f = f + random_int
        # Подсчитываем все кости и хорактеристику и выводим пользователю.
        the_amount = f + int(self.line.text())
        self.conclusion.display(the_amount)
        # Выводим на монитоор значение костей.
        if len(bones) == 1:
            self.decryption.setText('Ваши кубики {0} + навыки {1} '.
                                format(bones[0],self.line.text()))
        elif len(bones) == 2:
            self.decryption.setText('Ваши кубики {0} + {2} + навыки {1} '.
                                format(bones[0],self.line.text(),bones[1]))
        elif len(bones) == 3:
            self.decryption.setText('Ваши кубики {0} + {2} + {3} + навыки {1} '.
                                format(bones[0],self.line.text(),bones[1],bones[2]))
        elif len(bones) == 4:
            self.decryption.setText('Ваши кубики {0} + {2} +{3} + {4} + навыки {1} '.
                                format(bones[0],self.line.text(),bones[1],bones[2],bones[3]))
        elif len(bones) == 5:
            self.decryption.setText('Ваши кубики {0} + {2} +{3} + {4} +{5} + навыки {1} '.
                                format(bones[0],self.line.text(),bones[1],bones[2],bones[3],bones[4]))


if __name__ == '__main__':
    App = QApplication(sys.argv)
    # ВЫбор персонажа.
    the_choice_of_character = The_choice_of_the_hero()
    the_choice_of_character.exec()

    # Загружаем заставку.
    splash = QSplashScreen(QtGui.QPixmap('/home/denis-linux/Загрузки/444.jpg'))
    splash.showMessage('Загрузка данных .... 0%',
                       QtCore.Qt.AlignCenter | QtCore.Qt.AlignBottom, QtCore.Qt.red)
    splash.setGeometry(320, 320, 600, 400)
    splash.pixmap()
    # ОТображаем заставку
    splash.show()
    # Запускаем оборотный цикл
    App.processEvents()

    window = Window()
    window.load_data(splash)
    window.show()
    splash.finish(window)

    sys.exit(App.exec_())
