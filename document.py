"""
Document maker.

This file is made to speed up our work by making a document
while coding in python.
"""
import os
from pdflatex import PDFLaTeX


def struct():
    """Adds needed information for LaTeX."""

    return '\n\\usepackage[english]{babel} \n\\usepackage{microtype} \n\\usepackage{amsmath,amsfonts,amsthm} \n\\usepackage[svgnames]{xcolor} \n\\usepackage[hang, small, labelfont=bf, up, textfont=it]{caption} \n\\usepackage{booktabs} \n\\usepackage{lastpage} \n\\usepackage{graphicx}\n\\usepackage{enumitem}\n\setlist{noitemsep} \n\\usepackage{sectsty} \n \\allsectionsfont{\\usefont{OT1}{phv}{b}{n}} \n\\usepackage{geometry} \n\geometry{top=1cm, bottom=1.5cm, left=2cm, right=2cm, includehead,includefoot,}\n\setlength{\columnsep}{7mm} \n\\usepackage[T1]{fontenc} \n\\usepackage[utf8]{inputenc} \n\\usepackage{XCharter} \n\\usepackage{fancyhdr} \n\pagestyle{fancy} \n\\renewcommand{\headrulewidth}{0.0pt} \n\\renewcommand{\\footrulewidth}{0.4pt} \n \\renewcommand{\sectionmark}[1]{\markboth{#1}{}} \n \lhead{}\n\chead{\\textit{\\thetitle}} \n\\rhead{}\n\lfoot{}\n\cfoot{} \n\\fancypagestyle{firstpage}{\\fancyhf{} \\renewcommand{\\footrulewidth}{0pt}}\n\\newcommand{\\authorstyle}[1]{{\large\\usefont{OT1}{phv}{b}{n}\color{DarkBlue}#1}} \n\\newcommand{\institution}[1]{{\\footnotesize\\usefont{OT1}{phv}{m}{sl}\color{Black}#1}} \n\\usepackage{titling}\n\\newcommand{\HorRule}{\color{black}\\rule{\linewidth}{1pt}} \n\pretitle{	\\vspace{-30pt} 	\HorRule\\vspace{10pt} \\fontsize{32}{36}\\usefont{OT1}{phv}{b}{n}\selectfont \color{DarkBlue}}\n\posttitle{\par\\vskip 10pt} \n\preauthor{} \n\postauthor{ 	\\vspace{10pt} 	\par\HorRule \\vspace{0pt}}\n\\usepackage{lettrine} \n\\usepackage{fix-cm}	\n\\newcommand{\initial}[1]{ 	\lettrine[lines=3,findent=4pt,nindent=0pt]{		\color{DarkGoldenrod}		{#1}}{}}\n\\usepackage{xstring} \n\\newcommand{\lettrineabstract}[1]{	\StrLeft{#1}{1}[\\irstletter] 	\initial{\\irstletter}\\textbf{\StrGobbleLeft{#1}{llsectionsfont1}} }\n\\usepackage[backend=bibtex,style=authoryear,natbib=true]{biblatex} \n\\addbibresource{example.bib} \n\\usepackage[autostyle=true]{csquotes}'

#####
#
#   CLASSES
#


class Title:
    def __init__(self, text):
        self.text = text
        # self.subt = subt

    def get_tex(self):
        return '\documentclass[10pt, a4paper, twocolumn]{article}\n\input{structure.tex}\n\\usepackage{lipsum}\n\\title{%s}\n\date{}\n\\begin{document}\n\maketitle \\thispagestyle{firstpage}' % (self.text)

#
####
#
#   TODO:
#   - split Titel stuff for sub etc...
# .  - make it fancy
#   - check for one column text
#   - prepare for math exersice
#


# class SubTitle:
#    def __init__(self, text):
#        self.text = text
#    def get_tex(self):
#        return '\\author{\\authorstyle{%s}}\n ' % (self.text)

# class SubSubTitle:
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

        for i in range(0, len(self.item_list)):
            s = s + '\t\item %s\n' % (self.item_list[i]) + ' '
        return(s + s_e)  # + '\ '.strip()


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


class Matrix:
    def __init__(self, M, m_n):
        self.M = M
        self.m_n = m_n

    def build_matrix(self):
        m_mid = ''
        for m in range(len(self.m_n)):
            # print(m)
            # %s & %s & %s\n %s & %s & %s \n
            for n in range(len(self.m_n[m])):
                # print('n',n)
                # print(m_n[m][n])
                m_mid = m_mid + str(self.m_n[m][n])
                if (n < len(self.m_n[m])-1):
                    m_mid = m_mid + ' & '
                else:
                    if m == len(self.m_n)-1:
                        continue
                    else:
                        m_mid = m_mid + '\\\[0.3em]'
            m_mid = m_mid + ' \n '
        return m_mid

    def get_tex(self):
        m_begin = '\\begin{bmatrix}\n'
        m_end = '\end{bmatrix}'
        return '\n$ %s = %s %s %s $ ' % (self.M, m_begin, self.build_matrix(), m_end)


