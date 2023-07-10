from gendiff.diff import generate_diff, FORMAT_STYLISH, FORMAT_PLAIN
import pytest

# def test_generate_diff_1():
#     file_path1 = 'tests/fixtures/file1.json'
#     file_path2 = 'tests/fixtures/file2.json'
#     result = open('tests/fixtures/result.txt').read()
#     diff = generate_diff(file_path1, file_path2)
#     assert diff == result


# def test_generate_diff_2():
#     file_path1 = 'tests/fixtures/file1.yaml'
#     file_path2 = 'tests/fixtures/file2.yml'
#     result = open('tests/fixtures/result.txt').read()
#     diff = generate_diff(file_path1, file_path2)
#     assert diff == result

# def test_generate_diff3():
#     file_path1 = 'tests/fixtures/file6_1.json'
#     file_path2 = 'tests/fixtures/file6_2.json'
#     result = open('tests/fixtures/Result_stylish.txt').read()
#     diff = generate_diff(file_path1, file_path2)
#     assert diff == result




@pytest.mark.parametrize('file1, file2, result_file', (
        ('file1.json', 'file2.json', 'result.txt'),
        ('file1.yaml', 'file2.yml', 'result.txt'),
        ('file6_1.json', 'file6_2.json', 'Result_stylish.txt'),
        ('test_diff.yaml', 'test_diff2.yml', 'Result_stylish.txt'),
        
))
def test_generate_diff_stylish(file1, file2, result_file):


    file_path1 = 'tests/fixtures/' + file1
    file_path2 = 'tests/fixtures/' + file2
    result = open('tests/fixtures/' + result_file).read()
    diff = generate_diff(file_path1, file_path2, FORMAT_STYLISH)
    assert diff == result

@pytest.mark.parametrize('file1, file2, result_file', (
        
        ('file6_1.json', 'file6_2.json', 'result_plain.txt'),
        ('test_diff.yaml', 'test_diff2.yml', 'result_plain.txt'),
      

))        
def test_generate_diff_plain(file1, file2, result_file):


    file_path1 = 'tests/fixtures/' + file1
    file_path2 = 'tests/fixtures/' + file2
    result = open('tests/fixtures/' + result_file).read()
    diff = generate_diff(file_path1, file_path2, FORMAT_PLAIN)
    assert diff == result
