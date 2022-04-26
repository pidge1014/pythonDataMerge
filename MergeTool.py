
# Generic data merge utility.  
# This was originally written to replace excel use to merge data from MF file based data where sql is not available, or sources where extracting to csv is the only option.
# IMO, if you need to do any serious work in excel, your in the wrong place and should be coding it.  This tool can help.
# Utility can be used to assemble data from a large number of files, using a primary key present in the data.  
# 
import csv


class DataMerge:
  def __init__(self, keyFileName, dataFileName, desiredFieldsFileName):
    # open the files into objects, create list object from lines of the file of our key fields
    keyFile = open(keyFileName)
    keyFields = [line for line in keyFileName] 
   
    # Open File that contains values for key fields
    # File assumption: The first field in these csv files are the key field.
    dataFile = open(dataFileName)
    dataCollection [][]
    for line in dataFile: 
      with open(line), newline='' as f:
        reader = csv.reader(f)
        data = list(reader)
      
    # Open file that contains the data files

# File that contains desired output fields



