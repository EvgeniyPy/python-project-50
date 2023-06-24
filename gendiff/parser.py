import json
import yaml
from yaml import SafeLoader

def parser(file1, file2):
    if file1.split('.')[1] == 'json':
        file_1 = json.load(open(file1))
        file_2 = json.load(open(file2))
    if file1.split('.')[1] in ('yaml', 'yml'):
        file_1 = yaml.load(open(file1), Loader=SafeLoader)
        file_2 = yaml.load(open(file2), Loader=SafeLoader)
    return file_1, file_2




