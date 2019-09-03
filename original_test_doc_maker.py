"""Test if the doc maker makes an pdf."""

import os
import document


def test_doc_maker():
    """Just makes a doc and deletes it."""
    TITLE = 'This is a TITLE'

    SECTION = 'This is the first SECTION'
    SECTION2 = 'This is the second SECTION'

    SUBSECTION = 'The first SUBSECTION'

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

    paper = document.Document()

    paper.add_title(TITLE)

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

    assert os.path.isfile('output.pdf')

    os.remove('output.pdf')

    assert not os.path.isfile('output.pdf')
