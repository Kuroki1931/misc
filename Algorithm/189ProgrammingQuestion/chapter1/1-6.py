# 連続した文字の連なりを数字で表現する
# str -> str
# 例 aaabbbAAA -> a3b3A3
# 例 aabAD ->a2b1A1D1 -> aabAD

def check1(str1):

    count = 1
    str2 = ''
    for i in range(1, len(str1)):

        if str1[i] != str1[i-1]:
            str2 = str2 + str1[i-1] + str(count)
            count = 1
        if str1[i] == str1[i-1]:
            count += 1
        if str1[i+1:] == '':
            str2 = str2 + str1[i-1] + str(count)

    if len(str1) <= len(str2):
        return str1
    else:
        return str2


# test
print(check1('AABBCCDD') == 'AABBCCDD')
print(check1('AAABBBCCCDD') == 'A3B3C3D2')


"""
以下回答参照後
"""

# C言語とpythonではindex out of rangeの仕様が異なる？

# stringは固定長で足し合わせるには新しい文字列を毎回作り直す必要があって、計算量が増える。
# のであらかじめstringbuilderで可変長の文字列を作ってそこに加えていく。
# pythonではリストを作成してappendしていく


def check1(str1):

    count = 1
    str2_list = []
    for i in range(1, len(str1)):

        if str1[i] != str1[i-1]:
            str2_list.append(str1[i-1])
            str2_list.append(str(count))
            count = 1
        if str1[i] == str1[i-1]:
            count += 1
        if str1[i+1:] == '':
            str2_list.append(str1[i-1])
            str2_list.append(str(count))

    str2 = ''.join(str2_list)

    if len(str1) <= len(str2):
        return str1
    else:
        return str2


# test
print(check1('AABBCCDD') == 'AABBCCDD')
print(check1('AAABBBCCCDD') == 'A3B3C3D2')

"""
feedback後
"""


def check1(str1):

    count = 1
    str2 = ''
    for i in range(1, len(str1)):

        if str1[i] != str1[i-1]:
            str2 = str2 + str1[i-1] + str(count)
            count = 1
        if str1[i] == str1[i-1]:
            count += 1
        if str1[i+1:] == '':
            str2 = str2 + str1[i-1] + str(count)

    return str1 if len(str1) <= len(str2) else str2
