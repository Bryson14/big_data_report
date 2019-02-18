def grep(args):

    if args[0] == '-v':
        return exclude(args[2], args[1])
    else:
        return include(args[1:], args[0])


def include(files: list, iden: str):
    string = ''
    for file in files:
        try:
            for line in open(file):
                if iden in line.strip():
                    string += line

            return string

        except FileNotFoundError:
            print("Given file not found.")


def exclude(strng: str, iden: list):
    string = ''
    lines = strng.split('\n')
    for line in lines:
        cells = line.split(',')
        if iden not in cells[0]:
            string += (line + '\n')
    return string


def endgrep(args):
    if args[0] == '-v':
        return excludeend(args[2], args[1])
    else:
        return includeend(args[1], args[0])


def includeend(files: list, iden: str):
    string = ''
    for file in files:
        try:
            for line in open(file):
                line1 = line.strip().split(',')
                if line1[0].endswith(iden):
                    string += line

            return string

        except FileNotFoundError:
            print("File not found.")


def excludeend(file: str, iden: str):
    string = ''
    try:
        for line in open(file):
            line1 = line.strip().split(',')
            if not line1[0].endswith(iden):
                string += line

        return string

    except FileNotFoundError:
        print("File not found.")
