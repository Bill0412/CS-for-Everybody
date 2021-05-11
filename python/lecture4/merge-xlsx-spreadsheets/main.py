import pandas as pd
import numpy as np
import os
from typing import List


data_path = 'data'
spreadsheet_suffix = '.xlsx'


def load_files(path: str, suffix: str) -> List[str]:
    files = list()
    for filename in os.listdir(path):
        if filename == '' or filename[-5:] != suffix or filename[0] == '~':
            print('file {} is skipped'.format(filename))
            continue
        files.append(os.path.join(data_path, filename))
    return files


def read_excel(filename: str) -> pd.DataFrame:
    return pd.read_excel(filename, header=None)


def remove_row(df, row_num):
    def major_component(df, row_num='F') -> str:
        """
        :param df: the dataframe
        :param row_num: the row number to examine
        returns one of `nan`, `int` or `str`, which is with the highest frequency
        """
        if type(row_num) == str:
            row_num = ord(row_num.lower()) - ord('a') 
        freq = {
            'nan': 0,
            'num': 0, # numeric
            'str': 0
        }
        n_row = df.shape[0]
        for i in range(n_row):
            if type(df.iloc[i, 0]) != int:
                continue
            else:
                # skip the non-data rows
                cell = df.iloc[i, row_num]
                if pd.isna(cell):
                    freq['nan'] += 1
                elif type(cell) == str:
                    freq['str'] += 1
                elif type(cell) == int or type(cell) == np.float64:
                    freq['num'] += 1
                
        print(freq)
        return max(freq, key=freq.get)

    if major_component(df, row_num) == 'num':
        return False
    return True


def process_df(df, row_might_remove='F', n_col_kept=7):
    if type(row_might_remove) == str:
        row_might_remove = ord(row_might_remove.lower()) - ord('a')
    res_df = pd.DataFrame()
    
    print(res_df)

    if remove_row(df, row_might_remove):
        res_df = pd.concat(
            [df.iloc[:, :row_might_remove], df.iloc[:, row_might_remove+1:n_col_kept+1]],
            axis=1)
    else:
        res_df = df.iloc[:, :n_col_kept]
    res_df.columns = [str(i) for i in range(n_col_kept)]
    return res_df


if __name__ == '__main__':
    files = load_files(data_path, spreadsheet_suffix)
    all_df = pd.DataFrame()
    for file in files:
        df = process_df(read_excel(file))
        print(df.shape)
        all_df = pd.concat([all_df, process_df(df)], axis=0)
    all_df.to_excel("output.xlsx")
