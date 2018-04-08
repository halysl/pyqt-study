# -*- coding:utf-8*-

import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QHBoxLayout, QVBoxLayout, QWidget


'''
箱布局，引入拉伸概念，将小组件放在大致的方位，可随着窗体变化而变化
'''
class box_position(QWidget):
	def __init__(self):
		super(box_position, self).__init__()
		self.initUI()

	def initUI(self):

		okButton = QPushButton('ok')
		cancalButton = QPushButton('cancel')

		hbox = QHBoxLayout()
		hbox.addStretch(1)
		hbox.addWidget(okButton)
		hbox.addWidget(cancalButton)

		vbox = QVBoxLayout()
		vbox.addStretch(1)
		vbox.addLayout(hbox)

		self.setLayout(vbox)

		self.setGeometry(300, 300, 250, 150)
		self.setWindowTitle('box position')
		self.show()


if __name__ == "__main__":
	app =QApplication(sys.argv)
	bp = box_position()
	sys.exit(app.exec_())