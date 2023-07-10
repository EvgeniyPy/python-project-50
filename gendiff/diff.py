from gendiff.parsing import parser
from gendiff.comparator import comparator
from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import format_palin
FORMAT_STYLISH = 'stylish'
FORMAT_PLAIN = 'plain'


def generate_diff(file1, file2, format):
    data1, data2 = parser(file1, file2)
    if format == FORMAT_STYLISH:
        return format_stylish(comparator(data1, data2))
    elif format == FORMAT_PLAIN:
        return format_palin(comparator(data1, data2))
    else:
        raise Exception(f"Wrong format")
