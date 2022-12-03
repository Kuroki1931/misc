"""
AからBに変換するために必要なビット数を求める。
# 長さが同じ
11010   10101 
一つずつ比べる

# 長さが異なる場合
10101011   11010
"""

# 32bitを想定


def different_bit_num(A, B):
    count = 0
    for i in range(32):
        A_most_right = A & 1 << i
        B_most_right = B & 1 << i

        if A_most_right != B_most_right:
            count += 1

    return count

    assert different_bit_num(0b111, 0b000) == 3, 'error'

    """
    解答参照後
    """
