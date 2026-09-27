# resume builder using markdown files as source
# generates a unique resume based on keyword input

import sys
import argparse
import os.path
import markdown
import yake
from bs4 import BeautifulSoup

def is_valid_file(parser, path):
     if not os.path.exists(path):
          parser.error("file not found %s", path)
     else:
          return open(path, 'r')

def export_to_html(html_str, filename):
     with open(f"../{filename}.html", "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
          output_file.write(html_str)

def harvest_keywords(keys_str):
     extractor = yake.KeywordExtractor(n=1)
     return extractor.extract_keywords(keys_str)

def job_description_includes(html):
     html_dom = BeautifulSoup(html, 'html.parser')
     #print(html_dom.prettify())
     for tag in html_dom.find_all('a'):
         # print(f".{tag['href']}")
          if not os.path.exists(f".{tag['href']}"):
              print("nope")
              return html
          with open(f".{tag['href']}", 'r') as md_file:
              html_dom.find('h1').append(BeautifulSoup(markdown.markdown(md_file.read()), 'html.parser'))
          tag.parent.decompose() #delete tag and its parent 
    # print(html_dom.prettify())
     return html_dom

def build_resume(resume_text, keywords):
     resume_html = markdown.markdown(resume_text)
     resume_html = job_description_includes(resume_html) #include job descriptions from linked markdown files list
     return resume_html

def score_resume(bs_html, keywords):
     for tag in bs_html.find_all(['p', 'li']):
          content = ''.join(tag.contents)
          score = 0
          for key in keywords:
               #print(f"searching for {key[0]} in:\n\t {content}")
               if content.find(key[0]) > -1:
                  # print(f"{key[0]} found. adding {key[1]} to score")
                   score += key[1]
          if args.a is not None:
              ann = bs_html.new_tag('span')
              ann.string = f"^^^final score: {score}"
              ann['style'] = 'color:red;font-weight: bold'
              tag.insert_after(ann)
              #print(f"final score {score}")
     return bs_html

def export_linkedin(bs_html):
     print("exporting linkedin text")
     export_to_html(str(bs_html), "linkedin")

def export_indeed(bs_html):
     print("exporting indeed text")
     export_to_html(str(bs_html), "indeed")

def export_glassdoor(bs_html):
     print("exporting glassdoor text")
     export_to_html(str(bs_html), "glassdoor")

def export_pretty_resume(bs_html):
     print("exporting pretty human readable resume")
     export_to_html(str(bs_html), "pretty")

def main():
     keywords = harvest_keywords(args.keys.read())
     html_resume = build_resume(args.filename.read(), keywords)

     #score each p and li based on keyword matching
     score_resume(html_resume, keywords)

     export_to_html(str(html_resume), "resume_full")

     if args.L is not None:
         export_linkedin(html_resume)

     if args.I is not None:
         export_indeed(html_resume)

     if args.G is not None:
         export_glassdoor(html_resume)

     if args.P is not None:
         export_pretty_resume(html_resume)

if __name__ == '__main__':
     print("hello resume builder")
     parser = argparse.ArgumentParser()
     parser.add_argument('filename', help='file location of main.md', type=lambda x: is_valid_file(parser, x))
     parser.add_argument('keys', help='file location of keyword source text', type=lambda x: is_valid_file(parser, x))
     parser.add_argument('-a', help='export resume with annotations', nargs='?', const=False)
     parser.add_argument('-L', help='export linkedin sections', nargs='?', const=False)
     parser.add_argument('-I', help='export Indeed profile text', nargs='?', const=False)
     parser.add_argument('-G', help='export Glassdoor profile text', nargs='?', const=False)
     parser.add_argument('-P', help='export pretty resume for humans', nargs='?', const=False)
     args = parser.parse_args()
     #print(args.a)

     sys.exit(main())
