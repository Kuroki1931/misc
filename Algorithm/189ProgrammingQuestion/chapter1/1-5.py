# 文字の置き換え、削除、挿入のいずれかで作成することができるか
# int * int -> bool


def check1(str1, str2):
    if len(str1) == len(str2):
        # 置き換え
        # 例: apple bpple
        # n-1文字の位置が同じ

        count = 0
        for i in range(len(str1)):
            if str1[i] == str2[i]:
                count += 1

        if count == len(str1)-1:
            return True
        else:
            return False

    if len(str1)+1 == len(str2):
        # 挿入
        # 例: I'mTom I'm Tom
        # 左からチェックしていき、同じじゃない文字を見つけたら削除→両文を比べる

        str1 += ' '

        for i in range(len(str1)):
            if str1[i] != str2[i]:
                str2 = str2[:i] + str2[i+1:]
                str1 = str1[:-1]
                break

        if str1 == str2:
            return True
        else:
            return False

    if len(str1)-1 == len(str2):
        # 削除
        # 例: soccer socce
        # 挿入と同様

        str2 += ' '

        for i in range(len(str1)):
            if str1[i] != str2[i]:
                str1 = str1[:i] + str1[i+1:]
                str2 = str2[:-1]
                break

        if str1 == str2:
            return True
        else:
            return False

    else:
        return False


# test
print(check1('apple', 'bpple') == True)
print(check1('ImTom', 'Im Tom') == True)
print(check1('rion', 'human') == False)
print(check1('pale', 'ple') == True)


"""
以下解答参照後
"""
# 挿入と削除は文字を入れ替えればよいだけ。


"""
#不自然な気がするがクラスで書いてみた。
#うまく書けなかったので保留。


class check2():

    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2

    def check(self, str1, str2):
        if len(self.str1) == len(self.str2):
            return self.lenEquol(self.str1, self.str2)
        if len(self.str1) + 1 == len(self.str2):
            return self.lenNotEquol(self.str1, self.str2)
        if len(self.str1) == len(self.str2) + 1:
            return self.lenNotEquol(self.str2, self.str1)
        

    def lenEquol(self, str1, str2):
        # 置き換え
        # 例: apple bpple
        # n-1文字の位置が同じ

        count = 0
        for i in range(len(self.str1)):
            if self.str1[i] == self.str2[i]:
                count += 1

        if count == len(self.str1)-1:
            return True
        else:
            return False
                
    def letNotEquol(self, str1, str2):
        # 挿入
        # 例: I'mTom I'm Tom
        # 左からチェックしていき、同じじゃない文字を見つけたら削除→両文を比べる

        str1 += ' '

        for i in range(len(self.str1)):
            if self.str1[i] != self.str2[i]:
                self.str2 = self.str2[:i] + self.str2[i+1:]
                self.str1 = self.str1[:-1]
                break

        if self.str1 == self.str2:
               return True
        else:
            return False
 
# test

print(check2('apple', 'bpple') == True)
print(check2('ImTom', 'Im Tom') == True)
print(check2('rion', 'human') == False)
print(check2('pale', 'ple') == True)
"""


"""
feedback後
"""


def compare_two_list(str1, str2):
    if len(str1) == len(str2):
        count = 0
        for i in range(len(str1)):
            if str1[i] == str2[i]:
                count += 1

        return count == len(str1) - 1

    if len(str1)+1 == len(str2):
        str1 += ' '

        for i in range(len(str1)):
            if str1[i] != str2[i]:
                str2 = str2[:i] + str2[i+1:]
                str1 = str1[:-1]
                break

        return str1 == str2

    if len(str1)-1 == len(str2):
        str2 += ' '

        for i in range(len(str1)):
            if str1[i] != str2[i]:
                str1 = str1[:i] + str1[i+1:]
                str2 = str2[:-1]
                break

        return str1 == str2

    else:
        return False

# test


def test_compare_two_list():
    assert compare_two_list('pale', 'ple')
