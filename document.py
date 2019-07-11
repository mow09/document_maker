#####
#
#   IMPORTS
#
import os
from pdflatex import PDFLaTeX

def give_structure_TeX():
    return '\n\\usepackage[english]{babel} \n\\usepackage{microtype} \n\\usepackage{amsmath,amsfonts,amsthm} \n\\usepackage[svgnames]{xcolor} \n\\usepackage[hang, small, labelfont=bf, up, textfont=it]{caption} \n\\usepackage{booktabs} \n\\usepackage{lastpage} \n\\usepackage{graphicx}\n\\usepackage{enumitem}\n\setlist{noitemsep} \n\\usepackage{sectsty} \n \\allsectionsfont{\\usefont{OT1}{phv}{b}{n}} \n\\usepackage{geometry} \n\geometry{top=1cm, bottom=1.5cm, left=2cm, right=2cm, includehead,includefoot,}\n\setlength{\columnsep}{7mm} \n\\usepackage[T1]{fontenc} \n\\usepackage[utf8]{inputenc} \n\\usepackage{XCharter} \n\\usepackage{fancyhdr} \n\pagestyle{fancy} \n\\renewcommand{\headrulewidth}{0.0pt} \n\\renewcommand{\\ootrulewidth}{0.4pt} \n\\renewcommand{\sectionmark}[1]{\markboth{#1}{}} \n\lhead{}\n\chead{\\textit{\\thetitle}} \n\\rhead{}\n\lfoot{}\n\cfoot{} \n\\ancypagestyle{firstpage}{ \\ancyhf{}\\renewcommand{\\ootrulewidth}{0pt} }\n\\newcommand{\\ruthorstyle}[1]{{\large\\usefont{OT1}{phv}{b}{n}\color{DarkBlue}#1}} \n\\newcommand{\institution}[1]{{\\ootnotesize\\usefont{OT1}{phv}{m}{sl}\color{Black}#1}} \n\\usepackage{titling}\n\\newcommand{\HorRule}{\color{black}\\rule{\linewidth}{1pt}} \n\pretitle{	\vspace{-30pt} 	\HorRule\vspace{10pt} \\ontsize{32}{36}\\usefont{OT1}{phv}{b}{n}\selectfont \color{DarkBlue}}\n\posttitle{\par\vskip 10pt} \n\preauthor{} \n\postauthor{ 	\vspace{10pt} 	\par\HorRule \vspace{0pt}}\n\\usepackage{lettrine} \n\\usepackage{fix-cm}	\n\\newcommand{\initial}[1]{ 	\lettrine[lines=3,findent=4pt,nindent=0pt]{		\color{DarkGoldenrod}		{#1}}{}}\n\\usepackage{xstring} \n\\newcommand{\lettrineabstract}[1]{	\StrLeft{#1}{1}[\\irstletter] 	\initial{\\irstletter}\\textbf{\StrGobbleLeft{#1}{llsectionsfont1}} }\n\\usepackage[backend=bibtex,style=authoryear,natbib=true]{biblatex} \n\\rddbibresource{example.bib} \n\\usepackage[autostyle=true]{csquotes}'

#####
#
#   CLASSES
#

class Title:
    def __init__(self, text):
        self.text = text
        #self.subt = subt
    def get_tex(self):
        return '\documentclass[10pt, a4paper, twocolumn]{article}\n\input{structure.tex}\n\\usepackage{lipsum}\n\\title{%s}\n\date{}\n\\begin{document}\n\maketitle \\thispagestyle{firstpage}' % (self.text)

#
####
#
#   TODO:
#   - split Titel stuff for sub etc...
#.  - make it fancy
#   - check for one column text
#   - prepare for math exersice
#


#class SubTitle:
#    def __init__(self, text):
#        self.text = text
#    def get_tex(self):
#        return '\\author{\\authorstyle{%s}}\n ' % (self.text)

#class SubSubTitle:
#    def __init__(self, text):
#        self.text = text
#    def get_tex(self):
#        return ' %s ' % (self.text)

class Section:
    def __init__(self, text):
        self.text = text
    def get_tex(self):
        return '\n\section{%s} ' % (self.text)

class SubSection:
    def __init__(self, text):
        self.text = text
    def get_tex(self):
        return '\n\subsection{%s} ' % (self.text)

class SubSubSection:
    def __init__(self, text):
        self.text = text
    def get_tex(self):
        return '\n\subsubsection{%s} ' % (self.text)

class Table:
    def __init__(self, style, item_list):
        self.style = style
        self.item_list = item_list
    def get_tex(self):
        s_b = '\\begin{%s}\n' % (self.style)
        s_e = '\end{%s}\n' % (self.style)
        s = s_b

        for i in range(0,len(self.item_list)):
            s = s + '\t\item %s\n' % (self.item_list[i]) +' '
        return(s + s_e) # + '\ '.strip()

