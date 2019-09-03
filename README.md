[![Build Status](https://travis-ci.com/mow09/document_maker.svg?token=3YzpCr7zqrJRwks2k22w&branch=master)](https://travis-ci.com/mow09/document_maker)

# Making Document

Is there to speed up good documented work.

It is not perfect jet but in can make:
- Sections, Sub- and Subsections
- Vectors, Matrices
- Paragraphs
- Images
- Tables
	- itemize and
	2. numeric
- and naturally of course a title

## creating a pdf with LaTeX
To create a pdf it uses LaTeX which makes it all flexible.
But still there are a few things...

## missing

- [ ] a subtitle for more information
- [ ] more math than mat and vec
	- [ ] formula
- [ ] Graphs without images
- [ ] a solo column output file
- [ ] a QR for a reimplement
	- [ ] contains random seed for correction
	- [ ] analyzable
- [ ] add Lorem ipsum :smile: :+1:
- [ ] overwork struct .tex for the rest
- [ ] create TEST without an LaTex envirement
---
## just works with TEX set up
I recommend [TeXstudio](https://www.texstudio.org) and [LaTeX](https://www.latex-project.org/get/)

---
# Try it:

1. clone it (`git clone https://github.com/mow09/document_maker.git`)
2. make env (`virtualenv doc_maker`) in my_path
	- (!) `source my_path/doc_maker/bin/activate`
3. install requirements `pip install -r requirements` in env
4. run `python document.py` to see an example
