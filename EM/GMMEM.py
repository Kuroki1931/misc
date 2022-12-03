from curses import KEY_SELECT
import sys # 引数の操作
import csv # csvの読み込み
import numpy as np # 数値計算
import matplotlib.pyplot as plt # 可視化
from collections import Counter # 頻度カウント
from scipy.stats import multivariate_normal # 多次元ガウス分布の確率密度関数の計算
from mpl_toolkits.mplot3d import Axes3D # 可視化
from data.read_data import read_data

path = './data/data.csv'
X = read_data(path)

class GMMEM():
    def __init__(self, K):
        self.K = K
        self.eps = np.spacing(1)

    def init_params(self, X):
        # 入力データ X のサイズは (N, D)
        self.N, self.D = X.shape
        # 平均は標準ガウス分布から生成
        self.mu = np.random.randn(self.K, self.D)
        # 分散共分散行列は単位行列
        self.sigma = np.tile(np.eye(self.D), (self.K, 1, 1))
        # 重みは一様分布から生成
        self.pi = np.ones(self.K) / self.K
        # 負担率は標準正規分布から生成するがEステップですぐ更新するので初期値自体には意味がない
        self.r = np.random.randn(self.N, self.K)

    def gmm_pdf(self, X):
        return np.array([self.pi[k] * multivariate_normal.pdf(X, mean=self.mu[k], cov=self.sigma[k]) for k in range(self.K)]).T # (N, K)

    def e_step(self, X):
        # GMMの確率密度関数を計算
        gmm_pdf = self.gmm_pdf(X)
        # 対数領域で負担率を計算
        log_r = np.log(gmm_pdf) - np.log(np.sum(gmm_pdf, 1, keepdims=True) + self.eps)
        # 対数領域から元に戻す
        r = np.exp(log_r)
        # np.expでオーバーフローを起こしている可能性があるためnanを置換しておく
        r[np.isnan(r)] = 1.0 / (self.K)
        # 更新
        self.r = r

    def m_step(self, X):
        # Q関数を最大にするパラメータ (mu, sigma, pi) を計算する
        # まずは N_k を計算しておく
        N_k = np.sum(self.r, 0) # (K)
        # 最適なpiを計算して更新する
        self.pi = N_k / self.N # (K)
        # 最適なmuを計算して更新する
        self.mu = (self.r.T @ X) / (N_k[:, None] + np.spacing(1)) # (K, D)
        # 最適なsigmaを計算して更新する
        r_tile = np.tile(self.r[:,:,None], (1, 1, self.D)).transpose(1, 2, 0) # (K, D, N)
        res_error = np.tile(X[:,:,None], (1, 1, self.K)).transpose(2, 1, 0) - np.tile(self.mu[:,:,None], (1, 1, self.N)) # (K, D, N)
        self.sigma = ((r_tile * res_error) @ res_error.transpose(0, 2, 1)) / (N_k[:,None,None] + np.spacing(1)) # (K, D, D)

    def visualize(self, X):
        # クラスタリングを実行
        labels = np.argmax(self.r, 1) # (N)
        # 利用するカラーを極力揃えるためクラスタを出現頻度の降順に並び替える
        label_frequency_desc = [l[0] for l in Counter(labels).most_common()] # (K)
        # tab10 カラーマップを利用
        cm = plt.get_cmap("tab10")   
        # 描画準備
        fig = plt.figure(figsize=(4, 4), dpi=300)
        ax = Axes3D(fig)
        # メモリを除去
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_zticks([])
        # 少し回転させて見やすくする
        ax.view_init(elev=10, azim=70)
        # 各クラスタごとに可視化を実行する
        for k in range(len(label_frequency_desc)):
            cluster_indexes = np.where(labels==label_frequency_desc[k])[0]
            ax.plot(X[cluster_indexes, 0], X[cluster_indexes, 1], X[cluster_indexes, 2], "o", ms=0.5, color=cm(k))
        plt.show()

    def execute(self, X, iter_max, thr):
        # パラメータ初期化
        self.init_params(X)
        # 各イテレーションの対数尤度を記録するためのリスト
        log_likelihood_list = []
        # 対数尤度の初期値を計算
        log_likelihood_list.append(np.mean(np.log(np.sum(self.gmm_pdf(X), 1) + self.eps)))
        # 更新開始
        for i in range(iter_max):
            # Eステップの実行
            self.e_step(X)
            # Mステップの実行
            self.m_step(X)
            # 今回のイテレーションの対数尤度を記録する
            log_likelihood_list.append(np.mean(np.log(np.sum(self.gmm_pdf(X), 1) + self.eps)))
            # 前回の対数尤度からの増加幅を出力する
            print("Log-likelihood gap: " + str(round(np.abs(log_likelihood_list[i] - log_likelihood_list[i+1]), 2)))
            # もし収束条件を満たした場合，もしくは最大更新回数に到達した場合は更新停止して可視化を行う
            if (np.abs(log_likelihood_list[i] - log_likelihood_list[i+1]) < thr) or (i == iter_max - 1):
                print(f"EM algorithm has stopped after {i + 1} iteraions.")
                self.visualize(X)
                break

# モデルをインスタンス化する
model = GMMEM(K=4)
# EMアルゴリズムを実行する
model.execute(X, iter_max=5, thr=0.001)






