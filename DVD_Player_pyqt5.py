"""

"""

import time
import datetime
import sys
import os

from PyQt5 import QtCore, QtGui
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QWidget, QApplication, QPushButton, QHBoxLayout,
                             QVBoxLayout, QLabel, QSlider, QSizePolicy, QFileDialog, QSplashScreen, QSizeGrip
                             )
from PyQt5.QtGui import (QIcon, QPalette, QFont)
from PyQt5.QtCore import Qt, QUrl, QTimer

from help import Dialog  # Импортируем диалоговое окно.

from menu_pyqt import Menu  # Импортируем меню.
from btn import Btn_Video_Player  # Импортируем кнопки плера.
from list_file import List_file  # Импортируем плей лист.

# Глобальные переменные.
time_ts = 0  # Начальное значение таймера.
version_of_the_script = '1.0'  # Версия скрипта.
speed = 2  # Обычная скорость возпроиведения видео.
time_spees = 1000  # Скорость отсчета таймера (1 секунда)


def load_data(sp):
    # Заставка.
    data_sp = ['', '', '', '', '']
    ind = 0
    for i in range(1, 11):
        if i % 2 == 0:
            # Имитируем загрузку
            sp.showMessage('{0} .... {1}%'.format(data_sp[ind], i * 10),
                           QtCore.Qt.AlignCenter | QtCore.Qt.AlignBottom, QtCore.Qt.red)
            ind += 1
            time.sleep(0.5)
        else:
            sp.showMessage('{0} .... {1}%'.format(data_sp[ind], i * 10),
                           QtCore.Qt.AlignCenter | QtCore.Qt.AlignBottom, QtCore.Qt.red)
            time.sleep(0.5)


