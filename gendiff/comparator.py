def comparator(data1, data2):
    file_1, file_2 = data1, data2
    diff = {}
    key_set_file1 = set(file_1.keys())
    key_set_file2 = set(file_2.keys())

    key_remote = key_set_file1 - key_set_file2

    key_add = key_set_file2 - key_set_file1

    key_same = key_set_file1 & key_set_file2

    for key in key_add:
        value = file_2[key]
        diff[key] = {'status': 'added', 'value': [value]}

    for key in key_remote:
        value = file_1[key]
        diff[key] = {'status': 'removed', 'value': [value]}

    for key in key_same:
        value_1 = file_1[key]
        value_2 = file_2[key]
        if isinstance(file_1[key], dict) and isinstance(file_2[key], dict):
            diff[key] = {'status': 'nested',
                         'value': comparator(value_1, value_2)}
        elif file_2[key] != file_1[key]:
            diff[key] = {'status': 'changed', 'value': [value_2, value_1]}

        else:
            diff[key] = {'status': 'unchanged', 'value': [value_1]}

    return diff
