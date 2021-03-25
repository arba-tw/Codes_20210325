# -*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

a = '*'
b = ' '
c = 0
d = 0

s = '請輸入正整數：'
s_to_unicode = s.decode(encoding='utf-8')  # 要告訴decode原本的編碼是哪種

c = input(s_to_unicode)

for i in range(c):
    if i <= c/2:
        print(((c/2)-i)*b+i*a+(i-1)*a)
    elif i > c/2:
        d+=1
        print(d*b+((c/2)-d)*a+((c/2)-d-1)*a)
