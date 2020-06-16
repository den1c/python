from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication,QWidget,QSplashScreen,QDialog,QVBoxLayout,QHBoxLayout,\
    QLabel,QPushButton
from PyQt5 import QtCore,QtGui
import sys
import time


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.ui_window()

    def ui_window(self):
        self.setGeometry(320,350,600,400)


    def load_data(self,sp):
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

def start_main_window():
    App = QApplication(sys.argv)
    #Загружаем заставку.
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


start_main_window()