# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename:str, select:list=None, types:list=None, has_headers=True,
    delimiter:str=',', silence_errors=False):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)
        records = []

        # Read the file headers if has_headers is True
        if has_headers:
            headers = next(rows)
        else:
            headers = []

        # If a column selector was given, find indices of the specified columns.
        # Also narrow the set of headers used for resulting dictionaries
        if select and headers:
            indices = [ headers.index(colname) for colname in select ]
            headers = select
        elif select: #if there are no headers, treat as tuple and check for select
            if isinstance(select[0], int):
                indices = select
            else:
                raise TypeError('If no headers, then select must be a list of integers')
        else:
            indices = []
        
        for i, row in enumerate(rows):
            if not row:    # Skip rows with no data
                continue
            # Filter the row if specific columns were selected
            try:
                if indices:
                    row = [ row[index] for index in indices ]
                if types:
                    row = [ func(val) for func, val in zip(types, row) ]
                if headers:
                    #Make a dictionary
                    record = dict(zip(headers, row))
                    records.append(record)
                else:
                    record = tuple(ele for ele in row)
                    records.append(record)
            except ValueError as e:
                if not silence_errors:
                    print(f"Row {i+has_headers}: Couldn't convert {row}\n"
                        f'Row {i+has_headers}: Reason {e}')
                else:
                    pass

    return records