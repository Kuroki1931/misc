import numpy as np

# M×Nの行列で0が存在する行と列をすべて0にする。
# array -> array

def changeTo_0(array):

    zero_array = []

    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            if array[i, j] == 0:

                # M×Nで0の行列を作成し、[i, 0:N-1], [0:M-1, j]を1に変換

                zero = np.zeros(shape=(array.shape[0], array.shape[1]))
                zero[i, :] = np.ones(array.shape[1])
                zero[:, j] = np.ones(array.shape[0])

                zero_array.append(zero)

    over_one_array = sum(zero_array)

    # １以上の場所を0に変換する
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            if over_one_array[i, j] > 0:
                array[i, j] = 0

    return array


"""
以下解答参照後
"""

# 列と行ごとに0があるかないかのみ判定する。

def check1(array):
    row = [False] * array.shape[0]
    column = [False] * array.shape[1]

    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            if array[i, j] == 0:

                row[i] = True;
                column[j] = True;

    for i in range(len(row)):
        if row[i]:
            array[i, :] = 0

    for i in range(len(column)):
        if column[i]:
            array[:, i] = 0

    return array

# 空間メモリがO(N)で済む


# 最初の行と最初の列を利用する。

def check2(array):

    rowHasZero = False
    colHasZero = False

    for i in range(array.shape[0]):
        if array[i, 0] == 0:
            rowHasZero = True
            break

    for i in range(array.shape[1]):
        if array[0, j] == 0:
            colHasZero = True
            break

    for i in range(1, array.shape[0]):
        for j in range(1, array.shape[1]):
            if array[i, j] == 0:
                array[i, 0] = 0
                array[0, j] = 0

    
    for i in range(array.shape[0]):
        if array[i, 0] == 0:
            array[i, :] = 0

    for j in range(array.shape[1]):
        if array[0, j] == 0:
            array[:, i] = 0

    if rowHasZero:
        array[0, :] = 0

    if colHasZero:
        array[:, 0] = 0
        
        
    
    return array

# 空間メモリO(1) 元のarrayを使用している。


    
                                
                
                





