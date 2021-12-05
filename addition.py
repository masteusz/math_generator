import pylatex.tikz
from pylatex import Document, PageStyle, Head, MiniPage, LineBreak, MediumText, Math, LargeText, VerticalSpace, HugeText
from pylatex.utils import NoEscape
from equation_gen import generate_equation

if __name__ == "__main__":
    geometry_options = {"head": "40pt", "margin": "0.5in", "bottom": "0.6in", "includeheadfoot": True}

    doc = Document("addition", geometry_options=geometry_options)
    first_page = PageStyle("firstpage")

    with first_page.create(Head("L")) as header_left:
        with header_left.create(MiniPage(width=NoEscape(r"0.49\textwidth"), pos="c")) as name_wrapper:
            with name_wrapper.create(pylatex.TikZ()) as pic:
                pic.append(pylatex.TikZDraw(["(0,0)", "--", "++(5,0)"]))
            name_wrapper.append(LineBreak())
            name_wrapper.append(MediumText("Name"))

    with first_page.create(Head("R")) as right_header:
        with right_header.create(MiniPage(width=NoEscape(r"0.49\textwidth"), pos="c", align="r")) as date_wrapper:
            with date_wrapper.create(pylatex.TikZ()) as pic:
                pic.append(pylatex.TikZDraw(["(0,0)", "--", "(5,0)"]))
            date_wrapper.append(LineBreak())
            date_wrapper.append(MediumText("Date"))

    doc.change_document_style("firstpage")
    doc.preamble.append(first_page)
    doc.append(VerticalSpace("20pt"))
    for _ in range(2):
        with doc.create(MiniPage(width=r"0.5\textwidth")):
            for _ in range(6):
                doc.append(HugeText(Math(data=list(generate_equation(var_count=2, max_val=20, mask_random=False)))))
                doc.append(LineBreak())
    doc.generate_pdf()
    doc.generate_tex()
