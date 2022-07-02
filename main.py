# LunkLog Main File

import argparse

def set_up_args():
    parser = argparse.ArgumentParser(description="Main file for LunkLog")

    parser.add_argument("-p", "--print", action="store_true",
                         help="Print out a friendly message")

    return parser.parse_args()

if __name__ == "__main__":
    args = set_up_args()

    if args.print == True:
        print("Hello World!")
