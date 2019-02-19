import sys
from Grep import grep, endgrep
from Report import Report
from ConvertLine import line_to_dict


def dict_area_titles(d):
    fil = d + '\\area_titles.csv'
    no000 = endgrep(["-v", '000"', fil])
    noC = grep(["-v", 'C', no000])
    noS = grep(["-v", 'S', noC])
    noa = grep(["-v", 'a', noS])
    area_titles = line_to_dict(noa)
    return area_titles


def find_report_data(d: str, area_dict: dict):
    rpt = Report()
    myfil = d + '\\2017.annual.singlefile.csv'
    first_line = True
    for line in open(myfil):
        if not first_line:
            line = line.split(',')
            own_code = line[1]
            industry_code = line[2]
            estab = int(line[8])
            empl = int(line[9])
            wages = int(line[10])
            key = str(line[0]).strip('"')
            # print(key in area_dict)
            if key in area_dict:
                # print(own_code, industry_code, estab, empl, wages)

                # all industry info
                if own_code == '"0"' and industry_code == '"10"':
                    rpt.all.num_areas += 1

                    rpt.all.total_estab += estab
                    if estab > rpt.all.max_estab[1]:
                        rpt.all.max_estab = (area_dict[key], estab)

                    rpt.all.total_empl += empl
                    if empl > rpt.all.max_empl[1]:
                        rpt.all.max_empl = (area_dict[key], empl)

                    rpt.all.gross_annual_wages += wages
                    if wages > rpt.all.max_annual_wage[1]:
                        rpt.all.max_annual_wage = (area_dict[key], wages)

                # software sector info
                if own_code == '"5"' and industry_code == '"5112"':
                    rpt.soft.num_areas += 1

                    rpt.soft.total_estab += estab
                    if estab > rpt.soft.max_estab[1]:
                        rpt.soft.max_estab = (area_dict[key], estab)

                    rpt.soft.total_empl += empl
                    if empl > rpt.soft.max_empl[1]:
                        rpt.soft.max_empl = (area_dict[key], empl)

                    rpt.soft.gross_annual_wages += wages
                    if wages > rpt.soft.max_annual_wage[1]:
                        rpt.soft.max_annual_wage = (area_dict[key], wages)
        first_line = False

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
