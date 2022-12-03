import numpy as np

def pearson(e1,e2): # [1,3,0,3]
    #入力されたリストのうち、どちらともゼロでない要素のみの相関係数を算出
    te1=[]
    te2=[]
    tmp=np.array(e1)*np.array(e2)
    for i in range(len(tmp)):
        if tmp[i]!=0:
            te1.append(e1[i])
            te2.append(e2[i])
    if len(te1)==1:
        return 0
    return np.corrcoef(te1,te2)[0,1]

def average(e):
    #入力されたリストのうち、ゼロでない要素のみの平均を算出
    n = sum(e)
    d = len([x for x in e if x!=0])
    return n/d

def evaluate(a,y,data,arr):
    #評価推定値を算出
    aveA = average(data[a])
    d=0
    n=0
    for i in range(len(data)):
        if a!=i and data[i][y]!=0:#a自身と、yの評価値がないユーザを除く
            d+=abs(arr[a][i])
            n+=arr[a][i]*(data[i][y]-average(data[i]))
    return aveA+n/d


data = [[0 for i in range(4)] for j in range(4)]
arr = [[0 for i in range(4)] for j in range(4)]
eva = [[0 for i in range(4)] for j in range(4)]

# データの入力
data[0]= [1,3,0,3]
data[1]= [0,1,3,0]
data[2]= [2,1,3,1]
data[3]= [1,3,2,0]


# ユーザー間の類似度計算
for key in range(len(data)): # 0, 1, 2, 3
    base_customers = data[key]
    for key2 in range(len(data)): # 0, 1, 2, 3
        if key == key2:
            continue
        target_customers = data[key2]
        j = pearson(base_customers, target_customers)
        arr[key][key2] = j

#ユーザ・商品ごとの評価値推定
for i in range(len(data)):
    for j in range(len(data[i])):
        eva[i][j] = evaluate(i,j,data,arr)

# ユーザー間の類似度
print(' \t  1 \t  2 \t  3 \t  4 ')
print('1\t{0:2.2f}\t{1:2.2f}\t{2:2.2f}\t{3:2.2f}'.format(arr[0][0], arr[0][1], arr[0][2], arr[0][3]))
print('2\t{0:2.2f}\t{1:2.2f}\t{2:2.2f}\t{3:2.2f}'.format(arr[1][0], arr[1][1], arr[1][2], arr[1][3]))
print('3\t{0:2.2f}\t{1:2.2f}\t{2:2.2f}\t{3:2.2f}'.format(arr[2][0], arr[2][1], arr[2][2], arr[2][3]))
print('4\t{0:2.2f}\t{1:2.2f}\t{2:2.2f}\t{3:2.2f}'.format(arr[3][0], arr[3][1], arr[3][2], arr[3][3]))

#ユーザ・商品ごとの評価値推定値
print(' \t  1 \t  2 \t  3 \t  4 ')
print('1\t{0:2.2f}\t{1:2.2f}\t{2:2.2f}\t{3:2.2f}'.format(eva[0][0], eva[0][1], eva[0][2], eva[0][3]))
print('2\t{0:2.2f}\t{1:2.2f}\t{2:2.2f}\t{3:2.2f}'.format(eva[1][0], eva[1][1], eva[1][2], eva[1][3]))
print('3\t{0:2.2f}\t{1:2.2f}\t{2:2.2f}\t{3:2.2f}'.format(eva[2][0], eva[2][1], eva[2][2], eva[2][3]))
print('4\t{0:2.2f}\t{1:2.2f}\t{2:2.2f}\t{3:2.2f}'.format(eva[3][0], eva[3][1], eva[3][2], eva[3][3]))