class Vector:
    def __init__(self, v, ve_list):
        self.ve_list = ve_list
        self.v = v

    def build_vector(self):
        v_mid = ''
        for m in range(len(self.ve_list)):
            if m != len(self.ve_list)-1:
                v_mid = v_mid + str(self.ve_list[m]) + '\\\ \n'
            else:
                v_mid = v_mid + str(self.ve_list[m]) + ' \n '
        return v_mid

    def get_tex(self,):
        v_beg = '\n\\left(\n \\begin{array}{c}\n'
        v_end = '\end{array}\n \\right)\n'
        return '\n$ \\vec{%s} = %s %s %s $ ' % (self.v, v_beg, self.build_vector(), v_end)

#
#####
#####
#
#   MAIN Document
#


class Document:
    def __init__(self):
        self.blocks = []

    def add_title(self, text):
        t = Title(text)
        self.blocks.append(t)

    # def add_subtitle(self, text):
    #    t = SubTitle(text)
    #    self.blocks.append(t)

    # def add_subsubtitle(self, text):
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

    def add_matrix(self, M, m_n):
        # print('here')
        m = Matrix(M, m_n)
        # print('here')
        self.blocks.append(m)

    def add_vector(self, vector, m_list):
        v = Vector(vector, m_list)
        self.blocks.append(v)

    def write_tex(self):
        tex = ''
        for b in self.blocks:
            tex = tex + b.get_tex()
        tex = tex + '\end{document}'
        with open('somefile.tex', 'w') as tex_main:
            tex_main.write(tex)
        with open('structure.tex', 'w') as tex_struct:
            tex_struct.write(struct())
        # time.sleep(5)
        pdfl = PDFLaTeX.from_texfile('somefile.tex')
        pdf, log, completed_process = pdfl.create_pdf(keep_pdf_file=True, keep_log_file=True)
        # time.sleep(5)
        os.rename('somefile.pdf', 'output.pdf')
        # os.rmdir('some*')
        # os.system('rm some*')
        os.system('rm structure.tex')

        # return tex

    def __repr__(self):
        print("this class adds title, sub-, subsub-, ")


if __name__ == "__main__":

    #####
    #
    #   INPUT
    #

    TITLE = 'This is a TITLE'

    # SUBTITLE = 'A way to describe changes on markets and there customers'
    # SUBSUBTITLE = 'How does it work and how does it look like'

    SECTION = 'This is the first SECTION'
    SECTION2 = 'This is the second SECTION'

    SUBSECTION = 'The first SUBSECTION'
    SUBSECTION2 = "The second SUBSECTION is here"

    SUBSUBSECTION = 'The first and only SUBSUBSECTION'

    ITM1 = 'First  item in a list'
    ITM2 = 'Second  item in a list'
    ITM3 = 'Third  item in a list'
    ITM4 = 'fourth but not least'

    items_list = [ITM1, ITM2, ITM3]
    items_num = [ITM1, ITM2, ITM3, ITM4]

    LAYER1 = 'itemize'
    LAYER2 = 'enumerate'

    # PAR = ['\lipsum[2-4]']*10

    # IMAGE
    IMAGE_TITLE = 'This is a very smal example image.'
    IMAGE_PATH = 'example_pic.png'

    # PAR = ['\n\lipsum[1-2]\n',
    #        '\n\lipsum[2-3]\n',
    #        '\n\lipsum[4-5]\n',
    #        '\n\lipsum[5-6]\n',
    #        '\n\lipsum[8-9]\n',
    #        '\n\lipsum[10-11]\n',
    #        '\n\lipsum[13-15]\n',
    #        '\n\lipsum[18-19]\n',
    #        '\n\lipsum[20-21]\n',
    #        '\n\lipsum[22-23]\n']

    PAR = [
        'Lorem ipsum dolor sit amet, consetetur sadipscing elitr,  sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr,  sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr,  sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.',
        'Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.',
        'Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi.',
        'Nam liber tempor cum soluta nobis eleifend option congue nihil imperdiet doming id quod mazim placerat facer possim assum. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat.',
        'Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis.',
        'At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr,  sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr,  At accusam aliquyam diam diam dolore dolores duo eirmod eos erat, et nonumy sed tempor et et invidunt justo labore Stet clita ea et gubergren, kasd magna no rebum. sanctus sea sed takimata ut vero voluptua. est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr,  sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat. ',
        'Consetetur sadipscing elitr,  sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.',
        'Lorem ipsum dolor sit amet, consetetur sadipscing elitr,  sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr,  sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.',
        'Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exercitation ulliam corper suscipit lobortis nisl ut aliquip ex ea commodo consequat.',
        'Duis autem veleum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel willum lunombro dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi. Li Europan lingues es membres del sam familie. Lor separat existentie es un myth.',
        'Por scientie, musica, sport etc., li tot Europa usa li sam vocabularium. Li lingues differe solmen in li grammatica, li pronunciation e li plu commun vocabules. Omnicos directe al desirabilit… de un nov lingua franca: on refusa continuar payar custosi traductores.',
    ]

    m_n = [[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 2]]
    M = 'P'

#####
#
#   MAIN
#

    paper = Document()

    paper.add_title(TITLE)

    # paper.add_subtitle(SUBTITLE)

    # paper.add_subsubtitle(SUBSUBTITLE)

    paper.add_section(SECTION)

    paper.add_paragraph(PAR[1])

    paper.add_matrix(M, m_n)

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

    paper.add_image(IMAGE_PATH, IMAGE_TITLE)

    paper.add_paragraph(PAR[8])

    paper.add_paragraph(PAR[9])

    paper.write_tex()

    os.system('open output.pdf')
