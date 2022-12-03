"""
目的　
あるbitを他のbit中に上書きする。
例
01100  0110111111  2 6 -> 011 01100 11
手順
1 本体ののi-jのビットを0にする。
2 埋めるビットをj左にシフトさせ、orをとる
"""


def insert_bit(M, N, i, j):
    # Mのi-jを0にマスクする。
    # jまで01のビットを作る
    one_to_j = (1 << j+1) - 1
    # iまでを0にする
    one_i_to_j = one_to_j & i << i
    # 反転させてMをマスクする。
    m_mask = M & ~one_i_to_j
    # return
    return m_mask | N << i


# テスト
M = 0b110111100011010
N = 0b101011
assert bin(insert_bit(M, N, 3, 10)) == '0b110111101011010', 'error'


# 別のマスクの作り方
def insert_bit_2nd(M, N, i, j):
    # Mのi-jを0にマスクする。
    # j+1以降が1となるビットを作る
    one = ~0 << j+1
    # i以前を1にする
    one = one | (1 << i) - 1
    # 反転させてMをマスクする。
    m_mask = M & one
    # return
    return m_mask | N << i
