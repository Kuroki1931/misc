"""
目的
正の整数が与えられた時、２進表現したときの１個の個数が同じ整数の中で、1つ後の数と前の数の出力
例
2      10 -> 1    01     4  100
8     100 -> 10   2    1000 16
3      11 ->  none       5  110    
10   1010 -> 9  1001    12 1100


○全てが1の場合
一つ前の値：存在しない

一つ後の値：最大桁の1を一つ繰り上げる


○oが右に固まっている場合
一つ前の値：最も右にある0の塊の最左の０と、隣の1を入れ替える。　

一つ後の値：最大桁の1を一つ繰り上げる


○それ以外
一つ前の値
最も右にある0の塊の最左の０と、隣の1を入れ替える。

一つ後の値
最も右にある0と右隣の1を入れ替える。

"""

# 32bitを想定


def get_big(bit):
    if bit == 0:
        return 'no_one'

    # 初めの0をカウント
    count_bit = bit
    count_zero = 0
    while count_bit & 1 == 0:
        count_zero += 1
        count_bit = count_bit >> 1

    # 続く1のカウント
    count_one = 0
    while count_bit & 1 == 1:
        count_one += 1
        count_bit = count_bit >> 1

    if count_zero + count_one == 31:
        return 'no_bit_value'

    # index, count_zero + count_oneを1に反転する
    bit = bit | 1 << count_zero + count_one
    # index, count_zero + count_one以前を0にクリアする。
    mask_bit = 1 << (count_zero + count_one)
    bit = bit & ~(mask_bit - 1)
    # 右からcount_one　分の1を埋める。
    mask_bit = 1 << count_one - 1
    bit = bit | mask_bit - 1

    return bit


def get_small(bit):
    if bit == 0:
        return 'no small'

    # 初めの1をカウント
    count_bit = bit
    count_one = 0
    while count_bit & 1 == 1:
        count_one += 1
        count_bit = count_bit >> 1

    # 続く0のカウント
    count_zero = 0
    while count_bit & 1 == 0:
        count_zero += 1
        count_bit = count_bit >> 1

    if count_zero + count_one == 31:
        return 'no_bit_value'

    # index, count_zero + count_oneを0に反転する
    mask_bit = 1 << count_zero + count_one
    bit = bit & ~mask_bit
    print(bin(mask_bit))
    print(bin(bit))
    # index, count_zero + count_one以前を0にクリアする。
    mask_bit = 1 << (count_zero + count_one)
    bit = bit & ~(mask_bit - 1)
    # 左から一つ開けてcount_one+1の１を埋める。
    one_bit = (1 << count_one + 1) - 1
    one_bit = one_bit << count_zero - 1
    bit = bit | one_bit

    return bit
