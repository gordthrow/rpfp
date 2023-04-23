import sys
import os
import pyowm
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QMessageBox, QVBoxLayout
from PyQt5.QtCore import QUrl, QTimer, QDateTime
from PyQt5.QtGui import QDesktopServices, QFont
import speech_recognition as sr


class PersonalAssistant(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()
        
        # Initialize the speech recognition module
        self.recognizer = sr.Recognizer()

    def initUI(self):

        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle('Personal Assistant')
        
        # Create a button widget to activate voice recognition for the application name
        voice_button = QPushButton('Speak', self)
        voice_button.move(400, 150)
        voice_button.resize(60, 30)
        voice_button.clicked.connect(self.listen_application_name)
        

        # Create a label widget to display the title
        title_label = QLabel('Personal Assistant', self)
        title_label.move(150, 50)
        title_label.setStyleSheet('font-size: 32px; font-weight: bold;')

        # Create a label widget to display the clock
        self.clock_label = QLabel(self)
        self.clock_label.move(50, 100)
        font = QFont()
        font.setPointSize(20)
        self.clock_label.setFont(font)

        # Create a label widget and a line edit widget for the application name
        app_label = QLabel('Application Name:', self)
        app_label.move(50, 150)
        app_label.setStyleSheet('font-size: 16px; font-weight: bold;')

        self.app_edit = QLineEdit(self)
        self.app_edit.move(200, 150)
        self.app_edit.resize(200, 30)

        # Create a button widget to open the application
        open_button = QPushButton('Open', self)
        open_button.move(200, 200)
        open_button.resize(100, 30)
        open_button.clicked.connect(self.open_application)

        # Create a button widget to close the application
        close_button = QPushButton('Close', self)
        close_button.move(300, 200)
        close_button.resize(100, 30)
        close_button.clicked.connect(self.close_application)

        # Create a label widget and a line edit widget for the search query
        search_label = QLabel('Search Query:', self)
        search_label.move(50, 250)
        search_label.setStyleSheet('font-size: 16px; font-weight: bold;')

        self.search_edit = QLineEdit(self)
        self.search_edit.move(200, 250)
        self.search_edit.resize(200, 30)

        # Create a button widget to perform the search
        search_button = QPushButton('Search', self)
        search_button.move(200, 300)
        search_button.resize(100, 30)
        search_button.clicked.connect(self.perform_search)

        # Show the GUI
        self.show()

        # Create a timer to update the clock every second
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

    def open_application(self):
        app_name = self.app_edit.text()
        try:
            os.startfile(app_name)
        except OSError:
            QMessageBox.warning(self, 'Error', f'Could not open {app_name}')

    def close_application(self):
        app_name = self.app_edit.text()
        os.system(f'taskkill /f /im {app_name}.exe')

    def perform_search(self):
        query = self.search_edit.text()
        if query:
            url = QUrl(f'https://www.google.com/search?q={query}')
            QDesktopServices.openUrl(url)

    def update_time(self):
        now = QDateTime.currentDateTime()
        date_time = now.toString('hh:mm:ss AP dd-MM-yyyy')
        self.clock_label.setText(date_time)
        self.clock_label.adjustSize()
        
    def listen_application_name(self):
        with sr.Microphone() as source:
            print('Say the name of the application')
            audio = self.recognizer.listen(source)

            try:
                app_name = self.recognizer.recognize_google(audio)
                self.app_edit.setText(app_name)
            except sr.UnknownValueError:
                print('Could not understand audio')
            except sr.RequestError as e:
                print(f'Request error: {e}')

   #it does not work for now, for some reason i think my api key part is broken
    """
        # Create a label widget and a line edit widget for the weather location
        weather_label = QLabel('Weather Location:', self)
        weather_label.move(50, 350)
        weather_label.setStyleSheet('font-size: 16px; font-weight: bold;')

        self.weather_edit = QLineEdit(self)
        self.weather_edit.move(200, 350)
        self.weather_edit.resize(200, 30)

        # Create a button widget to get the weather update
        weather_button = QPushButton('Get Weather', self)
        weather_button.move(200, 400)
        weather_button.resize(100, 30)
        weather_button.clicked.connect(self.get_weather)
    
    def get_weather(self):
        location = self.weather_edit.text()
        if location:
            owm = pyowm.OWM('ea43b1f94009d15d9bbff6fce4fb1bb5')  
            mgr = owm.weather_manager()
            try:
                weather = mgr.weather_at_place(location).weather
                temp = weather.temperature('celsius')['temp']
                status = weather.detailed_status
                message = f'The temperature in {location} is {temp:.1f}°C and the weather is {status.lower()}'
                QMessageBox.information(self, 'Weather Update', message)
            except pyowm.weatherapi25.not_found_error.NotFoundError:
                QMessageBox.warning(self, 'Error', f'Could not find weather for {location}')
    """

if __name__ == '__main__':
    app = QApplication(sys.argv)
    assistant = PersonalAssistant()
    sys.exit(app.exec_())