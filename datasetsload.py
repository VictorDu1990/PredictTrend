#encoding:utf-8
import os
import numpy as np


def traverse_path(fpath):
    """
    功能：遍历路径fpath下的所有文件及其文件夹下的文件，并返回包含所有文件路径的list
    输入：文件夹路径
    输出：所有文件的list
    """
    fs = os.listdir(f)
    txtlist = []
    for f1 in fs:
        tmp_path = os.path.join(f, f1)
        if not os.path.isdir(tmp_path):
            txtlist.append(tmp_path)
            print('文件: %s' % tmp_path)
        else:
            print('文件夹：%s' % tmp_path)
            traverse(tmp_path)
    return  txtlist


def readdatafromtxt(txtlst=[]):
    '''
    :func: read data from .txt file to np.array ,delimiter=','
    :param txtlst: list of .txt files path
    :return: all data of the all txtfiles
    '''
    all_datasets = []
    isfist = 1
    for fpath in txtlst:
        data = np.loadtxt(fpath, delimiter=',')
        if isfist:
            all_datasets = data
            isfist = 0
        else:
            all_datasets = np.concatenate((all_datasets, data), axis=0)
    # all_datasets = np.random.permutation(all_datasets)
    return all_datasets
