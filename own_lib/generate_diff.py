# import json


# def generate_diff(first_file, second_file):
#     with open(first_file) as f:
#         data1 = json.load(f)
#     with open(second_file) as f:
#         data2 = json.load(f)

#     keys = set(data1)
#     keys.update(data2)
#     print('{')
#     diff_data = {}

#     for key in keys:
#         key_d1 = key in data1
#         key_d2 = key in data2

#         if key_d1 and key_d2:
#             v1 = data1[key]
#             v2 = data2[key]

#             if v1 == v2:
#                 diff_data[f'  {key}'] = v1
#             else:
#                 diff_data[f'- {key}'] = v1
#                 diff_data[f'+ {key}'] = v2
#         elif key_d1:
#             diff_data[f'- {key}'] = data1[key]
#         else:
#             diff_data[f'+ {key}'] = data2[key]

#     sortdata = dict(sorted(diff_data.items(), key=lambda x: x[0][2]))
#     for key in sortdata:
#         print("    " + key, ':', sortdata[key])
#     print("}")
#     return ' '
import json




def generate_diff(file_path1, file_path2):
    diff = []
    if file_path1.split('.')[1] == 'json':
        file_1 = json.load(open(file_path1))
        file_2 = json.load(open(file_path2))

    else:
        raise Exception('Invalid file format')

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