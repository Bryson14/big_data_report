import sys
from Partial import head

if __name__ == "__main__":

    # too little arguments
    if len(sys.argv) < 2:
        print("Usage: src\main.py DATA_DIRECTORY")
        sys.exit(1)

    # initializes the program
    elif len(sys.argv) == 2:
        try:
            head(sys.argv[1:])

        except FileNotFoundError:
            print("File not found.")
        sys.exit(1)

    # unidentified function call
    else:
        print("Too many arguments given\nUsage: src\main.py DATA_DIRECTORY")
        sys.exit(1)

# Convert `area_titles.csv` into a dictionary
#############################################


# Collect stats from `2017.annual.singlefile.csv`
#################################################


# Create the report object
##########################
rpt = Report()


# Fill in the report for all industries
#######################################
rpt.all.num_areas           = 1337

rpt.all.gross_annual_wages  = 13333337
rpt.all.max_annual_wage     = ("Trantor", 123456)

rpt.all.total_estab         = 42
rpt.all.max_estab           = ("Terminus", 12)

rpt.all.total_empl          = 987654
rpt.all.max_empl            = ("Anacreon", 654)


# Fill in the report for the software publishing industry
#########################################################
rpt.soft.num_areas          = 1010

rpt.soft.gross_annual_wages = 101001110111
rpt.soft.max_annual_wage    = ("Helicon", 110010001)

rpt.soft.total_estab        = 1110111
rpt.soft.max_estab          = ("Solaria", 11000)

rpt.soft.total_empl         = 100010011
rpt.soft.max_empl           = ("Gaia", 10110010)


# Print the completed report
############################
print(rpt)
