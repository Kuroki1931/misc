import sys # 引数の操作
import csv # csvの読み込み
import numpy as np # 数値計算
import matplotlib.pyplot as plt # 可視化
from collections import Counter # 頻度カウント
from scipy.stats import multivariate_normal # 多次元ガウス分布の確率密度関数の計算
from mpl_toolkits.mplot3d import Axes3D # 可視化

N1 = 4000
N2 = 3000
N3 = 2000
N4 = 1000

# 平均
Mu1 = [5, -5, -5]
Mu2 = [-5, 5, 5]
Mu3 = [-5, -5, -5]
Mu4 = [5, 5, 5]

# 共分散
Sigma1 = [[1, 0, -0.25], [0, 1, 0], [-0.25, 0, 1]]
Sigma2 = [[1, 0, 0], [0, 1, -0.25], [0, -0.25, 1]]
Sigma3 = [[1, 0.25, 0], [0.25, 1, 0], [0, 0, 1]]
Sigma4 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

# 乱数を生成
X1 = np.random.multivariate_normal(Mu1, Sigma1, N1)
X2 = np.random.multivariate_normal(Mu2, Sigma2, N2)
X3 = np.random.multivariate_normal(Mu3, Sigma3, N3)
X4 = np.random.multivariate_normal(Mu4, Sigma4, N4)

# 描画準備
fig = plt.figure(figsize=(4, 4), dpi=300)
ax = Axes3D(fig)

# 当サイトのカスタムカラーリスト
cm = plt.get_cmap("tab10")   

# メモリを除去
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

# 少し回転させて見やすくする
ax.view_init(elev=10, azim=70)

# 描画
ax.plot(X1[:,0], X1[:,1], X1[:,2], "o", ms=0.5, color=cm(0))
ax.plot(X2[:,0], X2[:,1], X2[:,2], "o", ms=0.5, color=cm(1))
ax.plot(X3[:,0], X3[:,1], X3[:,2], "o", ms=0.5, color=cm(2))
ax.plot(X4[:,0], X4[:,1], X4[:,2], "o", ms=0.5, color=cm(3))
plt.show()

#結合した内容を表示
X = np.concatenate([X1, X2, X3, X4])

# 描画準備
fig = plt.figure(figsize=(4, 4), dpi=300)
ax = Axes3D(fig)

# メモリを除去
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

# 少し回転させて見やすくする
ax.view_init(elev=10, azim=70)

# 描画
ax.plot(X[:,0], X[:,1], X[:,2], "o", ms=0.5, color=cm(0))
plt.show()

np.savetxt("data.csv", X, delimiter=",")