import json
from gendiff.parser import parser


def generate_diff(file1, file2):
    file_1, file_2 = parser(file1, file2)
    diff = []
    key_set_file1 = set(file_1.keys())
    key_set_file2 = set(file_2.keys())

    key_remote = key_set_file1 - key_set_file2

    key_add = key_set_file2 - key_set_file1

    key_same = key_set_file1 & key_set_file2

    diff += list(map(lambda x: f'  - {x}: {file_1[x]}', key_remote))
    diff += list(map(lambda x: f'  + {x}: {file_2[x]}', key_add))
    for item in key_same:
        if file_1[item] == file_2[item]:
            diff.append(f'    {item}: {file_1[item]}')
        else:
            diff.append(f'  - {item}: {file_1[item]}')
            diff.append(f'  + {item}: {file_2[item]}')
    diff.sort(key=lambda x: x[4:x.find(':')])
    diff = ['{'] + diff + ['}']
    return '\n'.join(diff)
