import pynmea2, datetime, sys
import pandas as pd
import numpy as np

import functions as fct

def addRowInDataFrame(raw_row, df):
    for i, msg in enumerate(raw_row):
        mtype = type(msg).__name__

        if fct.functions.has_key(mtype):
            getDataFunction = fct.functions[mtype]

            rows = getDataFunction(msg)
            cols = fct.columns[mtype]

            print('-> {}: {}'.format(mtype, repr(cols)))
            print(repr(rows))
            # Create DataFrame or Series
        else:
            continue

    # Concat row in DataFrame if it is valid
    return None


v = []
e = []
first = None
row = []
df = None

with open('test.nmea', 'r') as f:
    for line in f:
        try:
            msg = pynmea2.parse(line)
            if type(msg).__name__ == 'TXT':
                print(repr(msg))
            else:
                v.append(msg)
                if first == None:
                    first = msg
                elif msg == first:
                    df = addRowInDataFrame(row, df)
                    row = []
                row.append(msg) 
        except:
            e.append(sys.exc_info()[0])

if len(row) > 0:
    df = addRowInDataFrame(row, df)

print("Ok")
