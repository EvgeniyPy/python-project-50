import argparse


def get_args():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files ans shows a difference.'
    )

    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        help='set format of output',
                        default='stylish')

    return parser.parse_args()
