import sys
from Grep import grep, endgrep
from Report import Report
from ConvertLine import line_to_dict


def dict_area_titles(d):
    fil = d + '\\area_titles.csv'
    nozeros = endgrep(["-v", '000"', fil])
    noletters = grep(["-v", 'C', nozeros])
    noletters2 = grep(["-v", 'S', noletters])
    noletters3 = grep(["-v", 'a', noletters2])
    area_titles = line_to_dict(noletters3)
    return area_titles


def find_report_data(d: str, area_dict: dict):
    rpt = Report()
    myfil = d + '\\2017.annual.singlefile.csv'

    for line in open(myfil):
        line_lst = line.split(',')
        if line_lst[0] in area_dict:

            # all industry info
            if line_lst[1] == "0" and line_lst[2] == "10":

                rpt.all.total_estab += line_lst[8]
                if line_lst[8] > rpt.all.max_estab[1]:
                    rpt.all.max_estab = (area_dict[line_lst[0]], line_lst[8])

                rpt.all.total_empl += line_lst[9]
                if line_lst[9] > rpt.all.max_empl[1]:
                    rpt.all.max_empl = (area_dict[line_lst[0]], line_lst[9])

                rpt.all.gross_annual_wages += line_lst[10]
                if line_lst[10] > rpt.all.max_annual_wage[1]:
                    rpt.all.max_annual_wage = (area_dict[line_lst[0]], line_lst[10])

            # software sector info
            if line_lst[1] == "0" and line_lst[2] == "5112":

                rpt.soft.total_estab += line_lst[8]
                if line_lst[8] > rpt.soft.max_estab[1]:
                    rpt.soft.max_estab = (area_dict[line_lst[0]], line_lst[8])

                rpt.soft.total_empl += line_lst[9]
                if line_lst[9] > rpt.soft.max_empl[1]:
                    rpt.soft.max_empl = (area_dict[line_lst[0]], line_lst[9])

                rpt.soft.gross_annual_wages += line_lst[10]
                if line_lst[10] > rpt.soft.max_annual_wage[1]:
                    rpt.soft.max_annual_wage = (area_dict[line_lst[0]], line_lst[10])
    print(rpt)

def main():
    # too little arguments
    if len(sys.argv) < 2:
        print("Usage: src\main.py DATA_DIRECTORY")
        sys.exit(1)

    # initializes the program
    elif len(sys.argv) == 2:
        area_dict = dict_area_titles(sys.argv[1])
        find_report_data(sys.argv[1], area_dict)

    # unidentified function call
    else:
        print("Too many arguments given\nUsage: src\main.py DATA_DIRECTORY")
        sys.exit(1)


if __name__ == "__main__":
    main()
