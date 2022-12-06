import output as out


def changelist(listofpdfs):
    while True:
        out.head("Order (x=exit)")

        out.showlist(listofpdfs)
        pos1 = input("│ Change > ")

        if pos1.upper() == "X":
            break
        pos2 = input("│ To > ")
        if pos2.upper() == "X":
            break
        try:
            pos1 = int(pos1) - 1
            pos2 = int(pos2) - 1
        except ValueError:
            print("│ [INFO] Need a numeric input for change")
        try:
            tmp = listofpdfs[pos1]
            listofpdfs[pos1] = listofpdfs[pos2]
            listofpdfs[pos2] = tmp
        except IndexError:
            print("│ [INFO] Wrong index input")

        out.endblock()

    out.endblock()

    return listofpdfs


def editlist(listofpdfs):
    while True:
        out.head("Exclude (x=exit)")

        out.showlist(listofpdfs)
        pos = input("│ Exclude > ")

        if pos.upper() == "X":
            out.endblock()
            return listofpdfs

        try:
            pos = int(pos) - 1
        except ValueError:
            print("│ [INFO] Need a numeric input for change")

        try:
            listofpdfs.pop(pos)
        except IndexError:
            print("│ [INFO] Wrong index input")

        out.endblock()
