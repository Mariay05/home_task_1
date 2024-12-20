from PyQt6.QtCore import QUrlQuery
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLineEdit
import sys

app = QApplication(sys.argv)

def change_background():
    url = text_url.text()
    color = text_color.text()
    window.setStyleSheet(f"background-image: url('{url}');")
    window.setStyleSheet(f"background-color: {color};")

window = QMainWindow()
window.setWindowTitle("Окно")
super_widget = QWidget()

button = QPushButton("Нажми на кнопку - получишь результат...")
button.clicked.connect(change_background)


text_color = QLineEdit("Напиши цвет на английском")
text_url = QLineEdit("Напиши адрес изображения")

layout = QVBoxLayout()
layout.addWidget(button)
layout.addWidget(text_color)
layout.addWidget(text_url)
window.setLayout(layout)

super_widget.setLayout(layout)
window.setCentralWidget(super_widget)

window.show()
app.exec()




