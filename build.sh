#!/bin/bash

asciidoctor -D build resume.adoc

# $OSTYPE == darwin23.0
open -n /Applications/Firefox.app --args file://$PWD/build/resume.html
