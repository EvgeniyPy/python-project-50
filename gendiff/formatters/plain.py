FORMAT_PLAIN = 'plain'


PREFIX = {
    'added': 'Property \'{0}\' was added with value: {1}',
    'removed': 'Property \'{0}\' was removed',
    'changed': 'Property \'{0}\' was updated. From {1} to {2}'
}


def stringify(data):
    if isinstance(data, dict) or isinstance(data, list):
        return '[complex value]'
    elif isinstance(data, str):
        return f"'{data}'"
    elif data is None:
        return 'null'
    elif isinstance(data, bool):
        return 'true' if data else 'false'
    else:
        return data


def format_plain(data, path=None):
    if path is None:
        path = []
    result = []

    for key, value in sorted(data.items()):
        state = value.get('status')
        value = value.get('value')

        path.append(key)

        if state == 'added':
            result.append(PREFIX[state].format(
                '.'.join(path), stringify(value[0])))
        elif state == 'removed':
            result.append(PREFIX[state].format('.'.join(path), value[0]))
        elif state == 'changed':
            result.append(PREFIX[state].format(
                '.'.join(path), stringify(value[1]), stringify(value[0])))
        elif state == 'nested':
            result.append(format_plain(value, path))
        path.pop()

    return '\n'.join(result)
