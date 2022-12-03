"""
0から1までの数字が与えられた時に２進数で返す。32文字いない。

例
2をかけて行って、１かどうかを判定する
0.58232 -> 1.6464  0.6464 -> 1.298 0.298 -> 0.596 -> 
               1               1              0

数値が0になったら終わり
"""


def float_to_binary(num):
    print(num)
    if num == 0:
        return ''
    else:
        num *= 2
        if num >= 1:
            binary_str = '1'
            num -= 1
            return binary_str + float_to_binary(num)
        else:
            binary_str = '0'
            return binary_str + float_to_binary(num)

    return binary_str

    # 次はwhile文で書いてもいいかも。
    # 出力に合わせて途中で止めるのはwhileの方が書きやすい。
