# 文字列の空白を%20に置き換える
# str * int -> str

def insert1(str1, number):
    str_before = str1[:number]
    str_after = str_before.replace(' ', '%20')
    return str_after

# テスト
print(insert1('apple amazon ', 12) == 'apple%20amazon')

# 計算量 
# 消費メモリ



"""
以下解答参照後
"""

# replaceを使用しない。


def insert2(str1, number):
    space_count = 0
    for i in range(number):
        if str1[i] == ' ':
            space_count += 1
            
    str2 = ''
    for i in range(number):
        
            if str1[i] == ' ':
                str2 += '%20'
                need_space -= 3
            else:
                str2 += str1[i]
                need_space -= 1

    return str2


print(insert2('apple amazon ', 12) == 'apple%20amazon')









