import argparse
from pathlib import Path

from .hash import hash_file, hash_string


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=str,
                        help="Input string to hash (or path to a file if -f).")
    parser.add_argument("-f", "--file", action="store_true",
                        help="To hash a file.")
    parser.add_argument("-o", "--output", choices=["x", "b", "d"], default="x",
                        help="Output format (hexadecimal, binary or decimal)")
    parser.add_argument("--encoding", type=str, default=None,
                        help="Encoding to use (when hashing a string).")
    return parser.parse_args()


def main():
    args = parse_args()

    if not args.file:  # process input directly as a string
        hash_value = hash_string(args.input, encoding=args.encoding)

    else:  # input is a file
        path = Path(args.input)
        if not path.is_file():
            raise FileNotFoundError(path)
        if args.encoding is not None:
            print(f"WARNING: '--encoding {args.encoding}' won't be used since we directly hash a file ({path}).")
        hash_value = hash_file(path)

    # Print output
    if args.output == "x":
        print(hash_value.hex())
    elif args.output == "b":
        print(hash_value.bin())
    else:
        print(hash_value)


if __name__ == "__main__":
    main()
