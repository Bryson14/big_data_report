def cut(args):
    """remove sections from each column of csv files"""
    if args[0] == "-f":

        # takes in one or multiple column args.
        iden = args[1:-1]
        # one or multiple identifiers in a list can come out

        try:
            for i in range(len(iden)):
                iden[i] = int(iden[i])

        except ValueError:
            print("Indexes must be positive integers.")

        # print multiple specific columns
        if len(iden) > 1:
            print("mc")
            return print_cut(args[-1], iden)

        # print one specific column
        else:
            print("oc")
            return print_cut(args[-1], iden[0])

    else:
        return(print_cut(args, 0))


def print_cut(file, column):
    lst = []
    if not isinstance(column, list):  # single column
        try:
            for line in open(file):
                line_list = line.strip().split(',')

                if not isinstance(column, list):
                    try:
                        lst.append(line_list[column])
                    except IndexError:
                        print("The index you attempted doesn't exist in this file.", "cut")

        except FileNotFoundError:
            print("File not found, go to cut.py")

    else:  # multiple columns
        try:
            lst.append('')
            j = 0
            for line in open(file):
                line_list = line.strip().split(',')
                for i in range(len(column)):
                    lst[j] = lst[j] + line_list[column[i]]
                    if i < len(column) - 1:
                        lst[j] = lst[j] + ' ,'
                lst.append('')
                j += 1

        except FileNotFoundError:
            print("File not Found, go to cut.py")

    while '' in lst:
        lst.remove('')
    return lst


def paste(args):
    """merge lines of files"""

    data = []
    for file in args:
        try:
            with open(file) as stuff:
                lines = stuff.readlines()

            for i in range(len(lines)):
                lines[i] = lines[i].strip('\n')

            data.append(lines)

        except FileNotFoundError:
            print("File not found, go to paste.py")

    # find the longest file
    max = 0
    for cell in data:
        if len(cell) > max:
            max = len(cell)

    # prints the file in the correct csv format
    for i in range(max):
        for j in range(len(data)):
            if i < len(data[j]):
                print(data[j][i], end="")
            if j < len(data) - 1:
                print(",", end="")
        print("")