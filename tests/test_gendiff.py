from own_lib.generate_diff import generate_diff


def test_generate_diff_1():
    file_path1 = 'tests/fixtures/file1.json'
    file_path2 = 'tests/fixtures/file2.json'
    result = open('tests/fixtures/result.txt').read()
    diff = generate_diff(file_path1, file_path2)
    assert diff == result


def test_generate_diff_2():
    file_path1 = 'tests/fixtures/file1.yaml'
    file_path2 = 'tests/fixtures/file2.yml'
    result = open('tests/fixtures/result.txt').read()
    diff = generate_diff(file_path1, file_path2)
    assert diff == result