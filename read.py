import random
import matplotlib.pyplot as plt
import numpy as np
import time


class perceptron():
	def __init__(self,txtname,LR_condition,train_steps):


		def randompick (f):
			for line in f:

				if random.randint(1,3) != int(3):
					random_list_1.append(line)
				else:
					random_list_2.append(line)

			if len(random_list_1) == 0 or len(random_list_2) == 0:
				random_list_1.clear()
				random_list_2.clear()
				f = open(txtname)			
				randompick (f)

		f = open(txtname) #1 or 2

		random_list_1 = []
		random_list_2 = []

		tra_input_1 = []
		tra_input_2 = []
		tra_target = []

		tst_input_1 = []
		tst_input_2 = []
		tst_target = []

		tra_num=0
		tst_num=0

		#load dataset

		randompick (f)

		random.shuffle(random_list_1)
		random.shuffle(random_list_2)

		for line in random_list_1:
			line = line.split(" ")

			tra_input_1.append(float(line[0]))
			tra_input_2.append(float(line[1]))
			if txtname != "dataset/perceptron1.txt" and txtname != "dataset/perceptron2.txt" :
				tra_target.append(int(line[2].strip('\n'))-1) # set to 0 or 1
			else:
				tra_target.append(int(line[2].strip('\n')))
			tra_num +=1

		for line in random_list_2:
			line = line.split(" ")

			tst_input_1.append(float(line[0]))
			tst_input_2.append(float(line[1]))
			if txtname != "dataset/perceptron1.txt" and txtname != "dataset/perceptron2.txt" :
				tst_target.append(int(line[2].strip('\n'))-1) # set to 0 or 1
			else:
				tst_target.append(int(line[2].strip('\n')))
			tst_num +=1

		input_0 = 1
		w_0 = -1
		w_1 = 0.5
		w_2 = 0.5
		
		lr = LR_condition


		for k in range(train_steps):
			error=0

			for i in range(tra_num):
				#print("suppose get",tra_target[i])


				input_1 = tra_input_1[i]
				input_2 = tra_input_2[i]

				sum_ = input_0*w_0 + input_1*w_1 + input_2*w_2
				#print("sum=",sum_)

				if sum_ > 0:
					output = 1
					#print("we get 1")
				else: 
					output = -1
					#print("we get 0")

				if tra_target[i] == 1 and output == -1:
					w_0 = w_0 + lr*(input_0)
					w_1 = w_1 + lr*(input_1)
					w_2 = w_2 + lr*(input_2)
					error+=1

				elif tra_target[i] == 0 and output == 1 :
					w_0 = w_0 - lr*(input_0)
					w_1 = w_1 - lr*(input_1)
					w_2 = w_2 - lr*(input_2)
					error+=1
				else:
					w_0 = w_0
					w_1 = w_1
					w_2 = w_2

			### training accuracy
			#print("accuracy = ",((tra_num-error)/tra_num))


		tra_accuracy = ((tra_num-error)/tra_num)


		#print(tra_num,tst_num)
		#print(w_0,w_1,w_2)

		fig = plt.figure() # 生成一個圖片框
		ax = fig.add_subplot(1,1,1) # 編號
		for i in range(tst_num):
		    if tst_target[i] == 1:
		        ax.scatter(tst_input_1[i], tst_input_2[i], color='r')
		    else:
		        ax.scatter(tst_input_1[i], tst_input_2[i], color='b')

		test_error = 0

		for i in range(tst_num):
			#print("suppose get",tst_target[i])


			input_1 = tst_input_1[i]
			input_2 = tst_input_2[i]

			sum_ = input_0*w_0 + input_1*w_1 + input_2*w_2

			if sum_ > 0:
				output = 1
				
				#print("we get 1")
				if tst_target[i] ==0 :
					test_error +=1
					ax.scatter(input_1, input_2, color='g')
				else:
					ax.scatter(input_1, input_2, color='r')
			else: 
				output = -1
				#print("we get 0")
				if tst_target[i] ==1 :
					test_error +=1
					ax.scatter(input_1, input_2, color='g')
				else:
					ax.scatter(input_1, input_2, color='b')

		tst_accuracy = ((tst_num-test_error)/tst_num)

		### testing accuracy
		#print("testing accuracy = ",tst_accuracy)

		x1 = np.linspace(min(tst_input_1),max(tst_input_1))

		x2 = ( -w_0 - w_1*x1 )/w_2

		plt.plot(x1,x2)
		plt.savefig('dataset/pic.png')


		n = open('dataset/test.txt','w')


		tra = str(tra_accuracy) + "\n"
		tst = str(tst_accuracy) + "\n"
		weight_0 = str(w_0) + "\n"
		weight_1 = str(w_1) + "\n"
		weight_2 = str(w_2) + "\n"

		n.write(tra)
		n.write(tst)		
		n.write(weight_0)
		n.write(weight_1)
		n.write(weight_2)
		n.close()


