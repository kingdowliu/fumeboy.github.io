"""
使用这个程序来生成索引，会重写 index.md 文件
"""

from __future__ import unicode_literals
import os
cate_dict = {
    'C tutorial': 'C',
    '程序员的自我修养': 'culture',
}
ignore = ['.DS_Store']

strr = ''
print(cate_dict.keys())
for one in cate_dict:
    strr += ('\n' + one + '\n')
    pre_name = cate_dict[one]
    listt = os.listdir('./' + pre_name)
    for two in listt:
        if two in ignore:
            continue
        address = pre_name + '/' + two
        name = ''
        with open(address, 'r') as f:
            for num, line in enumerate(f):
                if num == 0:
                    name = line
                    break
        name = name.split("# ")[-1].split('\n')[0]
        strr += '* [' + name + '](?md=' + address + ')\n'

w = open('./index.md', 'w')
w.write(strr)
w.close()
