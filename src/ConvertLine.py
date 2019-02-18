# this works when on each line there is a key, value pair
def line_to_dict(string):
    dic = {}
    printed = False
    lst = string.split('\n')

    try:
        for line in lst:
            line = line.split(',')
            key = str(line[0]).strip('"')
            value = str(line[1]).strip('"')
            dic[key] = value
    except IndexError:
        pass

    return dic