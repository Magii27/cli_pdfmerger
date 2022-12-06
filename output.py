def header(v):
    print("┌" + "—" * 69 + "┐")
    print("│" + ("<│ PDFMerger " + v + " │>").center(69) + "│")
    print("│" + "<│ by Maksim │>".center(69) + "│")
    print("└ " + "˅" * 67 + " ┘")


def head(text):
    print("┌" + f"< {text} >".center(70, "—"), end="\n")


def endblock():
    print("└" + "—" * 70)


def yninput(text):
    while True:
        check = input(f"│ {text} > ")

        if check.upper() == "Y":
            return True
        elif check.upper() == "N":
            return False


def showlist(list):
    for i, item in enumerate(list):
        print(f"│ [{i + 1}] {item}")

    print("│")
