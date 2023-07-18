from gendiff.parsing import get_data
from gendiff.comparator import build_tree
from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import format_plain
from gendiff.formatters.json import format_json

FORMAT_STYLISH = 'stylish'
FORMAT_PLAIN = 'plain'
FORMTA_JSON = 'json'


def generate_diff(file1, file2, format='stylish'):
    data1 = get_data(file1)
    data2 = get_data(file2)
    diff_json = build_tree(data1, data2)
    if format == FORMAT_STYLISH:
        return format_stylish(diff_json)
    elif format == FORMAT_PLAIN:
        return format_plain(diff_json)
    elif format == FORMTA_JSON:
        return format_json(diff_json)
