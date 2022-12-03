import sys # 引数の操作
import csv # csvの読み込み
import numpy as np # 数値計算
import matplotlib.pyplot as plt # 可視化
from collections import Counter # 頻度カウント
from scipy.stats import multivariate_normal # 多次元ガウス分布の確率密度関数の計算
from mpl_toolkits.mplot3d import Axes3D # 可視化

def read_data(path):
    csv_dir = path

    # csvを読み取って(N, D)行列を生成
    with open(csv_dir) as f:
        reader = csv.reader(f)
        X = [_ for _ in reader]
        for i in range(len(X)):
            for j in range(len(X[i])):
                X[i][j] = float(X[i][j])

    # 後のためにnumpy化しておく
    X = np.array(X)
    return X