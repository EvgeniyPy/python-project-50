import pytest 
from gendiff.diff import generate_diff, FORMAT_STYLISH, FORMAT_PLAIN, FORMTA_JSON



@pytest.mark.parametrize('file1, file2, format, result_file', (
    ('flat1.json', 'flat2.json', FORMAT_STYLISH, 'flat_result.txt'),
    ('flat1.yaml', 'flat2.yaml', FORMAT_STYLISH, 'flat_result.txt'),
    ('nested1.json', 'nested2.json', FORMAT_STYLISH, 'result_stylish.txt'),
    ('nested1.yaml', 'nested2.yaml', FORMAT_STYLISH, 'result_stylish.txt'),
    ('nested1.yml', 'nested2.yml', FORMAT_STYLISH, 'result_stylish.txt'),
    ('nested1.json', 'nested2.json', FORMAT_PLAIN, 'result_plain.txt'),
    ('nested1.yaml', 'nested2.yaml', FORMAT_PLAIN, 'result_plain.txt'),
    ('nested1.json', 'nested2.json', FORMTA_JSON, 'result_json.txt'),
    ('nested1.yaml', 'nested2.yaml', FORMTA_JSON, 'result_json.txt'),

))
def test_generate_diff(file1, file2, format, result_file):

    file_path1 = 'tests/fixtures/' + file1
    file_path2 = 'tests/fixtures/' + file2
    result = open('tests/fixtures/' + result_file).read()
    diff = generate_diff(file_path1, file_path2, format)
    assert diff == result
