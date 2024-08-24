# resume builder using markdown files as source
# generates a unique resume based on keyword input

import sys
import argparse

def main():
     print("hello resume builder")
     parser = argparse.ArgumentParser()
     parser.add_argument('filename', help='file location of main.md')
     parser.add_argument('keys', help='file location of keyword source text')
     args = parser.parse_args()


if __name__ == '__main__':
     sys.exit(main())
