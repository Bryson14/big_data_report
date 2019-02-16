import sys
from Grep import grep, endgrep, startgrep
from CutPaste import cut
from Report import Report


def dict_area_titles(d) -> dict:
    fil = d + '\\area_titles.csv'
    area_titles = {}
    ut_list = grep(["-s", "Utah", "-", "000", fil])
    for pair in ut_list:
        pair = pair.split('","')
        area_titles[pair[0].strip('"')] = pair[1].strip('"')

    return area_titles


def find_report_data(d: str, area_dict: dict):
    myfil = d + r'\2017.annual.singlefile.csv'
    myfil = r'C:\Users\Bryson M\Desktop\Methods in CS\Assn2-Text_Tools\data\people.csv'
    results = cut(['-f', 0, 1, 2, myfil])
    print(results)
    pass


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
#
# # Convert `area_titles.csv` into a dictionary
# #############################################
#
#
# # Collect stats from `2017.annual.singlefile.csv`
# #################################################
#
#
# # Create the report object
# ##########################
# rpt = Report()
#
#
# # Fill in the report for all industries
# #######################################
# rpt.all.num_areas           = 1337
#
# rpt.all.gross_annual_wages  = 13333337
# rpt.all.max_annual_wage     = ("Trantor", 123456)
#
# rpt.all.total_estab         = 42
# rpt.all.max_estab           = ("Terminus", 12)
#
# rpt.all.total_empl          = 987654
# rpt.all.max_empl            = ("Anacreon", 654)
#
#
# # Fill in the report for the software publishing industry
# #########################################################
# rpt.soft.num_areas          = 1010
#
# rpt.soft.gross_annual_wages = 101001110111
# rpt.soft.max_annual_wage    = ("Helicon", 110010001)
#
# rpt.soft.total_estab        = 1110111
# rpt.soft.max_estab          = ("Solaria", 11000)
#
# rpt.soft.total_empl         = 100010011
# rpt.soft.max_empl           = ("Gaia", 10110010)
#
#
# # Print the completed report
# ############################
# print(rpt)
