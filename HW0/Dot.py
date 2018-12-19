import numpy as np;

def Get_Matrix(row, col, file_name):
	#先创建一个 row*col 的全零方阵A，并且数据的类型设置为float浮点数
	Matrix = np.zeros((row,col), dtype=float)
	#重定向输入流
	file = open('.\\'+file_name, 'r')
	#把文件中的所有数据按行读入
	lines = file.readlines()
	#Matrix目前所在行数
	rows = 0
	#遍历每一行
	for line in lines:
		#去除换行符，以空格来分割数据
		list = line.strip('\n').split(' ')
		Matrix[rows:] = [str(i) for i in list]
		rows += 1
	return Matrix

if __name__=="__main__":
	Matrix_A = Get_Matrix(1, 50, 'MatrixA.txt') 	
	Matrix_B = Get_Matrix(50, 1, 'MatrixB.txt')
	Matrix_ans = np.dot(Matrix_A, Matrix_B)
	print(Matrix_ans)
