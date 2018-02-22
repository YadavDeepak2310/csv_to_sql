'''
This Program import all csv files in given directory path
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
# create a sqlite database file, you can rename the file as required
sql_engine = create_engine('sqlite:///test.db', echo=False)
connection = sql_engine.raw_connection()

#initialize a list
csvDF = []
csvFilename = [] # this list holds the filenames of .csv files in directory which will be used to name tables in sqlite

directory path which stores .csv files
path = os.path.abspath('D:\\aaa\\bbb\\ccc')

for Filename in os.listdir(path):
    file = Pattern1.search(Filename)
    
# Skip files without the matching pattern.
    if file == None:
        continue
    
    Filename = os.path.join(path, Filename)
    try:
        df = pd.read_csv(Filename, header = 0) #read individual csv files
        csvFilename.append(df) #append names of file in list
        csvDF.append(format(file.group(0))) #append dataframes in list
        print("file saved in dataframe"+" "+format(file.group(0))[:-4])
        df.to_sql(format(file.group(0))[:-4], connection,index=False, if_exists='append') #db file is created in directory of this code
    # some csv files throu 'utf-8' decode error
    except:
        print("error in file {}".format(file.group(0)))



