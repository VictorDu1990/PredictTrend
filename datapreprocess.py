#coding:utf-8
import numpy as np

def colmean(X):
	'''
	功能：矩阵数据X每列减去各自单独列的平均值。
	几何解释：将数据的中心向原点靠近。
	输入 X：为[NxD]的矩阵。
	输出 X_mean: 为[NXD]的矩阵。
	'''
	X_mean = []
	X_mean = X - np.mean（X，axis = 0）
	return X_mean
	
def datanormal(X):
	'''
	功能：规范化数据分布范围，使其具有大致相同的规模。
	方法：一是将每个维度除以它的标准偏差（当数据均值为0时)。
		  二是将每个维度规范化，使每个维度最小值和最大值分别为-1和1。
	输入 X：为[NxD]的矩阵。
	输出 X_normal: 为[NxD]的矩阵。
	'''
	X_normal = []
	X_normal = X - np.std（X，axis = 0）
	return X_normal

def dataPCA(X, new_D):
	'''
	功能：提取主要特征，降低数据维度。
	输入 X：为[N x D]的矩阵。new_N:新的特征向量的维度。
	输出 Xrot_reduced: 为[N x new_D]的矩阵，保留new_D个主要特征。
	'''
	#大小为[N×D]的输入数据矩阵X
	X - = np.mean（X，axis = 0）		#零中心数据（重要）
	cov = np.dot（X.T，X）/ X.shape [0] #获得数据协方差矩阵
	
	#计算数据协方差矩阵的SVD分解：U的列是特征向量，S是奇异值的一维数组。
	U，S，V = np.linalg.svd(cov)
	#Xrot = np.dot(X, U) 为去除数据的相关性，
	#我们将原始数据（以零为中心）投影到特征向量上.
	#Xrot的协方差矩阵是对角的

	#可以通过只使用前几个特征向量来减少数据的维度，并丢弃数据方差很小的维度。
	Xrot_reduced = np.dot(X, U[:, :new_D])#Xrot_reduced变成[N×100]
	return Xrot_reduced
	
def dataWhite(X):
	'''
	功能：将基于特征向量的数据除以每个维度的特征值以规范化。
	几何解释：如果输入数据是一个服从高斯分布的多重变量，
			  那么白化数据将数据转化为具有零均值和单位协方差矩阵的高斯变量。
	输入 X：为[N x D]的矩阵
	输出 X_White：为[N x D]的矩阵
	'''
	X - = np.mean（X，axis = 0）		#零中心数据（重要）
	cov = np.dot（X.T，X）/ X.shape [0] #获得数据协方差矩阵
	
	#计算数据协方差矩阵的SVD分解：U的列是特征向量，S是奇异值的一维数组。
	U，S，V = np.linalg.svd(cov)
	Xrot = np.dot(X, U) 				#去除数据的相关性
	#白化数据：
	#除以特征值（其是奇异值的平方根）
	X_White = Xrot / np.sqrt(S + 1e-5)
	return X_White	
