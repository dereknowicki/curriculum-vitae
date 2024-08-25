# resume builder using markdown files as source
# generates a unique resume based on keyword input

import sys
import argparse
import os.path
import markdown
import yake

def is_valid_file(parser, path):
     if not os.path.exists(path):
          parser.error("file not found %s", path)
     else:
          return open(path, 'r')

def harvest_keywords(keys_str):
     extractor = yake.KeywordExtractor(n=1)
     return extractor.extract_keywords(keys_str)

def build_resume(resume_text, keywords):
     print("building resume")
#     print(resume_text)
     print(keywords)
     return markdown.markdown(resume_text)

def main():
     print("hello resume builder")
     parser = argparse.ArgumentParser()
     parser.add_argument('filename', help='file location of main.md', type=lambda x: is_valid_file(parser, x))
     parser.add_argument('keys', help='file location of keyword source text', type=lambda x: is_valid_file(parser, x))
     args = parser.parse_args()

     keywords = harvest_keywords(args.keys.read())
     html_resume = build_resume(args.filename.read(), keywords)

if __name__ == '__main__':
     sys.exit(main())
