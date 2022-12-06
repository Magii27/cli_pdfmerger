import os
from glob import glob

import PyPDF2
from PyPDF2 import PdfFileMerger

import function as f
import output as out

VERSION = "v1.0"

out.header(VERSION)

start = True
while True:
    if start:
        out.head("INPUT")

        while True:
            SOURCE = input(
                "│ Path to PDFs > ")  # "C:\\Users\\q506869\\OneDrive - BMW Group\\Dokumente\\01_Ausbildung\\Übernahme"  # input("Pfad angeben > ")

            if "\\" not in SOURCE:
                continue

            OUT_NAME = input("│ PDF output name > ")

            break

    else:
        out.head("Change directory? (y/n)")
        if out.yninput("Input"):
            while True:
                SOURCE = input("│ Path to PDFs > ")  # input("Pfad angeben > ")

                if "\\" not in SOURCE and "/" not in SOURCE:
                    print("│ [INFO] Need a Path")
                    continue

                OUT_NAME = input("│ PDF output name > ")

                break

    if SOURCE[len(SOURCE) - 1] != "\\":
        SOURCE += "\\"
    if ".pdf" not in OUT_NAME:
        OUT_NAME += ".pdf"

    pdf_list = []
    for i, item in enumerate(os.listdir(SOURCE)):
        if item.endswith('.pdf'):
            pdf_list.append(item)

    if len(pdf_list) == 0:
        print("│ [INFO] No PDFs in directory found")
        out.endblock()
        continue

    out.endblock()

    out.head("Operation needed (order, exclude)? (y/n)")
    operation = out.yninput("Input")
    out.endblock()

    if operation:
        first = True

        while True:
            if first:
                out.head("Change (c) - Exclude (e) - Continue (x)")
                first = False

            op = input("│ Input > ")

            if op.upper() == "C":
                out.endblock()
                pdf_list = f.changelist(pdf_list)
                first = True

                continue

            if op.upper() == "E":
                out.endblock()
                pdf_list = f.editlist(pdf_list)
                first = True

                continue

            if op.upper() == "X":
                out.endblock()

                break

    out.head("Order")
    out.showlist(pdf_list)
    out.endblock()

    while True:
        out.head("Start merging? (y/n)")

        if not out.yninput("Execute"):
            start = False
            out.endblock()
            break

        else:
            out.endblock()

            merger = PyPDF2.PdfWriter()

            for item in pdf_list:
                tmp_pdf = PyPDF2.PdfFileReader(SOURCE + item)
                for page in tmp_pdf.pages:
                    merger.addPage(page=page)

            merger.write(open(SOURCE + OUT_NAME, 'wb'))

            print(" PDF CREATED ".center(70, "—"))
            print("\n\n")
            start = False
            break
