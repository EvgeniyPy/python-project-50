from gendiff.cli import get_args
from gendiff.diff import generate_diff


def main():
    # parser = argparse.ArgumentParser(
    #     description='Compares two configuration files and shows a difference.'
    # )
    # parser.add_argument('first_file', type=str)
    # parser.add_argument('second_file', type=str)
    # parser.add_argument(
    #     '-f', '--format', help='set format of output'
    # )
    args = get_args()
    # print(args.format)
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == "__main__":
    main()
