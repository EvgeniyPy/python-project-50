import json


def generate_diff(first_file, second_file):
    with open(first_file) as f:
        data1 = json.load(f)
    with open(second_file) as f:
        data2 = json.load(f)

    keys = set(data1)
    keys.update(data2)
    print('{')
    diff_data = {}

    for key in keys:
        key_d1 = key in data1
        key_d2 = key in data2

        if key_d1 and key_d2:
            v1 = data1[key]
            v2 = data2[key]

            if v1 == v2:
                diff_data[f'  {key}'] = v1
            else:
                diff_data[f'- {key}'] = v1
                diff_data[f'+ {key}'] = v2
        elif key_d1:
            diff_data[f'- {key}'] = data1[key]
        else:
            diff_data[f'+ {key}'] = data2[key]

    sortdata = dict(sorted(diff_data.items(), key=lambda x: x[0][2]))
    for key in sortdata:
        print("    " + key, ':', sortdata[key])
    return '}'
