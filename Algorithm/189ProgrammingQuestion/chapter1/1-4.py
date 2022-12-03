# 文字列が回文であるかのチェック(英語想定)
# string -> bool

def check1(str):
    str_modify = str.replace(' ', '').replace('.', '').replace(',', '').lower()
    
    str_reverse=''
    for i in range(len(str_modify)):
        str_reverse += str_modify[-i-1]
        
    if str_reverse == str_modify:
        return True
    else:
        return False

# テスト
print(check1('Step on no pets') == True)
print(check1('A TOYOTA, Race fast, safe car. A TOYOTA') == True)
print(check1('A TOYOTA, Race fast, safe car. A HONDA') == False)


        


"""
以下解答参照後
"""

# 問題の読み取りを間違えた。
# 回文であるかどうかでなく、並び替えたら回文にできるかどうか。
# 回文にできる= 全ての文字数が偶数、または１文字だけ奇数。


def check2(str1):
    str2 = str1.replace(' ', '').replace('.', '').replace(',', '').lower()

     # 各文字をカウントして、全ての文字数が偶数、または１文字だけ奇数であることを確認する。
    azList = [chr(ord("a")+i) for i in range(26)]
        
    odd_count = 0
    for i in azList:
        counts = str2.count(i)
        if counts % 2 == 1:
            odd_count += 1
    
    if odd_count > 1:
        return False
    else:
        return True

# テスト
print(check2('Step on no pets') == True)
print(check2('A TOYOTA, Race fast, safe car. A TOYOTA') == True)
print(check2('A TOYOTA, Race fast, safe car. A HONDA') == False)







    

    
         
         

     

