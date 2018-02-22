# csv_to_sql
code for converting .csv files to .db (sqlite) using pandas and sqlalchemy
'''
This Program imports all csv files in given directory path
Remember all csv file metadata should be numeric and if text is included, individual text data shouldn't have any character = ","
'''

import pandas as pd
import os, re
import numpy as np
import sqlalchemy as sql
from sqlalchemy import create_engine

# Create a regex that matches a name pattern with the .csv extension filenames.
Pattern1 = re.compile(r"""^(.*?) # all text before the decimal
       .
       csv
       (.*?)$                   # all text after the decimal
""", re.VERBOSE)
'''
Passing re.VERBOSE for the second argument will allow whitespace and comments in
the regex string to make it more readable.
'''
# Create a sqlite file named filename.db
sql_engine = create_engine('sqlite:///test.db', echo=False)
connection = sql_engine.raw_connection()

#initialize a list
csvDF = [] #for storing dataframes
csvFilename = [] #for storing filenames, this will be helpfull in naming tables of SQL as per differnet csv files

# path for the directory where multiple .csv files will be stored
path = os.path.abspath('D:\\A\\A1\\A1.1\\A1.1.1\\A1.1.1.1')
for Filename in os.listdir(path):
    file = Pattern1.search(Filename)
    
# Skip files without the matching pattern.
    if file == None:
        continue
    
    Filename = os.path.join(path, Filename)
    try:
        df = pd.read_csv(Filename, header = 0)
        csvFilename.append(df)
        csvDF.append(format(file.group(0)))
        print("file saved in dataframe"+" "+format(file.group(0))[:-4])
        df.to_sql(format(file.group(0))[:-4], connection,index=False, if_exists='append')
    # some csv files may throw utf-8 decode error
    except:
        print("error in file {}".format(file.group(0)))



