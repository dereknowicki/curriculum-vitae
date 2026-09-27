#!/bin/bash

# asciidoctor -D build resume.adoc
#
# # $OSTYPE == darwin23.0
# open -n /Applications/Firefox.app --args file://$PWD/build/resume.html

# recursively build subdirectories #
# function print_dirs() {
#     for any in $1/*; do
#         if [ -d $any ]; then
#             echo $any
#             print_dirs $any
#         fi
#     done
# }
#
# print_dirs $PWD
