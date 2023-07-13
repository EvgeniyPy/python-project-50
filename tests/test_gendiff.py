from gendiff.diff import generate_diff, FORMAT_STYLISH, FORMAT_PLAIN, FORMTA_JSON
import pytest


@pytest.mark.parametrize('file1, file2, format, result_file', (
    ('file1.json', 'file2.json', FORMAT_STYLISH, 'result.txt'),
    ('file1.yaml', 'file2.yml', FORMAT_STYLISH, 'result.txt'),
    ('file6_1.json', 'file6_2.json', FORMAT_STYLISH, 'Result_stylish.txt'),
    ('test_diff.yaml', 'test_diff2.yml', FORMAT_STYLISH, 'Result_stylish.txt'),
    ('file6_1.json', 'file6_2.json', FORMAT_PLAIN, 'result_plain.txt'),
    ('test_diff.yaml', 'test_diff2.yml', FORMAT_PLAIN, 'result_plain.txt'),
    ('file6_1.json', 'file6_2.json', FORMTA_JSON, 'result_json.txt'),

))
def test_generate_diff_stylish(file1, file2, format, result_file):

    file_path1 = 'tests/fixtures/' + file1
    file_path2 = 'tests/fixtures/' + file2
    result = open('tests/fixtures/' + result_file).read()
    diff = generate_diff(file_path1, file_path2, format)
    assert diff == result
