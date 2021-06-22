#!/usr/bin/env python

import pandas as pd
import sys
import os
import glob
import fnmatch
import re

#region Time function
...
import atexit
from time import time, strftime, localtime
from datetime import timedelta

def secondsToStr(elapsed=None):
    if elapsed is None:
        return strftime("%Y-%m-%d %H:%M:%S", localtime())
    else:
        return str(timedelta(seconds=elapsed))

def log(s, elapsed=None):
    line = "="*40
    print(line)
    print(secondsToStr(), '-', s)
    if elapsed:
        print("Elapsed time:", elapsed)
    print(line)
    print()

def endlog():
    end = time()
    elapsed = end-start
    log("End Program", secondsToStr(elapsed))

start = time()
atexit.register(endlog)
log("Start Program")
#endregion

filetypes = ["*.xlsx","*.xls"]

#region First amplitude <30 Hz script
...

input_path = sys.argv[1]
writer = pd.ExcelWriter(input_path + os.sep + "HighestAmplitudeCombined.xlsx")
print('Getting first amplitudes <30 Hz! Outputting to ' + input_path + os.sep + "HighestAmplitudeCombined.xlsx")


for filename in os.listdir(input_path):
    for filetype in filetypes:
        if fnmatch.fnmatch(filename, filetype):
            workbook1 = glob.glob(os.path.join(input_path, "AveSpectrum*" + filetype)) #Only reads files named AveSpectrum and is excel (xlsx or xml)
            all_df = []
            for workbook in workbook1:
                workbook1 = pd.read_excel(workbook, sheet_name='Modes')
                for j in range(len(workbook1)):
                    if workbook1.frequencies.iloc[j] < 30:
                        firstrow = pd.DataFrame(columns=['frequencies', 'Amplitude'])
                        firstrow = firstrow.append(workbook1.iloc[j])
                        break
                firstrow['source'] = workbook.replace(input_path + os.sep, '')
                all_df.append(firstrow)
            data_concatenated = pd.concat(all_df, axis=0)
            data_concatenated.to_excel(writer, sheet_name="Modes",index=False)
        else:
            pass

writer.save()
print('Script complete!')
#endregion
