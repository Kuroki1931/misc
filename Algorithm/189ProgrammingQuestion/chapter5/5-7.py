"""
偶数ビットと奇数ビットを入れ替える最速のプログラムを構築する。

例
10110110
01111001
"""


def change_adjacent(A):
    even_slide = (A & 0xaaaaaaaa) >> 1
    odd_slide = (A & 0x55555555) << 1
    return even_slide | odd_slide
