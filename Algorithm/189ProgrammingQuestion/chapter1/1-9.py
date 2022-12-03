# ヒントを見た。
# str2がstr1を回転させたものか判定する。
# int * int -> bool

def kaiten(str1, str2):
    str3 = str2 + str2
    if len(str1) == len(str2) & isStubstring(str1, str3):
        return True
    else:
        return False


"""
解答と同じ
"""

"""
feedback後
"""


def kaiten(str1, str2):
    str3 = str2 + str2
    return len(str1) == len(str2) & isStubstring(str1, str3)
