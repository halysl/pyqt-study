# -*-coding:utf-8 -*-

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QStatusBar, QGridLayout, 
	                         QMainWindow, QLabel, QTextEdit)


class editorWithCount(QMainWindow):
	def __init__(self):
		super(editorWithCount, self).__init__()
		self.initUI()

	def initUI(self):

		grid = QGridLayout()
		grid.setSpacing(10)

		count = 0
		self.text = "count:{0}".format(count)

		self.label = QLabel(self.text, self)
		grid.addWidget(self.label, 1, 0)

		textEdit = QTextEdit(self)
		grid.addWidget(self.textEdit, 1, 1)

		self.setGeometry(300, 300, 250, 150)
		self.setWindowTitle('Editor With Count')
		self.show()


if __name__ == "__main__":
	app = QApplication(sys.argv)
	ewc = editorWithCount()
	sys.exit(app.exec_())
