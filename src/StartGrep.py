def startgrep(args):

    if args[0] == '-v':
        exclude(args[2:], args[1])
    else:
        include(args[1:], args[0])


def include(files: list, iden: str):
    print("")
    l = len(iden)
    for file in files:
        try:
            with open(file) as data:
                lines = data.readlines()

            # remove \n left over from .readlines()
            for i in range(len(lines)):
                lines[i] = lines[i][:-1]

            for line in lines:
                if line[:l] == iden:
                    print(line)

        except FileNotFoundError:
            print("file not found. ")


def exclude(files: list, iden: str):
    print("")
    l = len(iden)
    for file in files:
        try:
            with open(file) as data:
                lines = data.readlines()

            # remove \n left over from .readlines()
            for i in range(len(lines)):
                lines[i] = lines[i][:-1]

            for line in lines:
                if line[:l] == iden:
                    print(line)

        except FileNotFoundError:
            print("File not found.")
