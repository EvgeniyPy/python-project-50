import json

PREFIX = {
    'added': '+',
    'removed': '-',
    'unchanged': ' ',
    'changed': {
        'old_value': '-',
        'new_value': '+'
    }
}


INDENT = ' '
POSITION = '{0}{1} {2}: {3}'


def stringify(data, shift):
    result = []
    indent = INDENT * (4 * shift - 2)

    if isinstance(data, dict):
        result.append('{')
        for key, value in data.items():
            result.append(POSITION.format(
                indent, ' ', key, stringify(value, shift + 1)))
        result.append(f'{INDENT * (4 * (shift - 1))}}}')
    elif isinstance(data, str):
        result.append(data)
    else:
        result.append(json.dumps(data))
    return '\n'.join(result)


def format_stylish(data, shift=1):
    result = ['{']
    indent = INDENT * (4 * shift - 2)

    for key, value in sorted(data.items()):
        state = value.get('status')
        value = value.get('value')
        if state == 'changed':
            result.append(POSITION.format(
                indent, PREFIX[state]['old_value'],
                key, stringify(value[1], shift + 1)))
            result.append(POSITION.format(
                indent, PREFIX[state]['new_value'],
                key, stringify(value[0], shift + 1)))
        elif state != 'nested':
            result.append(POSITION.format(
                indent, PREFIX[state], key, stringify(value[0], shift + 1)))

        else:
            result.append(POSITION.format(indent, ' ', key,
                          format_stylish(value, shift + 1)))
    result.append(f'{INDENT * (4 * (shift - 1))}}}')

    return '\n'.join(result)
