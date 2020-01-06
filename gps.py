import pynmea2, datetime, sys
import pandas as pd
import numpy as np

import functions as fct

filename = 'test.nmea'
output = 'out.csv'

def addRowInDataFrame(raw_row, df):
    df_concat = []
    for i, msg in enumerate(raw_row):
        mtype = type(msg).__name__

        if mtype in fct.functions:
            getDataFunction = fct.functions[mtype]

            rows = getDataFunction(msg)
            cols = fct.columns[mtype]

            df_concat.append(pd.DataFrame([rows], columns=cols))
        else:
            continue

    df_row = pd.concat(df_concat, axis=1)
    valid = df_row.get('Valid?')[0]

    # Concat row in DataFrame if it is valid
    if valid:
        df = pd.concat([df, df_row])

    return df


e = []
row = []
first = None
data = pd.DataFrame()

total_lines = 0

with open(filename, 'r') as f:
    for line in f:
        total_lines += 1

with open(filename, 'r') as f:
    i = 0
    for line in f:
        i += 1
        print('Line {}/{}'.format(i, total_lines), end='\r')
        try:
            msg = pynmea2.parse(line)
            if type(msg).__name__ == 'TXT':
                pass
                # print('Ignoring TXT message', end='\r')
                # print(repr(msg))
            else:
                if first == None:
                    first = msg
                elif type(msg) == type(first):
                    data = addRowInDataFrame(row, data)
                    row = []
                row.append(msg)
        except:
            e.append(sys.exc_info()[0])

if len(row) > 1:
    data = addRowInDataFrame(row, data)

data.to_csv(output, index=False)

print('')

if len(e) == 0:
    print('Ok')
else:
    print('There were some errors')
    for err in e:
        print(repr(err))

