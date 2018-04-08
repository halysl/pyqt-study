# -*- coding:utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget


'''
绝对定位，给出一个坐标值，将控件放入该坐标，不随窗体变化而变化
'''
class absolutePosition(QWidget):
	def __init__(self):
		super(absolutePosition, self).__init__()
		self.initUI()

	def initUI(self):

		lab1 = QLabel('zetcode', self)
		lab1.move(15, 10)

		lab2 = QLabel('tutorials', self)
		lab2.move(35,40)

		lab3 = QLabel('for programmers', self)
		lab3.move(55, 70)

		self.setGeometry(300, 300, 250, 150)
		self.setWindowTitle('absolute Position')
		self.show()


if __name__ == "__main__":
	app = QApplication(sys.argv)
	ap = absolutePosition()
	sys.exit(app.exec_())