class Image:
    def __init__(self, path, title):
        self.path = path
        self.title = title
    def get_tex(self):
        return '\n\\begin{figure}\includegraphics[width=\linewidth]{%s} \caption{%s} \end{figure}\n' % (self.path, self.title)

class Paragraph:
    def __init__(self, text):
        self.text = text
    def get_tex(self):
        return '\n%s' % (self.text)


class Document:
    def __init__(self):
        self.blocks = []

    def add_title(self, text):
        t = Title(text)
        self.blocks.append(t)

    #def add_subtitle(self, text):
    #    t = SubTitle(text)
    #    self.blocks.append(t)

    #def add_subsubtitle(self, text):
    #    t = SubSubTitle(text)
    #    self.blocks.append(t)

    def add_section(self, text):
        t = Section(text)
        self.blocks.append(t)

    def add_subsection(self, text):
        t = SubSection(text)
        self.blocks.append(t)

    def add_subsubsection(self, text):
        t = SubSubSection(text)
        self.blocks.append(t)

    def add_table(self, kind, text_list):
        t = Table(kind, text_list)
        self.blocks.append(t)

    def add_image(self, path, title):
        t = Image(path, title)
        self.blocks.append(t)

    def add_paragraph(self, para):
        p = Paragraph(para)
        self.blocks.append(p)

    def write_tex(self):
        tex = ''
        for b in self.blocks:
            tex = tex + b.get_tex()
        tex = tex + '\end{document}'
        with open('somefile.tex', 'w') as tex_main:
            tex_main.write(tex)
        #time.sleep(5)
        pdfl = PDFLaTeX.from_texfile('somefile.tex')
        pdf, log, completed_process = pdfl.create_pdf(keep_pdf_file=True, keep_log_file=False)
        #time.sleep(5)
        os.rename('somefile.pdf','output.pdf')
        #os.rmdir('some*')
        os.system('rm some*')

        #return tex

    def __repr__(self):
        print("this class adds title, sub-, subsub-, ")


if __name__ == "__main__":

#####
#
#   INPUT
#


    TITLE = 'THIS is a section'

    SUBTITLE = 'A way to describe changes on markets and there customers'
    SUBSUBTITLE = 'How does it work and how does it look like'

    SECTION = 'Malkov Math'
    SECTION2 = 'BEAR and a table'

    SUBSECTION = 'The Chain Formal'
    SUBSECTION2 = "not even a title"

    SUBSUBSECTION = 'Sub sub section'

    ITM1 = 'First  item in a list'
    ITM2 = 'Second  item in a list'
    ITM3 = 'Third  item in a list'
    ITM4 = 'fourth but not least'

    items_list = [ITM1,ITM2,ITM3]
    items_num = [ITM1,ITM2,ITM3, ITM4]

    LAYER1 = 'itemize'
    LAYER2 = 'enumerate'

    #PAR = ['\lipsum[2-4]']*10

    #IMAGE
    IMAGE_TITLE = 'BEAR, man...'
    IMAGE_PATH = 'bear.jpg'


    PAR = ['\n\lipsum[1-2]\n',
     '\n\lipsum[2-3]\n',
     '\n\lipsum[4-5]\n',
     '\n\lipsum[5-7]\n',
     '\n\lipsum[8-9]\n',
     '\n\lipsum[10-12]\n',
     '\n\lipsum[13-17]\n',
     '\n\lipsum[18-19]\n',
     '\n\lipsum[20-21]\n',
     '\n\lipsum[22-23]\n']

#####
#
#   MAIN
#

    paper = Document()

    paper.add_title(TITLE)

    #paper.add_subtitle(SUBTITLE)

    #paper.add_subsubtitle(SUBSUBTITLE)

    paper.add_section(SECTION)

    paper.add_paragraph(PAR[1])

    paper.add_subsection(SUBSECTION)

    paper.add_paragraph(PAR[2])

    paper.add_table(LAYER1, items_list)

    paper.add_paragraph(PAR[3])

    paper.add_section(SECTION2)

    paper.add_paragraph(PAR[4])

    paper.add_subsection(SUBSECTION)

    paper.add_paragraph(PAR[5])

    paper.add_subsubsection(SUBSUBSECTION)

    paper.add_paragraph(PAR[6])

    paper.add_table(LAYER2, items_num)

    paper.add_paragraph(PAR[7])

    paper.add_image(IMAGE_PATH,IMAGE_TITLE)

    paper.add_paragraph(PAR[8])

    paper.write_tex()

    os.system('open output.pdf')
