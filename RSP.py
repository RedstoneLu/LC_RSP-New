from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QMessageBox
from PyQt5.QtGui import QPalette, QColor, QIcon, QFont
from PyQt5.QtCore import QTimer, Qt
import sys
import random

class RandomSelector(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        app = QApplication.instance() or QApplication(sys.argv)

        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(255, 255, 255))  # 设置窗口背景为白色
        palette.setColor(QPalette.WindowText, QColor(0, 0, 0))    # 设置窗口文本颜色为黑色
        palette.setColor(QPalette.Base, QColor(255, 255, 255))   # 设置基础颜色为白色
        palette.setColor(QPalette.AlternateBase, QColor(245, 245, 245))  # 设置交替背景颜色为浅灰色
        palette.setColor(QPalette.ToolTipBase, QColor(255, 255, 220))  # 设置工具提示背景颜色为浅黄色
        palette.setColor(QPalette.ToolTipText, QColor(0, 0, 0))  # 设置工具提示文本颜色为黑色
        app.setPalette(palette)

        self.setWindowTitle("随机点人")
        self.setWindowIcon(QIcon('icon.png'))
        self.setGeometry(300, 300, 400, 250)

        with open('students.txt', 'r', encoding='utf-8') as file:
            self.students = file.readlines()
        self.students = [student.strip() for student in self.students if student.strip()]

        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        layout = QVBoxLayout()
        self.centralWidget.setLayout(layout)

        self.selected_text = QLabel(self)
        self.selected_text.setWordWrap(True)
        self.selected_text.setFont(QFont("微软雅黑", 18))
        self.selected_text.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.selected_text)

        self.reselect_button = QPushButton("再次随机选人", self)
        self.reselect_button.clicked.connect(self.random_select)
        layout.addWidget(self.reselect_button)

        self.copyright_button = QPushButton("关于", self)
        self.copyright_button.clicked.connect(self.show_copyright_info)
        layout.addWidget(self.copyright_button)
        
        self.timer = QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.setInterval(1200)
        self.timer.timeout.connect(self.display_random_student)
        self.timer.start()

    def random_select(self):
        self.selected_text.setText("随机选人中...")
        self.timer.start()

    def display_random_student(self):
        self.selected_text.setText(f"选中的学生是：{random.choice(self.students)}")

    def show_copyright_info(self):
        QMessageBox.about(self, "版权信息", "版权所有 (C) 2023 轻云网络。\n版本号2.0.0_Run in PyQt5")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    selector = RandomSelector()
    selector.show()
    sys.exit(app.exec_())
