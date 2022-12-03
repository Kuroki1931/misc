# 2つの文字が並び替えによるものか確認
# int * int -> bool

def check1(str1, str2):
    if len(str1) == len(str2):
        for i in range(len(str1)):
            a = str1[i]

            if a in str2:
                str2 = str2.replace(a, '', 1)
            else:
                return False

        return True

    else:
        return False


print(check1('apple', 'ppela') == True)
print(check1('apple', 'apple1') == False)
print(check1('amazon', 'amaZon') == False)

# 計算量 str1の文字の長さ: O(n)　
# 消費メモリ 二文字分


"""
回答参照後
"""
# 文字の大小、空白が意味を成すか確認。

# ①ソートして比べる。


def check2(str1, str2):
    if sorted(str1) == sorted(str2):
        return True

    return False


print(check2('apple', 'ppela') == True)
print(check2('apple', 'apple1') == False)
print(check2('amazon', 'amaZon') == False)

# 計算量　O(N)
# 消費メモリ 2文字文


# ②ASCIIと仮定する。

def check3(str1, str2):
    if len(str1) == len(str2):
        ascii_list = [0] * 128

        for i in range(len(str1)):
            ascii_list[ord(str1[i])] += 1

        for i in range(len(str2)):
            ascii_list[ord(str2[i])] -= 1

        if ascii_list == [0] * 128:
            return True
        else:
            return False

    else:
        return False


print(check3('apple', 'ppela') == True)
print(check3('apple', 'apple1') == False)
print(check3('amazon', 'amaZon') == False)


# 計算量　O(N)
# 消費メモリ 2文字文+asciiリスト？？


"""
feedback後
"""


def two_strings_use_same_string(str1, str2):
    if len(str1) == len(str2):
        for i in str1:
            if i in str2:
                str2 = str2.replace(i, '', 1)
            else:
                return False
        return True
    else:
        return False


def test_two_string_use_same_string():
    assert two_strings_use_same_string('apple', 'ppela')
