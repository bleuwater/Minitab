# import os
# import shutil
# import openpyxl
import pandas as pd
# import numpy as np


df_base = pd.read_excel('SPC_DATA.xlsx', sheet_name='Sheet1', header=0, converters={'CREATE_DATE': str})

for inx in df_base.index:
    dt_err = df_base.loc[inx, 'CREATE_DATE'][8:]
#    print(dt_err)
    if len(dt_err) == 5:
        if int(dt_err[:2]) > 23:
            df_fix = '0' + dt_err
        elif int(dt_err[1:3]) > 59:
            df_fix = dt_err[:2] + '0' + dt_err[2:]
        elif int(dt_err[3:5]) > 59:
            df_fix = dt_err[:4] + '0' + dt_err[4]
        else:
            df_fix = '0' + dt_err

        df_base.loc[inx, 'CREATE_DATE'] = df_base.loc[inx, 'CREATE_DATE'][:8] + df_fix
        print(inx, df_base.loc[inx, 'CREATE_DATE'])

    elif len(df_base.loc[inx, 'CREATE_DATE']) > 14:
        print(inx)

df_base.to_csv('SPC_DATA.txt', index=False)
