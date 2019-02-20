# this works when on each line there is a key, value pair


def line_to_dict(string):
    dic = {}
    lst = string.split('\n')

    try:
        for line in lst:
            line = line.split(',')
            # print(line[1], line[2] or None)
            key = str(line[0]).strip('"')
            area = str(line[1]).strip('"')
            # area = area + ", " + str(line[2]).strip('"')
            dic[key] = area

    except IndexError:
        pass
    # print(dic)
    return dic
