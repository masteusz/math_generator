import os.path

import pylatex.tikz
from pylatex import Document, PageStyle, Head, MiniPage, LineBreak, MediumText, Math, VerticalSpace, HugeText, NewPage
from pylatex.utils import NoEscape
from equation_gen import generate_equation

OUTPUT_DIR = "out"


def gen_pdf(
    pdf_name: str,
    filepath: str,
    addition: bool = True,
    mask_random: bool = False,
    max_val: int = 20,
    var_count: int = 2,
    pages: int = 1,
):
    geometry_options = {
        "head": "40pt",
        "lmargin": "0.3in",
        "rmargin": "0.3in",
        "tmargin": "0.2in",
        "bmargin": "0.2in",
        "includeheadfoot": True,
    }

    doc = Document(pdf_name, geometry_options=geometry_options)
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
    for page in range(pages):
        for _ in range(2):
            with doc.create(MiniPage(width=r"0.5\textwidth")):
                for _ in range(7):
                    doc.append(
                        HugeText(
                            Math(
                                data=list(
                                    generate_equation(
                                        var_count=var_count,
                                        max_val=max_val,
                                        mask_random=mask_random,
                                        add=addition,
                                    )
                                )
                            )
                        )
                    )
                    doc.append(LineBreak())
        doc.append(NewPage())
    doc.generate_pdf(filepath=filepath)


if __name__ == "__main__":
    gen_pdf(
        pdf_name=f"addition",
        filepath=os.path.join(OUTPUT_DIR, f"addition"),
        addition=True,
        mask_random=False,
        max_val=30,
        var_count=2,
        pages=10,
    )

    gen_pdf(
        pdf_name=f"addition_3val",
        filepath=os.path.join(OUTPUT_DIR, f"addition_3val"),
        addition=True,
        mask_random=False,
        max_val=12,
        var_count=3,
        pages=10,
    )

    gen_pdf(
        pdf_name=f"addition_masked",
        filepath=os.path.join(OUTPUT_DIR, f"addition_masked"),
        addition=True,
        mask_random=True,
        max_val=20,
        var_count=2,
        pages=10,
    )
    gen_pdf(
        pdf_name=f"subtraction",
        filepath=os.path.join(OUTPUT_DIR, f"subtraction"),
        addition=False,
        mask_random=False,
        max_val=15,
        var_count=2,
        pages=10,
    )
    gen_pdf(
        pdf_name=f"subtraction_masked",
        filepath=os.path.join(OUTPUT_DIR, f"subtraction_masked"),
        addition=False,
        mask_random=True,
        max_val=12,
        var_count=2,
        pages=10,
    )
