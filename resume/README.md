# Resume

This document contains all of my work and education history in a comprehensive document. The intent of this document is to serve as a base for company-specific resumes.

You will need LyX Document processor to render the document to pdf.
http://www.lyx.org/Download

# ModernCV Documentation

There is no official documentation for the modernCV document class. The following is documentation that I drafted for my own use:

## Preamble
* The personal data like your name, image, address, etc. are set in the document preamble.
* You can view/edit the preamble by going to Document->Settings...->LaTeX Preamble
* To use the latext preamble as the title, you must insert some latext code at the top of the document to ensure that it will render:
	1. Insert -> Tex Code
	2. Paste the following code into the "erb": `\maketitle`
* When starting a new lyx document of this class the preamble will be empty. You can copy/paste the following code to begin with

```latex
% adjust the page margins
\usepackage[scale=0.75]{geometry}

\moderncvtheme[blue]{classic}
% possible themes are "classic" and "casual"
% optional argument are 'blue' (default), 'orange', 'red', 'green', 'grey' and 'roman' (for roman fonts, instead of sans serif fonts)

% required
\firstname{Derek}
% required
\familyname{Nowicki}

% optional, remove the line if not wanted
\title{Curriculum Vitae}

% optional
% \address{street and number}{postcode city}
% '\\' adds a line break
\address{5555 First Ave.}{Los Angeles, CA\protect\\[0.1em] 90041\protect\\[0.2em]}

% optional
\phone{555-123-4567}
% optional
%\mobile{+43(0)999 888}
% optional
%\fax{+43(0)999 7777}
% optional
\email{emailaddress@example.com}
% optional
%\extrainfo{www.lyx.org}

% optional
% \photo[height]{name}
% 'height' is the height the picture is resized to
% 'name' is the name of the picture file
%\photo[64pt]{CV-image}

% optional
%\quote{"You only live twice." (an optional quote)}
```

## Entry Section
* This is meant to be used for a job position or educational institution entry and it must follow the following format:

```latex
{year--year}{degree achieved/job title}{Institution/Company Name}{City}{State}{Description}
```
1. Set the section to Entry
2. Type in the year argument
3. Insert->Tex code
  * Type }{ into the "ert" box
4. Type in the degree/job title argument
5. Insert another }{ for each of the remaining arguments
  * There should be 5 total
6. Check that there are 6 total sections
  1. View the source code: View->View Source
  * Arguments 3 to 6 can be left empty

## Item Section
* This section is a two-argument item that can be used in many ways.
* It has the form:

```
{stuff}{things}
```

  * Both arguments are required
  * The first argument will be in the left column and the second argument will be in the right column
1. Set section to Item
2. Type in first argument
3. Insert->Tex code
  * Type }{ into the "ert" box
4. Type in second argument

## List Item
* The list item will get a nice little bubble next to it on the document
1. Set section to List Item
2. Write item text

## List Sub-Items
* The List Item section can be set up with sub-items using the itemize tag
1. Insert->Tex code
  * ` \begin{itemize}\item `
  * NOTE: There needs to be a whitespace at the end of the above code. VERY IMPORTANT!
2. Each additional child item can be annotated with this code:
  * ` \item `
  * NOTE: There needs to be a whitespace at the end of the above code. VERY IMPORTANT!
2. After that "ert" you can write whatever you want in your sub-item text
3. Insert->Tex code
  * ` \end{itemize}`
    * This marks the end of the itemized list

## Double Item
* Basically 2 items in a row and seperated into columns
* Also gets a nice bubble next to the line in the document
* fits the form:

```latex
{item left }{ item right}
```

* neither arguments are required so you can leave them both blank
1. Set section to Double Item
2. Write item left text
3. Insert->Tex code
  * }{
4. Write item right text

## Computer
* This section is a two-column list, where each column has a header.
* this is the form:

```latex
{Category 1}{List item, list item}{Category2}{list item, list item, list item}
```

* The format will look like this:
Category1    List item, list item    Category2    list item, list item,
                                                  list item
* The best way to do this is to consider Category1 as a general category and Category2 as a specific sub-category
  * An Example would be Category1=OS and Category2=Administration
    * Category1 would be a list of operating systems I know how to USE
    * Category2 would be a list of operating systems I know how to ADMINISTER
* None of the arguments are required so you can have an empty Category2 if there isnt really a more specific subcategory for Category1

## Unformatted Content
* If you need to have content that the document class will ignore, you can add a Close Section section.
* the unformatted section ends at the next end of line character.

## Empty Section
* This section will format all of its contents with modercv layout, but it will not have a section heading

## Space
* This section will insert a verticle space
* Has one argument that must have a number and a unit of measure.
* These are the valid units of measure:

| | | |
|:---:|:---:|:---:|
| pt | point | (1 in = 72.27 pt) |
| pc | pica | (1 pc = 12 pt) |
| in | inch | (1 in = 25.4 mm) |
| bp | big point | (1 in = 72 bp) |
| cm | centimetre | (1 cm = 10 mm) |
| mm | millimetre |  |
| dd | didot point | (1157 dd = 1238 pt) |
| cc | cicero | (1 cc = 12 dd) |
| sp | scaled point | (65536 sp = 1 pt) |


## Bibliography
* This section will enter a bibtex section
* The section header will read "References"
* Left-click the grey box to edit the key and label
  * The key property is used to reference the bib item in the document
  * The text of the label property will show up in the left column
* The text to the right of the gray box will show up in the right column of the section