class Window(QWidget):
    def __init__(self):
        super().__init__()

        # Дизайн видео плеера.
        self.mediaplayer = QMediaPlayer()
        # Объект видео виджет.
        self.videowidget = QVideoWidget()
        # Устанавливаем размеры видео виджета.
        self.videowidget.setMinimumWidth(870)  # Ширина видео виджета.
        self.videowidget.setMinimumHeight(370)  # Высота видео виджета.
        self.setWindowTitle('DVD player')  # Заголовок окна.
        self.setWindowIcon(QIcon('logo.jpg'))
        self.window_size()  # Обращаемся за размерами окна и координат его размещения.

        # Выполняем заливку виджета черным цветом.
        p = self.palette()
        p.setColor(QPalette.Window, Qt.black)
        self.setPalette(p)

        #  Создаем кнопки .
        self.openBtn = QPushButton()  # Кнопка выбора файла для просмотра.
        self.open_list_file = QPushButton()  # Кнопка список возпроизведений.
        self.playBtn = QPushButton()  # Кнопка плей.
        self.rewindBtn = QPushButton()  # Кнопка перемотка назад.
        self.forwardBtn = QPushButton()  # Кнопка перемотка вперед.
        self.stopBtn = QPushButton()  # Кнопка стоп.
        self.soundBtn = QPushButton()  # Кнопка включить или отклычить звук.
        self.deploy = QPushButton()  # Кнопка развернуть и свернуть окно.
        self.deploy.setIcon(QIcon('capture.png'))

        self.slider = QSlider(Qt.Horizontal)  # Главный ползунок видео.
        self.slider_sound = QSlider()  # Ползунок звука.

        self.time_video = QLabel('00:00:00')  # Виджет отображает длительность видео.
        self.time_video_on = QLabel('00:00:00')  # Виджет отображает время просмотреного видео.
        self.raz = QLabel('/')

        # Отображаем название видео.
        self.info_title_video = QLabel()
        # Отображаем версию скрипта.
        self.script = QLabel('version ' + version_of_the_script)
        self.script.setAlignment(Qt.AlignHCenter)
        self.script.setStyleSheet('color: white ')  # Установливаем цвет виджета.
        #
        self.label = QLabel()
        self.label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        # Создаем горизонтальный контейнер.
        self.hboxlayout = QHBoxLayout()
        # Содаем горизонтальный контейнер кнопок video player.
        self.hboxBtn = QHBoxLayout()
        # Создаем вертикальный контейнер.
        self.vbox = QVBoxLayout()
        self.info_time = ''

        # Время просмотренного видео.
        self.timer = QTimer()
        self.timer.setInterval(time_spees)

        self.init_ui()

        # Подключаем меню.
        self.menu = Menu(self.vbox, self.open_file, self.mediaplayer, self.slider_sound,
                         self.soundBtn, self.volume_muted)

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_F1:
            inf0_dialog = Dialog()
            inf0_dialog.exec_()

    def window_size(self):
        # Устанавливаем размеры окна и координаты его размещения.
        self.resize(900, 400)
        x = (QApplication.desktop().width() - self.width()) // 2
        y = (QApplication.desktop().height() - self.height()) // 4
        self.move(x, y)

    def time_display(self, time_ts):
        # Отображение пройденого времени видео.
        a = str(datetime.timedelta(seconds=time_ts))  # Переводим секунды в формат
        # 'Час:минута:секунда'
        self.time_video_on.setText(a)  # Отображаем время видео.
        self.time_video_on.setFont(QFont('Ubuntu', 10))

    def start_time(self):
        # Старт отчет времени.
        self.timer.start()

    def stop_time(self):
        # Останавливает таймер.
        self.timer.stop()

    def pause_time(self):
        # Пауза таймера.
        self.timer.stop()

    def time_report(self):
        # Счетчик.
        global time_ts
        time_ts += 1
        self.time_display(time_ts)

    def open_file(self):
        global time_ts
        """
        Диалоговое окно,для выбора файла.
        """
        try:
            user = os.getlogin()  # Запрашиваем имя пользователя пк.
            filename, _ = QFileDialog.getOpenFileName(self, 'Выберите файл',
                                                      directory="/Users/{0}/Documents".format(user),
                                                      filter='Видеофайлы (*.avi *.mp4 *.mp3)')

            if filename != '':
                self.mediaplayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
                self.playBtn.setIcon(QIcon('play-button.png'))
                self.playBtn.setEnabled(True)  # Делаем кнопку плей акттивной.
                self.rewindBtn.setEnabled(True)
                self.forwardBtn.setEnabled(True)

            self.stop_time()
            time_ts = 0  # Обнуляем таймер.
            self.time_display(time_ts)
        except QApplication:
            self.mediaplayer.setMedia(QMediaContent(QUrl.fromLocalFile('mideo-logo.png')))

    def play_video(self):
        # Реагируем на нажатие кнопок(play, stop, pause)
        if self.mediaplayer.state() == QMediaPlayer.PlayingState:
            self.mediaplayer.pause()

            self.pause_time()  # Ставим таймер на паузу.
            self.mediastate()
        else:
            self.mediaplayer.play()
            self.start_time()  # Запускаем отсчет времени.
            self.mediastate()

    def mediastate(self):
        # Изменяем вид кнопок в проигрователе.
        if self.mediaplayer.state() == QMediaPlayer.PlayingState:
            self.playBtn.setIcon(QIcon('play-on.png'))
            self.stopBtn.setEnabled(False)
        else:
            self.playBtn.setIcon(QIcon('pause-on.png'))
            self.stopBtn.setIcon(QIcon('stop-on.png'))
            self.stopBtn.setEnabled(True)

    def position_chander(self, position):
        # Работаем с позицией ползунка в плеере.
        self.slider.setValue(position)

    def duration_chander(self, duration):
        self.slider.setRange(0, duration)

    def set_position(self, position):
        global time_ts
        # Включаем видео в точке позиции ползунка.
        self.mediaplayer.setPosition(position)
        # Получаем время просмотра видео при перемищении ползунка.
        slider_now = self.slider.value() // 1000
        self.pause_time()  # На время перемищения таймер ставим на паузу.
        time_ts = slider_now  # В глобальную переменую помещаем значения времени ползунка.
        self.start_time()  # Снимаем с паузы таймер.

    def sound_volume(self):
        # Обрабатываем действия с громкостью.
        self.mediaplayer.setVolume(self.slider_sound.value())

    def volume_muted(self):
        # Выключаем и включаем звук.
        if self.mediaplayer.isMuted():
            self.mediaplayer.setMuted(False)  # Включаем звук.
            self.soundBtn.setIcon(QIcon('sound-on.png'))
        else:
            self.mediaplayer.setMuted(True)  # Отключаем звук.
            self.soundBtn.setIcon(QIcon('sound.png'))

    def fast_forward(self):
        # Управляем скоростью перемотки вперед.
        global speed, time_spees
        if speed > 4:  # Если скорость перемотки больше 4 скорости,
            self.mediaplayer.setPlaybackRate(1)  # устанавливаем стандартное возпроизведение видео.
            self.forwardBtn.setToolTip('Стандартная скорость.')
            speed = 2  # Устанавливаем 2 скорость.
            self.timer.setInterval(time_spees)  # Стандартный отсчет счетчика.
            self.forwardBtn.setIcon(QIcon('forward.png'))
        else:
            self.mediaplayer.setPlaybackRate(speed)  # Перематываем видео .
            self.forwardBtn.setToolTip('Стандартная скорость * {0}'.format(speed))
            self.timer.setInterval(time_spees // speed)
            speed += 2  # Увеличиваем скорость перемотки.
            self.forwardBtn.setIcon(QIcon('forward-on.png'))
        # self.mediaplayer.setPosition(self.mediaplayer.position() + 10000)

    def stop(self):
        global time_ts
        # Останавливаем воспроизведения видео.Перемищяем позицию ползунка на начало.
        self.mediaplayer.stop()
        self.playBtn.setIcon(QIcon('play-button.png'))  # Изменяем картинку на кнопке.
        self.stopBtn.setIcon(QIcon('stop.png'))  # Изменяем картинку на кнопке.

        time_ts = 0  # Обнуляем таймер.
        self.time_display(time_ts)  # Отображаем время.

    def handle_errors(self):
        self.playBtn.setEnabled(False)
        self.labei.setText('ERROR ^  ' + self.mediaplayer.errorString())

    def info_video(self, state):
        try:
            # Получаем информаию о видео файле.
            if state == QMediaPlayer.LoadedMedia:
                self.info_time = (self.mediaplayer.metaData('Duration') // 1000)
                a = str(datetime.timedelta(seconds=self.info_time))  # Переводим секунды в формат
                # 'Час:минута:секунда'
                self.time_video.setText(a)  # Отображаем время.
                self.time_video.setFont(QFont('Ubuntu', 10))
        except QApplication:
            pass

        # Получаем название видео.
        try:
            info = self.mediaplayer.metaData('Title')
            if info is None:
                self.info_title_video.setText('Нет информации о видео.')
                self.info_title_video.setStyleSheet('color: white ')  # Установливаем цвет виджета.
            else:
                self.info_title_video.setText(info)
                self.info_title_video.setStyleSheet('color: white ')  # Установливаем цвет виджета.
        except QApplication:
            self.info_title_video.setText('Ошибка при получении информации о видео.')

    def changing_the_window_size(self):
        # Изменения размера окна.
        if not self.isMaximized() or self.isFullScreen():
            self.showMaximized()
            self.deploy.setIcon(QIcon('mini_w.png'))
        else:
            self.window_size()
            self.deploy.setIcon(QIcon('capture.png'))
            print(6555)

    def init_ui(self):
        global version_of_the_script, time_spees
        # Работает с дизайном кнопок.
        Btn_Video_Player(self.openBtn, self.open_list_file, self.playBtn,
                         self.rewindBtn, self.forwardBtn, self.stopBtn, self.soundBtn)
        # Команды кнопок плеера.
        self.openBtn.clicked.connect(self.open_file)
        self.playBtn.clicked.connect(self.play_video)
        self.rewindBtn.clicked.connect(self.play_video)
        self.forwardBtn.clicked.connect(self.fast_forward)
        self.stopBtn.clicked.connect(self.stop)
        self.soundBtn.clicked.connect(self.volume_muted)
        self.open_list_file.clicked.connect(lambda: List_file(self.videowidget, self.vbox, self.window))
        self.deploy.clicked.connect(self.changing_the_window_size)

        # горизонтальный ползунок времени.
        self.slider.setRange(0, 0)
        self.slider.sliderMoved.connect(self.set_position)
        # Горизонтальный ползунок громкости.
        self.slider_sound.setRange(0, 100)  # Минимальное и максимальное значение.
        self.slider_sound.setTickInterval(5)
        self.slider_sound.setValue(30)
        self.slider_sound.setMaximumHeight(40)
        self.slider_sound.setMaximumWidth(20)
        self.slider_sound.sliderMoved.connect(self.sound_volume)

        # Виджет отображает длительность видео.
        self.time_video.setFont(QFont('Ubuntu', 10))
        self.time_video.setStyleSheet('color: white ')  # Установливаем цвет виджета.
        # Виджет отображает время просмотреного видео.
        self.time_video_on.setFont(QFont('Ubuntu', 10))
        self.time_video_on.setStyleSheet('color: white ')  # Установливаем цвет виджета.
        # Разделитель.
        self.raz.setFont(QFont('Ubuntu', 10))
        self.raz.setStyleSheet('color: white ')  # Установливаем цвет виджета.

        # Добавлям виджеты в горизонтальный контейнер.
        self.hboxlayout.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout.addWidget(self.openBtn)
        self.hboxlayout.addWidget(self.open_list_file)
        self.hboxlayout.addWidget(self.slider)
        self.hboxlayout.addWidget(self.time_video_on)
        self.hboxlayout.addWidget(self.raz)
        self.hboxlayout.addWidget(self.time_video)
        self.hboxlayout.addWidget(self.deploy)

        # Добавляем кнопки в горинтальный контейнер.
        self.hboxBtn.setAlignment(Qt.AlignHCenter)
        self.hboxBtn.addWidget(self.rewindBtn)
        self.hboxBtn.addWidget(self.stopBtn)
        self.hboxBtn.addWidget(self.playBtn)
        self.hboxBtn.addWidget(self.forwardBtn)
        self.hboxBtn.addWidget(self.soundBtn)
        self.hboxBtn.addWidget(self.slider_sound)

        # Добавляем виджеты в вертикальный контейнер.
        self.vbox.addWidget(self.videowidget)
        self.vbox.addWidget(self.info_title_video)
        self.vbox.addLayout(self.hboxlayout)
        self.vbox.addLayout(self.hboxBtn)
        self.vbox.addWidget(self.script)

        self.setLayout(self.vbox)

        self.mediaplayer.setVideoOutput(self.videowidget)

        # media player signals
        self.mediaplayer.positionChanged.connect(self.position_chander)
        self.mediaplayer.durationChanged.connect(self.duration_chander)
        self.mediaplayer.mediaStatusChanged.connect(self.info_video)
        self.timer.timeout.connect(self.time_report)


if __name__ == '__main__':
    App = QApplication(sys.argv)
    App.setWindowIcon(QIcon('logo.jpg'))
    # Загружаем заставку.
    splash = QSplashScreen(QtGui.QPixmap('mideo-logo.png'))
    splash.showMessage('Проверка обновлений .... 0%',
                       QtCore.Qt.AlignCenter | QtCore.Qt.AlignBottom, QtCore.Qt.red)

    splash.pixmap()
    # ОТображаем заставку
    splash.show()
    # Запускаем оборотный цикл
    App.processEvents()
    window = Window()
    desktop = QApplication.desktop()
    load_data(splash)
    window.show()
    splash.finish(window)

    sys.exit(App.exec_())
