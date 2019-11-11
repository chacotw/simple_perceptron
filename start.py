# -*- coding: utf-8 -*-

import sys
#import os
#import time
#import shutil
import fix_qt_import_error

from PyQt5 import QtWidgets
from mainwnd import Ui_MainWindow
from PyQt5 import QtGui

from test2 import perceptron


class Main_Window(QtWidgets.QMainWindow):
	def __init__(self):
		QtWidgets.QMainWindow.__init__(self)#QMainWindow的初始化
		self.mainwnd = Ui_MainWindow()#主窗口的实例化
		self.mainwnd.setupUi(self)


	def start(self):
		self.image = QtGui.QPixmap()

		pic_path = "dataset/pic.png"

		txtname = self.mainwnd.chooseTXT.currentText()

		txtname =  "dataset/"+txtname

		try:
		    LR_condition = float(self.mainwnd.lineEdit.text())
		except:
		    LR_condition = 0.01
		else:
		    LR_condition = float(self.mainwnd.lineEdit.text())
		

		try:
		    train_steps = int(self.mainwnd.lineEdit_2.text())
		except:
		    train_steps = 100
		else:
		    train_steps = int(self.mainwnd.lineEdit_2.text())


		perceptron(txtname,LR_condition,train_steps)

		self.image.load(pic_path)
		self.show_image()

		"""
		w = open('dataset/test.txt','r')

		tst_accuracy = w.read()
		tst_accuracy = float(tst_accuracy)*100
		#print(accuracy)
		self.mainwnd.textBrowser_6.setText(str(tst_accuracy))
		"""
		#############
		count = 0
		w = open('dataset/test.txt','r')
		for line in w:
			if count == 0 :
				tra_accuracy = float(line)*100
				self.mainwnd.textBrowser_8.setText(str(tra_accuracy))
			elif count == 1 :
				tst_accuracy = float(line)*100	
				self.mainwnd.textBrowser_6.setText(str(tst_accuracy))			
			elif count == 2 :
				w_0 = float(line)
				self.mainwnd.textBrowser_12.setText(str(w_0))
			elif count == 3 :
				w_1 = float(line)
				self.mainwnd.textBrowser_13.setText(str(w_1))			
			elif count == 4 :
				w_2 = float(line)
				self.mainwnd.textBrowser_14.setText(str(w_2))
			count +=1

		"""
		m = open('dataset/test2.txt','r')
		tra_accuracy = m.read()
		tra_accuracy = float(tra_accuracy)*100
		#print(accuracy)
		self.mainwnd.textBrowser_8.setText(str(tra_accuracy))
		#self.comboBox.clear()  # 清空items

		#self.comboBox.clear()  # 清空items
		"""
	def show_image(self):
		self.mainwnd.Graphic.scene = QtWidgets.QGraphicsScene()            
		item = QtWidgets.QGraphicsPixmapItem(self.image)                
		self.mainwnd.Graphic.scene.addItem(item)       		       
		self.mainwnd.Graphic.setScene(self.mainwnd.Graphic.scene)   
		self.mainwnd.Graphic.fitInView(item)


app = QtWidgets.QApplication(sys.argv)

window = Main_Window()

btn=window.mainwnd.start_Button
btn.clicked.connect(window.start)



window.show()
sys.exit(app.exec_())

