import json
import yaml


def parser(data, format):
    if format == 'json':
        return json.load(data)
    if format in ('yaml', 'yml'):
        return yaml.safe_load(data)
    raise Exception("Unsupported format, only for json and yaml files")


def get_data(path):
    format = path.split('.')[-1]
    with open(path) as file:
        return parser(file, format)
