def grep(args):

    if args[0] == '-v':
        exclude(args[2:], args[1])
    else:
        include(args[1:], args[0])


def include(files: list, iden: str):
    print("")
    for file in files:
        try:
            with open(file) as data:
                lines = data.readlines()

            # remove \n left over from .readlines()
            for i in range(len(lines)):
                lines[i] = lines[i][:-1]

            for line in lines:
                if line.find(iden) != -1:
                    print(line)

        except FileNotFoundError:
            print("Given file not found.")


def exclude(files: list, iden: str):
    print("")
    for file in files:
        try:
            with open(file) as data:
                lines = data.readlines()

            # remove \n left over from .readlines()
            for i in range(len(lines)):
                lines[i] = lines[i][:-1]

            for line in lines:
                if line.find(iden) == -1:
                    print(line)

        except FileNotFoundError:
            print("Given file not found.")

def startgrep(args):

    if args[0] == '-v':
        excludestart(args[2:], args[1])
    else:
        includestart(args[1:], args[0])


def includestart(files: list, iden: str):
    print("")
    for file in files:
        try:
            with open(file) as data:
                lines = data.readlines()

            # remove \n left over from .readlines()
            for i in range(len(lines)):
                lines[i] = lines[i][:-1]

            for line in lines:
                if line.startswith(iden):
                    print(line)

        except FileNotFoundError:
            print("file not found. ")


def excludestart(files: list, iden: str):
    print("")
    for file in files:
        try:
            with open(file) as data:
                lines = data.readlines()

            # remove \n left over from .readlines()
            for i in range(len(lines)):
                lines[i] = lines[i][:-1]

            for line in lines:
                if line.startswith(iden):
                    print(line)

        except FileNotFoundError:
            print("File not found.")


def endgrep(args):
    if args[0] == '-v':
        excludeend(args[2:], args[1])
    else:
        includeend(args[1:], args[0])


def includeend(files: list, iden: str):
    print("")
    for file in files:
        try:
            with open(file) as data:
                lines = data.readlines()

            # remove \n left over from .readlines()
            for i in range(len(lines)):
                lines[i] = lines[i][:-1]

            for line in lines:
                if line.endswith(iden):
                    print(line)

        except FileNotFoundError:
            print("file not found. ")


def excludeend(files: list, iden: str):
    print("")
    for file in files:
        try:
            with open(file) as data:
                lines = data.readlines()

            # remove \n left over from .readlines()
            for i in range(len(lines)):
                lines[i] = lines[i][:-1]

            for line in lines:
                if line.endswith(iden):
                    print(line)

        except FileNotFoundError:
            print("File not found.")

