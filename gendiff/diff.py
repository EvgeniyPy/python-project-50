from gendiff.parsing import parser
from gendiff.comparator import comparator
from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import format_palin
from gendiff.formatters.json import format_json
FORMAT_STYLISH = 'stylish'
FORMAT_PLAIN = 'plain'
FORMTA_JSON = 'json'


def generate_diff(file1, file2, format='stylish'):
    data1, data2 = parser(file1, file2)
    diff_json = comparator(data1, data2)
    if format == FORMAT_STYLISH:
        return format_stylish(diff_json)
    elif format == FORMAT_PLAIN:
        return format_palin(diff_json)
    elif format == FORMTA_JSON:
        return format_json(diff_json)
    # else:
    #     raise Exception("Wrong format")
