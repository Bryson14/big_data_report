def grep(args):

    if args[0] == '-v':
        exclude(args[2:], args[1])
    else:
        include(args[1:], args[0])


def include(files: list, iden: str):
    lst = []
    for file in files:
        try:
            for line in open(file):
                line = line.strip()
                if iden in line:
                    lst.append(line)

        except FileNotFoundError:
            print("Given file not found.")

    return lst


def exclude(files: list, iden: str):
    lst = []
    for file in files:
        try:
            for line in open(file):
                line = line.strip()
                if iden not in line:
                    lst.append(line)

        except FileNotFoundError:
            print("Given file not found.")

    return lst


def startgrep(args):

    if args[0] == '-v':
        excludestart(args[2:], args[1])
    else:
        includestart(args[1:], args[0])


def includestart(files: list, iden: str):
    lst = []
    for file in files:
        try:
            for line in open(file):
                line = line.strip()
                if line.startswith(iden):
                    lst.append(line)

        except FileNotFoundError:
            print("file not found. ")

    return lst


def excludestart(files: list, iden: str):
    lst = []
    for file in files:
        try:
            for line in open(file):
                line = line.strip()
                if not line.startswith(iden):
                    lst.append(line)

        except FileNotFoundError:
            print("File not found.")

    return lst


def endgrep(args):
    if args[0] == '-v':
        excludeend(args[2:], args[1])
    else:
        includeend(args[1:], args[0])


def includeend(files: list, iden: str):
    lst = []
    for file in files:
        try:
            for line in open(file):
                line = line.strip()
                if line.endswith(iden):
                    lst.append(line)

        except FileNotFoundError:
            print("file not found. ")

    return lst


def excludeend(files: list, iden: str):
    lst = []
    for file in files:
        try:
            for line in open(file):
                line = line.strip()
                if not line.endswith(iden):
                    lst.append(line)

        except FileNotFoundError:
            print("File not found.")

    return lst
