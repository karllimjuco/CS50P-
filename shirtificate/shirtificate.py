import os

from fpdf import FPDF

SHIRT_IMAGE = os.path.join(os.path.dirname(__file__), "shirtificate.png")


def main():
    name = input("Name: ")
    make_shirtificate(name, "shirtificate.pdf")


def make_shirtificate(name, output):
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    # Title, centered horizontally near the top.
    pdf.set_font("Helvetica", "B", 28)
    pdf.cell(0, 40, "CS50 Shirtificate", align="C")

    # Shirt image, centered horizontally.
    img_width = 170
    x = (pdf.w - img_width) / 2
    pdf.image(SHIRT_IMAGE, x=x, y=60, w=img_width)

    # Name in white text, overlaid on the shirt.
    pdf.set_font("Helvetica", "B", 20)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(0, 110)
    pdf.cell(0, 10, f"{name} took CS50", align="C")

    pdf.output(output)


if __name__ == "__main__":
    main()