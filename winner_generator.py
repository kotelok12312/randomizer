
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,  QPushButton, QLabel, QVBoxLayout
from random import randint
def show_winner():
        random_number = randint(1, 100)
        number.setText(str(random_number))
        text.setText('случайное число:')


app = QApplication([])
window = QWidget()
window.setWindowTitle('Рандом')
window.resize(800, 600)
window.move(157,27)
text = QLabel('Нажми число')
number = QLabel('?')
btn = QPushButton('число')
btn.clicked.connect(show_winner)
v_line = QVBoxLayout()
v_line.addWidget(text, alignment=Qt.AlignCenter)
v_line.addWidget(number, alignment=Qt.AlignCenter)
v_line.addWidget(btn, alignment=Qt.AlignCenter)
window.setLayout(v_line)
window.show()
app.exec()
