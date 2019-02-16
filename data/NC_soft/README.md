This dataset was generated from a full copy of the data file
`2017.annual.singlefile.csv` using a version of `tt.py` containing the
'startgrep' subcommand and this sequence of commands:

## Linux

    $ python tt.py head -n 1 2017.annual.singlefile.csv > header.csv
    $ python tt.py startgrep '"37' 2017.annual.singlefile.csv > dat.csv
    $ python tt.py grep '"5","5112"' dat.csv > trimmed.csv
    $ python tt.py cat header.csv trimmed.csv > 2017.annual.singlefile.csv
    $ rm header.csv dat.csv trimmed.csv


## Windows

    C:\> python tt.py head -n 1 2017.annual.singlefile.csv > header.csv
    C:\> python tt.py startgrep """37" 2017.annual.singlefile.csv > dat.csv
    C:\> python tt.py grep """5""","""5112""" dat.csv > trimmed.csv
    C:\> python tt.py cat header.csv trimmed.csv > 2017.annual.singlefile.csv
    C:\> del header.csv dat.csv trimmed.csv
