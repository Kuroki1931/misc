"""
目的　
１ビット変換して長い１の連なりを作り、その長さを求める
例
0110100101111 -> 01101001 1 1111  6 
既存の1のかたまりの長さと、間の距離を1 or not で表現する。

0110100101111 -> [4, 1, 'not', 1, 2]
となり合う数字を足し合わせて、1を足して最も長い数字を返す。
"""


def float_to_binary(num):
    binary_list = []
    while num != 0:
        if num % 2 == 1:
            binary_list.append(1)
        else:
            binary_list.append(0)

        num = num // 2

    return binary_list


def length(num):
    # 与えられた整数を2進数に変換する。
    binary_list = float_to_binary(num)

    # 0から始まる0と1の繋がりのリストを作成
    searching_for = 0
    count_list = []
    count = 0

    for i in binary_list:
        if i != searching_for:
            count_list.append(count)
            searching_for = i
            count = 0
        count += 1

    count_list.append(count)

    # 奇数のindexを作り出す。
    index_list = list(range(len(count_list)))[1:][::2]
    add_list = []

    for i in index_list[:-1]:
        if count_list[i+1] == 1:
            add_list.append(count_list[i]+1+count_list[i+2])
        else:
            add_list.append(count_list[i]+1)

    max_length = max(add_list)

    return max_length


assert length(14455) == 7, 'error'

"""
#計算量 O(bit+bit+1/2bit) = O(b)
# 空間  O(bit+bit+1/2bit) = O(b)
"""


# 解答参照後
