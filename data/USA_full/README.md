
## [BLS Quarterly Census of Employment and Wages](https://www.bls.gov/cew/datatoc.htm)

This is the home page for this data set.  Here you can find the most official
documentation about this data set as well as data sets for previous quarters
and years.  In the past the official version of this file had been changed
without warning, which led to confusion as it changed the results our programs
came up with.  To avoid this problem you will download the big data file from
Canvas instead.

2017 Annual Averages Single File CSV.  Download and unzip this file into this
directory, leaving its filename intact.
    https://data.bls.gov/cew/data/files/2017/csv/2017_annual_singlefile.zip


[QCEW Area Code Guide] (https://data.bls.gov/cew/doc/titles/area/area_guide.htm)
This document explains how the FIPS area codes are constructed.


Interpretation of the columns in this CSV file.  Note that the singlefile CSV
is missing about 8 of the columns listed here.
    https://data.bls.gov/cew/doc/layouts/csv_annual_layout.htm

The Pythonic way to consume this CSV file:
    https://docs.python.org/3.6/library/csv.html
    We won't do this, since our requirements are special.  Plus, this CSV
    module would likely consume a *lot* of RAM since it will slurp in the
    entirety of the ~490MB CSV file.  But this may come in handy for you as you
    write your code.
